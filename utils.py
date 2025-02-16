import streamlit as st
import http.client
import urllib.parse
import json
import os


# Function to get the transcript data from the API as JSON
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


# Function to extract required text chunks from the JSON data
# JSON we have got from get_transcript_with_params
def extract_transcript_text(apiResponse):
    transcript_text = []
    if isinstance(apiResponse, dict):
        for key, value in apiResponse.items():
            if key == "text":
                transcript_text.append(value)
            else:
                transcript_text.extend(extract_transcript_text(value))
    elif isinstance(apiResponse, list):
        for item in apiResponse:
            transcript_text.extend(extract_transcript_text(item))
    return transcript_text


def summarize_text(texts):
    # Placeholder function for summarizing text
    conn = http.client.HTTPSConnection("gpt-summarization.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "2bd75d2069msh7d63312ea77e344p1786cbjsn875221b51434",
        'x-rapidapi-host': "gpt-summarization.p.rapidapi.com",
        'Content-Type': "application/json"
    }

    conn.request("POST", "/summarize", texts, headers)

    res = conn.getresponse()
    summary = res.read().decode("utf-8")
    #st.write(summary)
    return summary
