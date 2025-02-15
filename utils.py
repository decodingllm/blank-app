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
