"""Count IP Addresses."""


def ips_between(start: str, end: str) -> int:
    """Count the number of IP addresses between two given IP addresses."""
    start_ip: list[int] = split_ip(start)
    end_ip: list[int] = split_ip(end)
    address_count: int = 0
    for i in range(4):
        address_count += (end_ip[i] - start_ip[i]) * (256 ** (3 - i))
    return address_count


def split_ip(ip: str) -> list[int]:
    """Split an IP address into a list of integers."""
    return list(map(int, ip.split('.')))


if __name__ == "__main__":

    print(ips_between("150.0.0.0", "150.0.0.1"), 1)
    print(ips_between("10.0.0.0", "10.0.0.50"), 50)
    print(ips_between("20.0.0.10", "20.0.1.0"), 246)
    print(ips_between("10.11.12.13", "10.11.13.0"), 243)
    print(ips_between("160.0.0.0", "160.0.1.0"), 256)
