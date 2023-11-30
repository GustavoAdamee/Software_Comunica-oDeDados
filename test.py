import numpy as np
import matplotlib.pyplot as plt
from encode_decode import *

# def plot(data1, data2, data3, msg, title1, title2,title3):
#     if plt.fignum_exists(True):
#         plt.close()

#     #setando o layout para 3 subplots
#     plt.rcParams["figure.autolayout"] = True
#     fig, axs = plt.subplots(3)
#     # titulo geral
#     fig.suptitle(msg)

#     #printando os titulo o grafico de cada dataset
#     index = list(np.arange(len(data1)))
#     axs[0].set_title(title1)
#     axs[0].plot(index, data1)
    
#     index = list(np.arange(len(data2)))
#     axs[1].set_title(title2)
#     axs[1].bar(index, data2)
#     axs[1].hlines(y = 0, xmin = 0, xmax = len(data3), linewidth = 1)
    
#     index = list(np.arange(len(data3)))
#     axs[2].set_title(title3)
#     axs[2].bar(index, data3)
#     axs[2].hlines(y = 0, xmin = 0, xmax = len(data3), linewidth = 1)

    
#     plt.show()


# from Crypto.Cipher import AES
# obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
# message = "The answer is no"
# ciphertext = obj.encrypt(message)
# ciphertext
# obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
# obj2.decrypt(ciphertext)


# never use ECB in strong systems obviously

# ...
text = input('Digite a mensagem\n')

text = caesar(text, 5, 1)
print('CAESER encode:')
print(text)

text_to_ascii = asciiEncode(text)
print('ASCII encode:')
print(text_to_ascii)

ascii_to_binary = binaryEncode(text_to_ascii)
print('Binary Encode:')
print(ascii_to_binary)

binary_to_HDB3 = HDB3Encode(ascii_to_binary)
print('HDB3 encode: ')
print(binary_to_HDB3[0])
print(ascii_to_binary)

print(ascii_to_binary)
# plot(text_to_ascii, ascii_to_binary, binary_to_HDB3[1], 'Encode', 'ASCII', 'Binary', 'HDB3')

HDB3_to_binary = HDB3Decode(binary_to_HDB3[0])
print('HDB3 decode:')
print(HDB3_to_binary)

binary_to_ascii = binaryDecode(HDB3_to_binary)
print('Binary decode:')
print(binary_to_ascii)

ascii_to_text = asciiDecode(binary_to_ascii)
print('ASCII decode:')
print(ascii_to_text)

print('CAESER decode:')
cesar = caesar(ascii_to_text, 5, 0)
print(cesar)