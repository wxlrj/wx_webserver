from socket import *
sPort = 80
hySocket = socket(AF_INET, SOCK_STREAM)
hySocket.bind(('',sPort))
hySocket.listen(1)
print ('ready OK')
while True:
  ljSocket, addr = hySocket.accept()
  qqbw = ljSocket.recv(1024)
  qqbws = qqbw.decode()
  urlEnd = qqbws.index('HTTP')
  url = qqbws[4:urlEnd]
  if (len(url) <= 2):
    url = 'index.html'
  wj = 'D:\\www\\' + url
  fhwjl = open(wj)
  fhstr = ''.join(fhwjl)
  fhsb = "HTTP/1/1 200 OK<cr><lf>\
          Connection:close<cr><lf>\
          Server: my<cr><lf>\
          Connection-Type: text/html"
  xystr = fhsb + fhstr
  xyz = xystr.encode()
  ljSocket.send(xyz)
  ljSocket.close()
  ss = input("quit?(y/n)").lower()
  if (ss == 'y'):
    break
hySocket.close()
