# 🍿 Movie Analytics Explorer

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://YOUR_STREAMLIT_APP_URL_HERE)

A cloud-based data dashboard that dynamically pulls, cleans, and visualizes movie data in real-time using the OMDb API. 

## 🎯 Project Overview
This application serves as a demonstration of full-stack Python development, focusing on RESTful API integration, data wrangling, and interactive UI design. It handles user inputs securely, formats URL parameters to prevent internet request failures, and gracefully manages missing or incomplete JSON database entries.

### ✨ Key Features
* **Live API Integration:** Fetches real-time JSON data from the Open Movie Database (OMDb).
* **Dynamic Data Visualization:** Cleans raw string data (e.g., "83%") into floating-point numbers to render comparative bar charts for cross-platform movie ratings (IMDB, Rotten Tomatoes, Metacritic).
* **Fault-Tolerant Design:** Includes "bouncer" logic to gracefully handle invalid user queries or missing database entries without crashing the application.
* **Secure Credential Management:** Utilizes Streamlit Secrets to securely inject API keys during cloud deployment, preventing credential leaks.

## 🛠️ Technology Stack
* **Frontend/Deployment:** Streamlit, Streamlit Community Cloud
* **Data Processing:** Pandas
* **Network Requests:** Python `requests` library

## 💻 Run it Locally

1. Clone this repository:
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/movie-explorer-app.git](https://github.com/YOUR_GITHUB_USERNAME/movie-explorer-app.git)
