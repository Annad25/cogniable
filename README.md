# Therapist and Child Detection and Tracking

## Project Overview
This project aims to build a system that detects and tracks children and therapists in therapy sessions, assigning unique IDs to individuals and maintaining these IDs throughout the video, even after occlusion or re-entry. The goal is to identify and analyze the behavior and interactions of children with Autism Spectrum Disorder (ASD) and therapists to provide insights into their engagement and behavior patterns.

## Problem Statement
The system should:
- Detect children and therapists in videos.
- Assign unique IDs to each detected person.
- Track individuals even after they exit and re-enter the frame.
- Handle occlusions and reassign the correct ID upon reappearance.

## Prerequisites
ultralytics
fiftyone
opencv-python-headless
matplotlib
yt-dlp


## Setup and Installation

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-directory>



## Installation
1. Clone the repository:
```
git clone https://github.com/your-username/person-tracking.git
```
2. Navigate to the project directory:
```
cd person-tracking
```
3. Install the required dependencies:
```
pip install -r requirements.txt
```

## Download Videos 

 The videos used for tracking need to be downloaded first. 
 Run the videos.py script to download the videos:

python video_downloader.py

###  Run the tracking code:

 use the person_tracking.py script to perform detection and tracking:

python tracking.py

## Usage



## Results

The trained YOLOv8 models achieved the following mean average precisions (mAP) on the test_videos test set:
- yolov8n: `0.61287`



### Video Downloader

The videos.py script downloads videos from YouTube using the yt-dlp library. It saves the videos in the specified directory for further processing.

### Detection & Tracking

The person_tracking.py script utilizes the YOLOv8 model to detect persons (children and therapists) in the video and track their movement. The script assigns unique IDs to detected individuals and keeps track of these IDs throughout the video.

YOLO Model: The model used is YOLOv8, a state-of-the-art object detection model.
Tracking Logic: The code tracks detected persons by assigning IDs and keeps track of them even after occlusions or re-entries into the frame.

### Expected Output

The output is a video (output.avi) showing the bounding boxes around detected individuals along with their unique IDs.