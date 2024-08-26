import socket
from time import sleep



def HZmessage(messages):
    host = '192.168.1.10'
    port = 1234
    # 创建一个UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = (host, port)

    try:
        for message in messages:
            # 发送数据
            message = bytes.fromhex(message)
            print(message)

            # 发送数据
            print(f'Sending: {message}')
            sent = sock.sendto(message, server_address)
            sleep(0.1)

    finally:
        # # 接收响应
        # print('Waiting for response...')
        # data, server = sock.recvfrom(1024)
        # print(f'Received {len(data)} bytes from {server}')
        # # 打印
        # print(f'Hex data: {data.hex()}')
        print('Closing socket')
        sock.close()

def udp_client(messages=['01000001']):
    host = '192.168.1.10'
    port = 1234
    # 创建一个UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = (host, port)

    try:
        for message in messages:
            # 发送数据
            message = bytes.fromhex(message)
            print(message)

            # 发送数据
            print(f'Sending: {message}')
            sent = sock.sendto(message, server_address)
            sleep(0.1)

    finally:
        # # 接收响应
        # print('Waiting for response...')
        # data, server = sock.recvfrom(1024)
        # print(f'Received {len(data)} bytes from {server}')
        # # 打印
        # print(f'Hex data: {data.hex()}')
        print('Closing socket')
        sock.close()
if __name__ == '__main__':
    udp_client()