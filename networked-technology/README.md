# Networked Technology 	:man_technologist:

## TCP 
![image1](https://linube.com/blog/wp-content/uploads/protocolo-tcp.png)

Transport Control Protocol or TCP. 

- Built on top of IP (Internet protocol)
- Assumes IP might lose some data stores and retransmits data if it 
seems to be lost
- Handles "the flow control" using a transmit window
- Provides a nice reliable <a href="https://sourceforge.net/projects/tcppipe/#:~:text=TCP-Pipe%20%28or%20Remote%20Pipe%29%20is%20a%20small%20set,server%2C%20which%20pipes%20out%20the%20stream%20to%20stdout.">pipe</a>


## TCP Connections/Sockets

An application can communicate with a remote process by exchanging data with TCP/IP by knowing the combination of protocol type, IP address, and port number. This combination is often known as a socket address. It is the network-facing access handle to the network socket. The remote process establishes a network socket in its own instance of the protocol stack, and uses the networking API to connect to the application, presenting its own socket address for use by the application. Source: <a href="https://en.wikipedia.org/wiki/Network_socket">Wikipedia</a>

### Sockets in Python

Python has built-in support for TCP Sockets

```
import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('SOME_URL'), 'PORT')
```