import socket
import threading
from collections import defaultdict
import time


class SimpleFirewall:
    def __init__(self):
        self.blocked_ips = set()
        self.connection_counts = defaultdict(int)
        self.last_connection_time = defaultdict(float)
        self.rate_limit = 10  # connections per second
        self.blacklist_threshold = 100  # max failed attempts

    def is_blocked(self, ip):
        return ip in self.blocked_ips

    def check_rate_limit(self, ip):
        current_time = time.time()
        if current_time - self.last_connection_time[ip] >= 1:
            self.connection_counts[ip] = 0
            self.last_connection_time[ip] = current_time

        self.connection_counts[ip] += 1
        return self.connection_counts[ip] <= self.rate_limit

    def start_firewall(self, port=8000):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('0.0.0.0', port))
        server_socket.listen(5)
        print(f"Firewall started on port {port}")

        while True:
            try:
                client_socket, address = server_socket.accept()
                client_ip = address[0]

                if self.is_blocked(client_ip):
                    client_socket.close()
                    continue

                if not self.check_rate_limit(client_ip):
                    print(f"Rate limit exceeded for {client_ip}")
                    self.blocked_ips.add(client_ip)
                    client_socket.close()
                    continue

                # Handle legitimate connection
                thread = threading.Thread(target=self.handle_connection,
                                          args=(client_socket, client_ip))
                thread.start()

            except Exception as e:
                print(f"Error: {e}")

    def handle_connection(self, client_socket, client_ip):
        try:
            # Add your connection handling logic here
            data = client_socket.recv(1024)
            # Process the data as needed
            client_socket.send(b"Connection accepted")
        except Exception as e:
            print(f"Connection error from {client_ip}: {e}")
            self.connection_counts[client_ip] += 1
            if self.connection_counts[client_ip] >= self.blacklist_threshold:
                self.blocked_ips.add(client_ip)
        finally:
            client_socket.close()


if __name__ == "__main__":
    firewall = SimpleFirewall()
    firewall.start_firewall()
