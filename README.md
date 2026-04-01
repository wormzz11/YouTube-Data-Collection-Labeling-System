# YouTube Data Collection & Labeling Pipeline

<div style="display: flex; gap: 20px;">
  <img src="https://github.com/user-attachments/assets/fb173f96-ba64-4959-b8cc-880d14db28f9" width="400"/>
  <img src="https://github.com/user-attachments/assets/5917a6af-e8b1-4f7c-aedb-c4d3d6ef9646" width="400"/>
</div>

## Project Overview
This project is a data pipeline and labeling platform designed to build ground-truth datasets from YouTube video data. It enables users to collect video metadata, assign theme-based relevance labels via an intuitive interface, and export the labeled data in ML-ready formats.

## Features
- Fetches video metadata from YouTube using the YouTube Data API  
- Stores and manages video data in a structured SQLite database  
- Provides a user interface for labeling videos with themes  
- Allows assigning relevance labels to videos per theme  
- Supports querying labeled and unlabeled data  
- Prevents duplicate entries using database constraints  
- Enables exporting datasets in CSV/XLSX formats for machine learning use  

## Technologies Used
- Python  
- Pandas (data manipulation and export)  
- Streamlit (user interface)  
- SQLite (data storage)  
- YouTube Data API (data collection)  

## How It Works
The system follows a simple data pipeline:

1. **Data Collection**  
   - Fetches video metadata from the YouTube Data API based on a user-defined query  

2. **Data Processing**  
   - Extracts relevant fields (video ID, title, thumbnail) and formats them for storage  

3. **Data Storage**  
   - Stores videos in a SQLite database  
   - Prevents duplicate entries using a `(videoId, theme)` uniqueness constraint  

4. **Data Annotation**  
   - Users assign themes and label videos as relevant or irrelevant through the UI  

5. **Data Export**  
   - Labeled data can be exported as CSV or XLSX for machine learning workflows
   - Supports assigning themes during data collection without requiring relevance labels  
  
## Setup

1. Clone the repository:
 ```bash
   git clone https://github.com/wormzz11/YouTube-Data-Collection-Labeling-System
   cd YouTube-Data-Collection-Labeling-System
   ```
   
3. Create and activate a virtual environment:
 ```bash
   python -m venv venv
   venv\Scripts\Activate.ps1
  ```
5. Install dependencies:
 ```bash
   pip install -e .
  ```
7. Configure your YouTube API key:
 ```python
  Create a file `config/settings.py` and add: 
  YOUTUBE_API_KEY = "<your_api_key_here>"
```
8. Run the application:
 ```bash
   python -m streamlit run app/app.py
 ```
     
