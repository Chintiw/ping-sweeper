import ipaddress
from ping3 import ping, verbose_ping

def ping_sweeper(network, timeout=2, verbose=False):

    live_hosts = []

    # Create an IPv4 network object
    ip_network = ipaddress.IPv4Network(network, strict=False)

    # Loop through each host in the network
    for ip in ip_network.hosts():
        ip_str = str(ip)
        result = ping(ip_str, timeout=timeout)

        if result is not None:
            live_hosts.append(ip_str)

        if verbose:
            print(f"{ip_str} {'is alive' if result else 'did not respond'}")

    return live_hosts

# Example usage
if __name__ == "__main__":
    network_to_sweep = "192.168.1.0/24"
    live_hosts = ping_sweeper(network_to_sweep, verbose=True)

    print("\nLive Hosts:")
    for host in live_hosts:
        print(host)

