import socket

def send_compressed_data(data, address, port):
    try:
        # Create a socket and connect to the specified address and port
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((address, port))
            
            # Send the compressed data
            s.sendall(data)
    
    except Exception as e:
        # Handle network-related errors
        print(f"Error sending data: {str(e)}")

def receive_compressed_data(address, port):
    try:
        # Create a socket and bind it to the specified address and port
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((address, port))
            s.listen()

            # Accept incoming connections
            conn, addr = s.accept()
            
            with conn:
                received_data = b""
                while True:
                    # Receive data in chunks
                    chunk = conn.recv(1024)
                    if not chunk:
                        break
                    received_data += chunk
                    
                return received_data
    
    except Exception as e:
        # Handle network-related errors
        print(f"Error receiving data: {str(e)}")
        return None
