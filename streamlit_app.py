import streamlit as st
import http.client
import urllib.parse
import json
import os

st.title("YouTube Transcript & Summary")

# Add an input bar to take string input from the user
baseURL = st.text_input("Enter the base URL:")

# Split the URL after the '=' sign to get the video_Id
video_id = ""

if '=' in baseURL:
    parts = baseURL.split('=')
    # Store the second part in the 'VID' variable
    video_id = parts[1] 
    st.write(f"Extracted Video ID: {video_id}")
else:
    st.write(f"Invalid YouTube URL format. Please provide a URL containing video_id starting with'='.'")

## required params
from config import api_key
rapidapi_host = "youtube-video-summarizer-gpt-ai.p.rapidapi.com"
platform = "youtube"

#transcript_data = get_transcript_with_params(video_id, api_key, rapidapi_host, platform)
#data = json.loads(transcript_data)

# Call the function with additional parameters as needed
# API returns the JSON data which is stored in the 'data' variable

# Add a button to trigger the transcript extraction
apiResponse=[]
if st.button("Get Transcript"):
    from utils import get_transcript_with_params  # Import the function from utils.py
    apiResponse = json.loads(get_transcript_with_params(video_id, api_key, rapidapi_host, platform))

# Extract the transcript text from the JSON data
from utils import extract_transcript_text  # Import the function from utils.py
all_texts = extract_transcript_text(apiResponse)

# Print the result
for text in all_texts:
    st.write(text)

# Display the transcript data
#st.text_area("Transcript:", transcript_text, height=400)
