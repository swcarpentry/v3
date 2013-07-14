import sys, socket

buffer_size = 1024     # bytes
host = ''              # empty string means 'this machine'
port = 19073           # must agree with client

# Create and bind a socket.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

# Wait for a connection request.
s.listen(True)
sock, addr = s.accept()
print 'Connected by', addr

# Receive and display a message.
data = sock.recv(buffer_size)
print 'server saw', str(data)

# Replace vowels in reply.
data = data.replace('i', 'o')
sock.send(data)

sock.close()
