import http3
import asyncio
import subprocess

async def download_image():
    async with http3.AsyncClient() as client:
        response = await client.get('https://example.com/image.jpg')
        with open('image.jpg', 'wb') as f:
            f.write(response.content)
        output = subprocess.check_output(['ls', '-a', 'image.jpg']).decode('utf-8')
        file_size = output.split()[4]
        print(f"Downloaded image size: {file_size} bytes")

if __name__ == '__main__':
    asyncio.run(download_image())
