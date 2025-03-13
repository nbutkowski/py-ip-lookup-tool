import ipaddress

def find_matching_cidr(ip, cidr):
    """Check if an IP address is inside a CIDR block."""
    ip_obj = ipaddress.ip_address(ip.strip())  # Strip spaces if any
    network = ipaddress.ip_network(cidr, strict=False)
    return ip_obj in network
