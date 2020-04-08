import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mmysock.connect(('data.pr4e.org', 80))

## str.encode()
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()  ## bytes, encode() goes from unicode to bytes
mysock.send(cmd)  # send bytes


while True:
	data = mysock.recv(512)  ## Bytes
	if (len(data) < 1 ):
		break
	#bytes.decode()
	mystring = data.decode()  ## unicode,  decode() goes fromm bytes to unicode
	print(mystring)




print(ord('')) # '' to ASCII
print(chr(number)) # ASCII number to text