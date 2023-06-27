import argparse
import os
import sys

from quic.client import QuicClient
from quic.server import QuicServer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["client", "server"], required=True)
    parser.add_argument("--host", type=str, default="localhost")
    parser.add_argument("--port", type=int, default=8080)
    args = parser.parse_args()

    if args.mode == "client":
        client = QuicClient(args.host, args.port)
        client.connect()
        client.send("Hello, world!")
        client.close()
    elif args.mode == "server":
        server = QuicServer(args.host, args.port)
        server.listen()
        while True:
            connection = server.accept()
            connection.read()
            connection.write("Hello, world!")
            connection.close()


if __name__ == "__main__":
    main()

