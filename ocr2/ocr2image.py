import io
import sys
import pyocr
# import libraries
import pytesseract
from PIL import Image

# initialize OCR tool
ocr_tool = pyocr.get_available_tools()[0]

# set OCR engine configuration parameters
ocr_tool.set_variable('tessedit_char_blacklist', '')

# set OCR page segmentation mode
ocr_tool.set_page_segmentation_mode(
    pyocr.tesseract.PageSegMode.AUTO
)

# load the image to be processed
image = Image.open('image.png')

# perform OCR on the image
ocr_result = ocr_tool.image_to_string(
   image,
   lang='eng+num',
   builder=pyocr.builders.TextBuilder()
)

# print the OCR result
print(ocr_result)
