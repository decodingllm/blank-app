import streamlit as st
import http.client
import urllib.parse
import json
import os

from utils import extract_transcript_text, get_transcript_with_params, summarize_text  # Import the functions from utils.py

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
from config import rapidapi_host
platform = "youtube"

#transcript_data = get_transcript_with_params(video_id, api_key, rapidapi_host, platform)
#data = json.loads(transcript_data)

# Call the function with additional parameters as needed
# API returns the JSON data which is stored in the 'data' variable

# Add a button to trigger the transcript extraction
apiResponse=[]
if 'apiResponse' not in st.session_state:
    st.session_state.apiResponse = []

if 'transcript_text' not in st.session_state:
    st.session_state.transcript_text = []

if st.button("Get Transcript"):
    st.session_state.apiResponse = json.loads(get_transcript_with_params(video_id, api_key, rapidapi_host, platform))
    st.session_state.transcript_text = extract_transcript_text(st.session_state.apiResponse)

    for text in st.session_state.transcript_text:
        st.write(text)
    #apiResponse = json.loads(get_transcript_with_params(video_id, api_key, rapidapi_host, platform))


if st.button("Summarize", disabled=not st.session_state.transcript_text):
    summary = summarize_text(" ".join(st.session_state.transcript_text))
    st.write(summary)

# Extract the transcript text from the JSON data
all_texts = extract_transcript_text(apiResponse)

# Print the result
for text in all_texts:
    st.write(text)

# Display the transcript data
#st.text_area("Transcript:", transcript_text, height=400)

st.title("YouTube Transcript & Summary")

# Add an input bar to take string input from the user
baseURL = st.text_input("Enter the base URL:")

# Split the URL after the '=' sign to get the video_Id
video_id = ""

if '=' in baseURL:
    parts = baseURL.split('=')
    video_id = parts[1] 
    st.write(f"Extracted Video ID: {video_id}")
else:
    st.write(f"Invalid YouTube URL format!!")

#transcript_data = get_transcript_with_params(video_id, api_key, rapidapi_host, platform)
#data = json.loads(transcript_data)

# Call the function with additional parameters as needed
# API returns the JSON data which is stored in the 'data' variable

# Add a button to trigger the transcript extraction
apiResponse=[]
text=""
if 'apiResponse' not in st.session_state:
    st.session_state.apiResponse = []

if 'transcript_text' not in st.session_state:
    st.session_state.transcript_text = []

if st.button("Get Transcript"):
    st.session_state.apiResponse = json.loads(get_transcript_with_params(video_id, api_key, rapidapi_host, platform))
    st.session_state.transcript_text = extract_transcript_text(st.session_state.apiResponse)

    for text in st.session_state.transcript_text:
        st.write(text)
    #apiResponse = json.loads(get_transcript_with_params(video_id, api_key, rapidapi_host, platform))


if st.button("Summarize", disabled=not st.session_state.transcript_text):
    summary = summarize_text(text)
    st.write(summary)

# Extract the transcript text from the JSON data
#all_texts = extract_transcript_text(apiResponse)

# Print the result
#for text in all_texts:
#    st.write(text)

# Display the transcript data
#st.text_area("Transcript:", transcript_text, height=400)


# Run FastAPI app
import subprocess
subprocess.Popen(["uvicorn", "api:app", "--reload"])