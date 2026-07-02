import streamlit as st
import pandas as pd
import requests

st.title("🍿 Movie Analytics Explorer")

movie_name = st.text_input("Enter a movie title:", "The Matrix")

if st.button("Search"):
    
    api_key = st.secrets["omdb_key"]
    url = "https://www.omdbapi.com/"
    my_params = {
        "t": movie_name,
        "apikey": api_key
    }
    
    response = requests.get(url, params=my_params)
    
    if response.status_code == 200:
        data = response.json()
        
        # --- THE BOUNCER ---
        # We check if OMDb actually found the movie before extracting data!
        if data.get("Response") == "True":
            
            title = data['Title']
            
            # Not all movies have posters. We use a fallback if it's missing!
            poster_url = data.get('Poster', 'https://via.placeholder.com/300x450?text=No+Poster')
            plot = data.get('Plot', 'No plot available.')
            
            st.subheader(title)
            
            # Streamlit will crash if the image URL is literally "N/A"
            if poster_url != "N/A":
                st.image(poster_url)
                
            st.write(f"**Plot:** {plot}")

            st.divider() 
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(label="IMDB Rating", value=data.get('imdbRating', 'N/A'))
            with col2:
                st.metric(label="Metascore", value=data.get('Metascore', 'N/A'))
            with col3:
                st.metric(label="Runtime", value=data.get('Runtime', 'N/A'))

            st.subheader("Ratings Chart")
            
            def clean_rating(value_str):
                if "%" in value_str:
                    return float(value_str.replace("%", ""))
                elif "/100" in value_str:
                    return float(value_str.replace("/100", ""))
                elif "/10" in value_str:
                    return float(value_str.replace("/10", "")) * 10
                return 0.0

            ratings_list = []
            
            # We also check if the "Ratings" list actually exists and has items
            if "Ratings" in data and len(data["Ratings"]) > 0:
                for item in data['Ratings']:
                    source_name = item['Source']
                    raw_value = item['Value']
                    clean_score = clean_rating(raw_value)
                    ratings_list.append({"Reviewer": source_name, "Score": clean_score})
                    
                df = pd.DataFrame(ratings_list)
                chart_data = df.set_index('Reviewer')
                st.bar_chart(chart_data)
            else:
                st.info("No detailed ratings available to chart for this movie.")
                
        else:
            # If Response is "False", we gracefully show the user the error message
            st.warning(f"Oops! {data.get('Error', 'Movie not found.')}")
            
    else:
        st.error(f"API Error: Status Code {response.status_code}")