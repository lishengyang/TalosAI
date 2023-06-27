import cv2
from pix2struct import Pix2StructOCR

# Load the image
image = cv2.imread('path/to/image.jpg')

# Define rules to extract English words
rules = [
    {'type': 'word', 'lang': 'eng'}
]

# Initialize a Pix2StructOCR object and extract the English words
ocr = Pix2StructOCR()
output = ocr.ocr_image(image, rules)

# Store the words in a list
words = []
for item in output:
    words.append(item["text"])

# Print the words
print(words)
