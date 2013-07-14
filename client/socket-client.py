import sys, socket

buffer_size = 1024     # bytes
host = '127.0.0.1'     # local machine
port = 19073           # hope nobody else is using it...
message = 'ping!'      # what to send

# AF_INET means 'Internet socket'.
# SOCK_STREAM means 'TCP'.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

# Send the message.
sock.send(message)

# Receive and display the reply.
data = sock.recv(buffer_size)
print 'client received', `data`

# Tidy up.
sock.close()
