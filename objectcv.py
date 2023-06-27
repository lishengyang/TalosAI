import cv2

# Load the pre-trained model
net = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'model.caffemodel')

# Load the image
image = cv2.imread('image.jpg')

# Resize the image to fit the input size of the model
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)

# Set the input of the model
net.setInput(blob)

# Run the model inference
detections = net.forward()

# Loop over the detections and draw bounding boxes around the detected objects
for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]
    if confidence > 0.5:
        box = detections[0, 0, i, 3:7] * np.array([image.shape[1], image.shape[0], image.shape[1], image.shape[0]])
        (startX, startY, endX, endY) = box.astype('int')
        cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)

# Show the image with the detected objects
cv2.imshow('Image', image)
cv2.waitKey(0)
