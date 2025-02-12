import socket
import json
import ssl
import logging
from datetime import datetime

# Logging setup
logging.basicConfig(level=logging.INFO)

# Server settings
HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 5000
CERT_FILE = 'path_to_server_cert.pem'  # Server SSL certificate
KEY_FILE = 'path_to_server_key.pem'    # Server private key
CA_CERT_FILE = 'path_to_ca_cert.pem'   # CA certificate for verifying clients
LOG_FILE = "received_os_logs.json"

# Set up SSL context
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)
context.load_verify_locations(CA_CERT_FILE)

def save_logs(logs):
    """Save received logs to a JSON file."""
    try:
        with open(LOG_FILE, "a") as f:
            json.dump(logs, f, indent=4)
            f.write(",\n")
        logging.info("Logs saved successfully.")
    except Exception as e:
        logging.error(f"Error saving logs: {e}")

def start_server():
    """Start the secure log receiver server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        logging.info(f"Server listening on {HOST}:{PORT}")

        with context.wrap_socket(server_socket, server_side=True) as secure_socket:
            while True:
                client_socket, addr = secure_socket.accept()
                logging.info(f"Connection from {addr}")

                try:
                    data = client_socket.recv(8192).decode()
                    if data:
                        logs = json.loads(data)
                        logs["received_timestamp"] = datetime.utcnow().isoformat()  # Add timestamp
                        save_logs(logs)
                except Exception as e:
                    logging.error(f"Error processing data: {e}")
                finally:
                    client_socket.close()

if __name__ == "__main__":
    start_server()
