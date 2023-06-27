import sys
import pyocr
from PIL import Image

# check if image file path was provided as argument
if len(sys.argv) < 2:
    print("Please provide an image file path as an argument")
    sys.exit()

# get image file path from command line argument
image_file_path = sys.argv[1]

# initialize OCR tool
ocr_tool = pyocr.get_available_tools()[0]

# set OCR engine configuration parameters
ocr_tool.set_variable('tessedit_char_blacklist', '')

# set OCR page segmentation mode
ocr_tool.set_page_segmentation_mode(
    pyocr.tesseract.PageSegMode.AUTO
)

# load the image to be processed
image = Image.open(image_file_path)

# perform OCR on the image
ocr_result = ocr_tool.image_to_string(
   image,
   lang='eng+num',
   builder=pyocr.builders.TextBuilder()
)

# print the OCR result
print(ocr_result)
