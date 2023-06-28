import cv2
import zbar
import pyttsx3

# initialize the camera
cap = cv2.VideoCapture(0)

# create a Scanner object
scanner = zbar.Scanner()

# initialize the text-to-speech engine
engine = pyttsx3.init()

while True:
    # capture a frame from the camera
    ret, frame = cap.read()

    # convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect barcodes in the grayscale frame
    results = scanner.scan(gray)

    # loop over the detected barcodes
    for result in results:
        # extract the barcode data and type from the result
        data = result.data.decode("utf-8")
        barcode_type = result.type

        # speak the barcode data
        engine.say(data)
        engine.runAndWait()

        # output the barcode data and type to the terminal
        print("Barcode data: {}".format(data))
        print("Barcode type: {}".format(barcode_type))

    # exit the program if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the camera and close all windows
cap.release()
cv2.destroyAllWindows()

