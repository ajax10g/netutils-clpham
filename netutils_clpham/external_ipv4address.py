import netifaces
import ipaddress


def external_ipv4address() -> ipaddress.IPv4Address | None:
    """
    Returns the host's ipv4 address as an ipaddress.IPv4Address object if found;  otherwise None.
    """

    try:
        default_gw_intf_name = netifaces.gateways()['default'][netifaces.AF_INET][1]

        # Get the network addresses from the default interface
        netaddrs = netifaces.ifaddresses(default_gw_intf_name)

        ipv4_str = netaddrs[netifaces.AF_INET][0]['addr']

        return ipaddress.IPv4Address(ipv4_str)

    except Exception:
        return None
