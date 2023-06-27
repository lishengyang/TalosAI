from PIL import Image
import random
import http3
import asyncio
import subprocess

def create_random_image():
    img = Image.new('RGB', (500, 500), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    img.save('image.jpg')

async def download_image():
    async with http3.AsyncClient() as client:
        response = await client.get('https://example.com/image.jpg')
        with open('image.jpg', 'wb') as f:
            f.write(response.content)
        output = subprocess.check_output(['ls', '-l', 'image.jpg']).decode('utf-8')
        file_size = output.split()[4]
        print(f"Downloaded image size: {file_size} bytes")

if __name__ == '__main__':
    create_random_image()
    asyncio.run(download_image())
