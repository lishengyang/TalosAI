import re
import requests
from xml.etree import ElementTree as ET

def download_auto_generated_english_subtitles(video_link):
    # Extract video ID from the video link
    video_id = re.findall(r'(?<=v=)[^&#]+', video_link)
    
    if not video_id:
        raise ValueError('Invalid YouTube video link')
    
    # Construct the subtitle URL
    subtitle_url = "https://www.youtube.com/api/timedtext?lang=en&v=" + video_id[0] + "&fmt=srv3"
    
    # Send a GET request to fetch the data
    response = requests.get(subtitle_url)
    
    if response.status_code != 200:
        raise ValueError('Could not fetch subtitles')
    
    # Parse the XML response to extract the subtitle text
    root = ET.fromstring(response.text)
    subtitle_text = ""
    
    for child in root:
        subtitle_text += child.text + " "
    
    return subtitle_text

#To use this function, pass a valid YouTube video link to it:


video_link = "https://www.youtube.com/watch?v=Hc20D8FUdgA"
subtitle_text = download_auto_generated_english_subtitles(video_link)
print(subtitle_text)

