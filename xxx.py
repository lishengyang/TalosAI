import sys
import subprocess

# Get YouTube video URL from command-line argument
url = sys.argv[1]

# Download English subtitles in SRT format using youtube-dl
subprocess.run(["youtube-dl", "--write-sub", "--sub-lang", "en", "--convert-subs", "srt", "--skip-download", "--output", "%(title)s.%(ext)s", url])

# Convert SRT file to plain text using srt2txt
# Read SRT file and extract English subtitles
with open("video_title.en.srt", "r") as srt_file:
    lines = srt_file.readlines()
    subtitles = [line.strip() for line in lines if line.strip().isdigit() == False]

# Save English subtitles to plain text file
with open("video_title.en.txt", "w") as txt_file:
    txt_file.write("\n".join(subtitles))

print("Subtitles downloaded and converted to plain text!")

