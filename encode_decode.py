import socket
import numpy as np

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
    array = np.array(array)
    #concatenate the array into a string
    array = np.concatenate(array)
    print(array)
    #printar grafico aqui
    string_ints = [str(int) for int in array]
    string_ints = ''.join(string_ints)
    values = []
    # splits the string into an array containing substrings with the fixed length of (size of 1 byte)
    ascii_array =  [string_ints[i:i+8] for i in range(0, len(string_ints), 8)] 
    for i in ascii_array:
        values.append(int(i,2))
    return values

def aply_pre_def_table(chunk):
    chunk_string = ''.join(str(e) for e in chunk)
    #disparity -6
    if chunk_string == '000000':
        chunk_output_string = '01011001'
    #disparity +6
    elif chunk_string == '111111':
        chunk_output_string = '01100110'
    #disparity -4
    elif chunk_string == '000001':
        chunk_output_string = '01110001'
    elif chunk_string == '000010':
        chunk_output_string = '01110010'
    elif chunk_string == '000100':
        chunk_output_string = '01100101'
    elif chunk_string == '001000':
        chunk_output_string = '01101001'
    elif chunk_string == '010000':
        chunk_output_string = '01010011'
    elif chunk_string == '100000':
        chunk_output_string = '01100011'
    #disparity +4
    elif chunk_string == '111110':
        chunk_output_string = '01001110'
    elif chunk_string == '111101':
        chunk_output_string = '01001101'
    elif chunk_string == '111011':
        chunk_output_string = '01011010'
    elif chunk_string == '110111':
        chunk_output_string = '01010110'
    elif chunk_string == '101111':
        chunk_output_string = '01101100'
    elif chunk_string == '011111':
        chunk_output_string = '01011100'
    #disparity -2
    elif chunk_string == '110000':
        chunk_output_string = '01110100'
    #disparity +2
    elif chunk_string == '001111':
        chunk_output_string = '01001011'
    #control
    elif chunk_string == '000111':
        chunk_output_string = '01000111'
    elif chunk_string == '010101':
        chunk_output_string = '01010101'
    elif chunk_string == '111000':
        chunk_output_string = '01111000'
    elif chunk_string == '101010':
        chunk_output_string = '01101010'
    else:
        return False 
    #transform the chunk into a list
    chunk_output_list = list(chunk_output_string)
    #transform the list into a list of ints
    chunk_output_list = [int(i) for i in chunk_output_list]
    return chunk_output_list
    
def Encode6B8B(message):
    # divide the message in 6 bits chunks
    chunk_list = []
    for i in range(0,len(message),6):
        chunk = message[i:i+6]
        chunk_list.append(chunk)
    # if chunk is less than 6 bits, add 0s to the left and encode it
    for chunk in chunk_list:
        if len(chunk) != 6:
            zeros_to_add = 6 - len(chunk)
            for i in range(zeros_to_add):
                chunk.insert(0,0)
    # encode each chunk
    final_chunk_list = []
    for chunk in chunk_list:
        processed_chunk = aply_pre_def_table(chunk)
        if processed_chunk == False:
            #get the amount of zeros and ones in the chunk
            zeros = chunk.count(0)
            ones = chunk.count(1)
            disparity = ones - zeros
            if disparity == 0:
                chunk.insert(0,0)
                chunk.insert(0,1)
            elif disparity == 2: 
                chunk.insert(0,0)
                chunk.insert(0,0)
            elif disparity == -2:
                chunk.insert(0,1)
                chunk.insert(0,1)
            final_chunk_list.append(chunk)
        else:
            final_chunk_list.append(processed_chunk)
    return final_chunk_list

def aply_decode_table(chunk):
    chunk_string = ''.join(str(e) for e in chunk)
    #disparity -6
    if chunk_string == '01011001':
        chunk_output_string = '000000'
    #disparity +6
    elif chunk_string == '01100110':
        chunk_output_string = '111111'
    #disparity -4
    elif chunk_string == '01110001':
        chunk_output_string = '000001'
    elif chunk_string == '01110010':
        chunk_output_string = '000010'
    elif chunk_string == '01100101':
        chunk_output_string = '000100'
    elif chunk_string == '01101001':
        chunk_output_string = '001000'
    elif chunk_string == '01010011':
        chunk_output_string = '010000'
    elif chunk_string == '01100011':
        chunk_output_string = '100000'
    #disparity +4
    elif chunk_string == '01001110':
        chunk_output_string = '111110'
    elif chunk_string == '01001101':
        chunk_output_string = '111101'
    elif chunk_string == '01011010':
        chunk_output_string = '111011'
    elif chunk_string == '01010110':
        chunk_output_string = '110111'
    elif chunk_string == '01101100':
        chunk_output_string = '101111'
    elif chunk_string == '01011100':
        chunk_output_string = '011111'
    #disparity -2
    elif chunk_string == '01110100':
        chunk_output_string = '110000'
    #disparity +2
    elif chunk_string == '01001011':
        chunk_output_string = '001111'
    #control
    elif chunk_string == '01000111':
        chunk_output_string = '000111'
    elif chunk_string == '01010101':
        chunk_output_string = '010101'
    elif chunk_string == '01111000':
        chunk_output_string = '111000'
    elif chunk_string == '01101010':
        chunk_output_string = '101010'
    #transform the chunk into a list
    chunk_output_list = list(chunk_output_string)
    #transform the list into a list of ints
    chunk_output_list = [int(i) for i in chunk_output_list]
    return chunk_output_list

#TODO implement the 6b8b decoding
def Decode6B8B(message):
    decoded_message = []
    for chunk in message:
        if chunk[0] == 0 and chunk[1] == 1:
            decoded_message.append(aply_decode_table(chunk))
        else:
            chunk.pop(0)
            chunk.pop(0)
            decoded_message.append(chunk)
    return decoded_message

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