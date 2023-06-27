import pyocr
import pyocr.builders
from PIL import Image
import sys

tools = pyocr.get_available_tools()
tool = tools[0]

filename = sys.argv[1]
img = Image.open(filename)
text = tool.image_to_string(
    img,
    lang='eng+num',
    builder=pyocr.builders.TextBuilder()
)
print(text)
