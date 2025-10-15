import base64
CH_hex= "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
CH_bytes = bytes.fromhex(CH_hex)
CH_base = base64.b64encode(CH_bytes).decode()
print(CH_base)





