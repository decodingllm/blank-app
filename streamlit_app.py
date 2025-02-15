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

def get_transcript_with_params(video_id, api_key, rapidapi_host, platform):
    conn = http.client.HTTPSConnection("youtube-video-summarizer-gpt-ai.p.rapidapi.com") # API endpoint

    headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': rapidapi_host
    }

    # Construct the URL with dynamic parameters
    params = {
        'video_id': video_id,
        'platform': platform
    }
    #params.update(platform)  # Adding platform selection
    url = "/api/v1/get-transcript-v2?" + urllib.parse.urlencode(params)  # encoding parameters

    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")

#transcript_data = get_transcript_with_params(video_id, api_key, rapidapi_host, platform)
#data = json.loads(transcript_data)

# Call the function with additional parameters as needed
# API returns the JSON data which is stored in the 'data' variable

#apiResponse = json.loads(get_transcript_with_params(video_id, api_key, rapidapi_host, platform))
#transcript_text = apiResponse["data"]["transcripts"]["en_auto"]["custom"][0]["text"]

apiResponse=[]

# Add a button to trigger the transcript extraction
if st.button("Get Transcript"):
    apiResponse = json.loads(get_transcript_with_params(video_id, api_key, rapidapi_host, platform))

# Extract the transcript text from the JSON data
from utils import extract_transcript_text  # Import the function from utils.py
all_texts = extract_transcript_text(apiResponse)

# Print the result
for text in all_texts:
    st.write(text)

# Display the transcript data
#st.text_area("Transcript:", transcript_text, height=400)
