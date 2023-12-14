import cache
import socket

dns_cache = cache.DnsCache("bard.google.com", 5)

real_getaddrinfo = socket.getaddrinfo

def my_getaddrinfo(host, port, family=0, type=0, proto=0, flags=0):
	if host == "bard.google.com":
		address = dns_cache.getaddress
		return [(socket.AF_INET, type, proto, '', (address, port))]
	else:
		return real_getaddrinfo(host, port, family, type, proto, flags)

def enable():
	socket.getaddrinfo = my_getaddrinfo