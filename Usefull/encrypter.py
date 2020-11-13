from Crypto.Cipher import AES
import base64, console
console.clear()
message = input('Enter Message')
print('Message length: ' + str(len(message)))

result = '0000000000000000'
#print len(result)

msg_text = message.rjust(16)
secret_key = result # create new & store somewhere safe

cipher = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously
encoded = base64.b64encode(cipher.encrypt(msg_text))
# ...
decoded = cipher.decrypt(base64.b64decode(encoded))
print(encoded.strip())
print('Encoded length: ' + str(len(encoded.strip())))

print(decoded.strip())