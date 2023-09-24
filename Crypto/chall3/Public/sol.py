from hashlib import md5
def encrypt(plaintext, key):
    key = md5(key).digest()
    msg = plaintext + b'|' + key
    # print(msg)
    encrypted = b'K'
    for i in range(len(msg)):
        encrypted += bytes([(msg[i] + key[i%len(key)]  + encrypted[i]) & 0xff])
    return encrypted.hex()



flag = b""
key =b''
ciphertext = "4b851cc4cdd1c7a3b7a3d83095a46a320e6b21e9e5afab7b8869d930c9cd981a0523a037faca8425f9a921c6ebca8f7087f8aab5bc53fe9cd5acfa9e"
ct_bytes = bytes.fromhex(ciphertext)
print(ct_bytes)
key = b'\xefJg\x8e\x9c\x82h\xa4y\xfb)6\x95^S{'
# print(len(key))

#msg[42] = b'|'


encrypted=b'K'
for i in range(59):
    for x in range(256):
        tmp = bytes([(x + key[i%len(key)]  + encrypted[i]) & 0xff])
        if tmp == bytes([ct_bytes[i+1]]):
            encrypted += tmp
            flag += bytes([x])
        
print(flag)
# print(key)
        


