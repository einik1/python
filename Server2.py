import socket
import select

def send_waiting_messages(wlist1, messages_to_send1):
    for message in messages_to_send1:
        (client_socket, data) = message
        if client_socket in wlist1:
            client_socket.send(data)
            messages_to_send1.remove(message)


server_socket = socket.socket()
server_socket.bind(("192.168.56.1", 4444))
server_socket.listen(5)
open_client_sockets = []
messages_to_send = []

print 'server is running!!'
while True:
    rlist, wlist, xlist = select.select([server_socket] + open_client_sockets, open_client_sockets, [])
    for current_socket in rlist:
        if current_socket == server_socket:
            (new_socket, address) = server_socket.accept()
            open_client_sockets.append(new_socket)
            print "new client"
        else:
            data = current_socket.recv(1024).lower()
            if data == "":
                open_client_sockets.remove(current_socket)
                print 'connection with client is over'
            else:
                if data == "time":
                    messages_to_send.append((current_socket, 'the time is : 12:00'))
                elif data == "name":
                    messages_to_send.append((current_socket, 'my name is kobi'))
                elif data == "rand":
                    messages_to_send.append((current_socket, 'randum num'))
                else:
                     messages_to_send.append((current_socket, 'you want me to doo what?!?!?!?!'))
                'messages_to_send.append((current_socket, hello + data))'
    send_waiting_messages(wlist, messages_to_send)
