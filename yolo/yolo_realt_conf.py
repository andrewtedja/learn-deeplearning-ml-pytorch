import cv2
from ultralytics import YOLO

# Load the YOLO model
model = YOLO('best_bukpen.pt')  # Use a smaller model for faster real-time detection
#model=YOLO('YOLO/best.onnx')
# Initialize the camera (webcam)
cap = cv2.VideoCapture(0)  # Change index to 1 or higher for external webcams

# Check if the camera was successfully opened
if not cap.isOpened():
    print("Error: Cannot open webcam.")
    exit()

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break

    # Run YOLO on the frame
    results = model(frame)

    # Filter detections by confidence (e.g., above 0.5)
    confident_results = [det for det in results[0].boxes if det.conf[0] > 0.5]

    # Annotate the frame with filtered results
    annotated_frame = frame.copy()
    for det in confident_results:
        # Extract coordinates, confidence, and class
        x1, y1, x2, y2 = map(int, det.xyxy[0])  # Bounding box coordinates
        confidence = det.conf[0]  # Confidence score
        class_id = det.cls[0]  # Class ID
        label = f"{model.names[int(class_id)]} {confidence:.2f}"  # Label with confidence
        
        # Draw the bounding box and label
        cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(annotated_frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the annotated frame
    cv2.imshow('YOLO Real-Time Detection', annotated_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
