import yt_dlp

# List of video URLs
video_urls = [
    "https://www.youtube.com/watch?v=V9YDDpo9LWg",
    "https://www.youtube.com/watch?v=JBoc3w5EKfI",
    "https://www.youtube.com/watch?v=aWV7UUMddCU",
    "https://www.youtube.com/watch?v=f6wqlpG9rd0",
    "https://www.youtube.com/watch?v=GNVTuLHdeSo",
    "https://www.youtube.com/watch?v=SWtmkjd45so",
    "https://www.youtube.com/watch?v=RzI6Ar5mu2Q",
    "https://www.youtube.com/watch?v=aulLej6Z6W8",
    "https://www.youtube.com/watch?v=7pN6ydLE4EQ",
    "https://www.youtube.com/watch?v=fEEelCgBkWA",
    "https://www.youtube.com/watch?v=ckZQbQwM3oU",
    "https://www.youtube.com/watch?v=E8Wgwg3F4X0",
    "https://www.youtube.com/watch?v=rvIPH4ccfpI",
    "https://www.youtube.com/watch?v=F6iqlW6ovZc",
    "https://www.youtube.com/watch?v=9qjk-Sq415s&list=PL5B0D2D5B4BFE92C1&index=6",
    "https://www.youtube.com/watch?v=DI25kGJis0w",
    "https://www.youtube.com/watch?v=rrLhFZG6iQY",
    "https://www.youtube.com/watch?v=RKOZbT0ftL4&t=1s",
    "https://www.youtube.com/watch?v=N7TBbWHB01E",
    "https://www.youtube.com/watch?v=1YqVEVbXQ1c"
]

# Directory to save videos
download_dir = "./"

# Create download directory if it doesn't exist
import os
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Download videos
for url in video_urls:
    ydl_opts = {
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'format': 'mp4',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print(url)
