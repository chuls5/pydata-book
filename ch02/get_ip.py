"""
This module provides a utility to retrieve the local IP address of the active network interface.

It includes the `get_ip()` function, which connects to an external server (Google's public DNS)
to determine the IP address associated with the active network interface.

Example usage:
    % !python get_ip.py
"""

import socket

def get_ip():
    """
    Retrieve the local IP address of the active network interface.

    This function establishes a dummy connection to an external server (Google's public DNS server)
    to determine the local IP address associated with the active network interface.

    Returns:
        str: The local IP address if successfully retrieved, or an error message if an exception occurs.

    Example:

        >>> get_ip()
        '192.168.1.100'
    """
    try:
        # Establish a socket connection to Google's DNS server
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Dummy connection to determine the local IP
        ip = s.getsockname()[0]  # Extract the IP address
        s.close()
        return ip
    except Exception as e:
        return f"Error: {e}"  # Return error message if something goes wrong


# Example usage
if __name__ == "__main__":
    print("Your IP address is:", get_ip())
