import socket

def caesar(data, key, mode):
    alphabet = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'
    new_data = ''
    for c in data:
        index = alphabet.find(c)
        if index == -1:
            new_data += c
        else:
            new_index = index + key if mode == 1 else index - key
            new_index = new_index % len(alphabet)
            new_data += alphabet[new_index:new_index+1]
    return new_data

def asciiEncode(message):
    values = []
    for char in message:
        values.append(ord(char))
    return values

def asciiDecode(message):
    values = []
    for char in message:
        values.append(chr(char))
    return ''.join(values)

def binaryEncode(array):
    values = []
    bit_values = []
    
    for i in array:
        values.append(f'{i:08b}'.format(8))
    
    values = list(''.join(values))

    for bit in values:
        bit_values.append(int(bit))

    return bit_values

def binaryDecode(array):
    #printar grafico aqui
    string_ints = [str(int) for int in array]
    string_ints = ''.join(string_ints)
    values = []
    # splits the string into an array containing substrings with the fixed length of (size of 1 byte)
    ascii_array =  [string_ints[i:i+8] for i in range(0, len(string_ints), 8)] 
    for i in ascii_array:
        values.append(int(i,2))
    return values

#TODO implement here the 6b8b encoding
def Encode6B8B(message):
    
    return

def Decode6B8B(message):

    return

def encode(message):
    text_to_ceaser = caesar(message,5,1)
    ceaser_to_ascii = asciiEncode(text_to_ceaser)
    ascii_to_binary = binaryEncode(ceaser_to_ascii)
    binary_to_6b8b = Encode6B8B(ascii_to_binary)

    return binary_to_6b8b

def decode(message):
    e6b8b_to_binary = Decode6B8B(message)
    binary_to_ascii = binaryDecode(e6b8b_to_binary)
    ascii_to_ceaser = asciiDecode(binary_to_ascii)
    ceaser_to_text = caesar(ascii_to_ceaser,5,0)

    return ceaser_to_text

def get_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        try:
            # doesn't even have to be reachable
            s.connect(('10.254.254.254', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP