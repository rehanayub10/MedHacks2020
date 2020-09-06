import base64

with open('./audio/happy-sample.wav', 'rb') as fp:
    data = fp.read()

_byte = base64.b64encode(data)

message = _byte.decode('utf-8')

with open('./audio/happy-sample.txt', 'w+') as fp:
    fp.write(message)

print(message)