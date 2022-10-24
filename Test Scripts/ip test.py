from netaddr import *




input_address = IPNetwork('192.168.1.1/24')
print(input_address.version)


address = input_address.ip
network = input_address.network
netmask = input_address.netmask
netmask_dec = input_address.value

print(address,network,netmask,netmask_dec )