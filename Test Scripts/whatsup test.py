from netaddr import *
from jinja2 import Template

ip = IPAddress('62.125.24.5')
y =ip.is_private()
print(y)
x =ip.is_unicast() and  ip.is_private()
print(x)