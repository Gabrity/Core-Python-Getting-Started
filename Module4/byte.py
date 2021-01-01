# byte is datatype for sequence of bytes
byte = b'data'
print(byte[2])

# to convert byte => str is encode
# to convert str => byte is decode
string = 'ááé3őpűúő'
data = string.encode('utf8')
print(string)
print(data)
new_string = data.decode('utf8')
print(new_string)

#  byte is important since http responses are in the format of byte streams 