import asyncio
import http3

async def main():
    async with http3.AsyncClient() as client:
        response = await client.get('https://example.com')
        print(f"Response status code: {response.status_code}")
        print(f"Response text: {response.text}")

if __name__ == '__main__':
    asyncio.run(main())
