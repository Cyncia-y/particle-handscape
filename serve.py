#!/usr/bin/env python3
"""Local-only web server for the KINETIC gesture particle field."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import threading
import webbrowser

ROOT = Path(__file__).resolve().parent
HOST = "127.0.0.1"
START_PORT = 8787


class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        print(f"[KINETIC] {self.address_string()} - {fmt % args}")


def main():
    import os

    os.chdir(ROOT)
    server = None
    port = START_PORT
    for candidate in range(START_PORT, START_PORT + 12):
        try:
            server = ThreadingHTTPServer((HOST, candidate), Handler)
            port = candidate
            break
        except OSError:
            continue

    if server is None:
        raise SystemExit("无法启动本地服务器：8787–8798 端口均被占用。")

    url = f"http://{HOST}:{port}/"
    print()
    print("KINETIC — 手势粒子场")
    print(f"打开地址：{url}")
    print("按 Control-C 结束服务器。")
    print()
    threading.Timer(0.7, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
        print("\n服务器已关闭。")


if __name__ == "__main__":
    main()
