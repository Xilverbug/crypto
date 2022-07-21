import base64

hex_str = "4261736531362c204261736533322c20616e642042617365363420616c676f726974686d73"

str = bytes.fromhex(hex_str)
b64_str = base64.b64encode(str)
print(b64_str)