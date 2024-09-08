from ultralytics import YOLO
import cv2
import matplotlib 

model_path = 'yolov8n.pt'
video_path = 'Group Therapy for Autism Spectrum Disorder.mp4'
model = YOLO(model_path)

results = model.track(video_path, persist=True, stream=True, conf=0.25, task='detect')

max_track_id = 0

cap = cv2.VideoCapture(video_path)
output = cv2.VideoWriter("output-4.avi", cv2.VideoWriter_fourcc(*'MPEG'), 25, (int(cap.get(3)),int(cap.get(4))))


for result in results:
    summary = result.summary()
    filtered_detections = []
    for s in summary:
        if 'track_id' in s and 'name' in s and s['name'] == 'person':
            if s['track_id'] > max_track_id:
                max_track_id = s['track_id']
            filtered_detections.append(s)
    
    # Plot only the filtered detections
    if filtered_detections:
        tracked_frame = result.plot()  # Assuming 'person' is class 0
    else:
        tracked_frame = result.plot()  # Plot all detections if none are filtered
    output.write(tracked_frame)
    cv2.imshow('frame', tracked_frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
   

output.release()
cap.release()
cv2.destroyAllWindows()
print("Tracking video complete...")
print(f"There are {max_track_id} peoples in video")

