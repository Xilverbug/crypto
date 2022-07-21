import base64

b64_msg = b'AQIDBAQGBwgJCgsMDQ4P/w=='

msg = base64.b64decode(b64_msg)
print(msg)