# Import modules
import pyocr
import pytesseract
#import pyocr.builders
from PIL import Image

# Set the path to Tesseract executable
pytesseract.tesseract_cmd = '/usr/bin/tesseract'
# Get the list of available tools
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

# Select the first tool (usually Tesseract)
tool = tools[0]
print("Using tool: %s" % tool.get_name())

# Get the list of available languages
langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))

# Choose a language (English by default)
lang = 'eng'
print("Using language: %s" % lang)

# Perform OCR on the image
text = tool.image_to_string(
    Image.open('image.png'),
    lang=lang,
    builder=pyocr.builders.TextBuilder()
)

# Print the OCR result
print(text)
