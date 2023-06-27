import asyncio
import time
import http3

async def make_quic_request():
    async with http3.AsyncClient() as client:
        start_time = time.time()
        response = await client.get('https://example.com')
        end_time = time.time()
        return end_time - start_time

async def make_udp_request():
    reader, writer = await asyncio.open_connection('example.com', 80)
    start_time = time.time()
    writer.write(b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n')
    await writer.drain()
    data = await reader.read(1024)
    end_time = time.time()
    writer.close()
    return end_time - start_time

async def main():
    quic_latency = await make_quic_request()
    udp_latency = await make_udp_request()
    print(f"QUIC latency: {quic_latency}")
    print(f"UDP latency: {udp_latency}")

if __name__ == '__main__':
    asyncio.run(main())
