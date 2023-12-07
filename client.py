import numpy as np
import matplotlib.pyplot as plt
from encode_decode import *
import socket

class Client:
    def __init__(self):
        self.connection_socket = socket.socket()
        self.host = ''
        self.port = 0000
        self.conn = ''
        self.address = ''

        self.text_message = ''
        self.caesar = ''
        self.ascii_message = ''
        self.binary_message = ''
        self.plot_message = ''
        self.encoded_message = ''

        self.is_host = False

    def connect(self):
        self.connection_socket.connect((self.host, self.port))

    def create_connection(self):
        self.connection_socket.bind((self.host, self.port))
        self.connection_socket.listen(2)
        self.conn, self.address = self.connection_socket.accept()

    def set_message_to_send(self, message):
        self.text_message = message
        self.caesar = caesar(self.text_message, 5, 1)
        self.ascii_message = asciiEncode(self.caesar)
        self.binary_message = binaryEncode(self.ascii_message)
        self.plot_message = self.binary_message.copy()
        self.encoded_message = Encode6B8B(self.plot_message)
        self.encoded_message = np.array(self.encoded_message)
        #contatenate the message into one array
        self.encoded_message = np.concatenate(self.encoded_message).astype(str).tolist()
        #transform the list into a string
        self.encoded_message = ''.join(self.encoded_message)
            

    def send_message(self):
        self.plot_graph(self.plot_message, 'Enviado')
        if self.is_host:
            self.conn.send(self.encoded_message.encode())
        else:
            self.connection_socket.send(self.encoded_message.encode())

    def receive_message(self):
        if self.is_host:
            e6b8b_code = self.conn.recv(1024).decode()
        else:
            e6b8b_code = self.connection_socket.recv(1024).decode()

        print(e6b8b_code)
        aux_list = list(e6b8b_code)
        #concatenate the message into one array for plotting
        bit_array = np.array(aux_list)
        print(bit_array)
        # bit_array = np.concatenate(bit_array).astype(int)

        if plt.fignum_exists(True):
            plt.close()

        self.plot_graph(bit_array, 'Recebido')

        aux = []
        for i in range(0,len(aux_list),8):
            chunk = aux_list[i:i+8]
            aux.append(chunk)

        self.encoded_message = aux
        self.binary_message = Decode6B8B(self.encoded_message)
        self.ascii_message = binaryDecode(self.binary_message)
        self.caesar = asciiDecode(self.ascii_message)
        self.text_message = caesar(self.caesar, 5, 0)

    def plot_graph(self, message, title):
        if plt.fignum_exists(True):
            plt.close()
        plt.rcParams["figure.autolayout"] = True
        plt.title(title)
        index = list(np.arange(len(message)))
        plt.hlines(y = 0, xmin = 0, xmax = len(message), linewidth = 1)
        plt.bar(index, message)
        plt.show()
