import streamlit as st
import http.client
import urllib.parse
import json
import os

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
