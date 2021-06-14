import socket
REMOTE_SERVER = "one.one.one.one"
def is_connected(hostname):
  try:
    host = socket.gethostbyname(hostname)
    s = socket.create_connection((host, 80), 2)
    s.close()
    print("True")
  except:
     pass
     print("False")
is_connected(REMOTE_SERVER)
