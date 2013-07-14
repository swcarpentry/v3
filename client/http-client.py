import sys, socket

buffer_size = 1024

HttpRequest = "GET /greeting.html HTTP/1.0\n\n"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('www.third-bit.com', 80))

sock.send(HttpRequest)

response = ''
while True:
    data = sock.recv(buffer_size)
    if not data:
        break
    response += data
sock.close()

print response
