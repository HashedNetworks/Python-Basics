# creas la config, 
# la pasas en el equipo y validas q si quedo como debe quedar. 
# y das un reporte con los resultados.

from netaddr import *
from jinja2 import Template

ip_range =['192.168.1.1/24',
           '192.168.1.2',
           '172.16.1.0/33',
           '10.0.0.0/8',
           '62.125.24.5',
           '1.1.1.259/33'
           ]



# Ip validation . The IP will come from YAML File with variables
def check_valid_ip_addr(ip_addr):
    try:
        input_address = IPNetwork(ip_addr)
   
        address = input_address.ip
        network = input_address.network
        netmask = input_address.netmask
        netmask_len = input_address.prefixlen
        is_private = input_address.is_private()
        is_unicast = input_address.is_unicast()

        
        return [str(address), netmask_len, str(netmask), str(network), bool(is_private), bool(is_unicast) ]
        
    except AddrFormatError:
        #print(f'Invalid IP address Entered {ip_addr}')
        return 'Invalid'





def main():

    for ip in ip_range :
        ip_addr = ip
        addr_info = check_valid_ip_addr(ip_addr)


        if addr_info == 'Invalid':
             continue            
        else:
            print('')
            print(f'Valid IP address Entered:\n IP: {addr_info[0]}\n NETWORK: {addr_info[3]}\{addr_info[1]}\n IS PRIVATE: {addr_info[4]}\n') 




main()


