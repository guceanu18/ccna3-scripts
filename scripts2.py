import napalm
from pprint import pprint

device_params = {
    'driver': 'ios',
    'hostname': '192.168.178.144',
    'username': 'admin',
    'password': 'admin'
}

driver = napalm.get_network_driver(device_params['driver'])
device = driver(hostname=device_params['hostname'],
                username=device_params['username'],
                password=device_params['password'])

device.open()

int_ip = device.get_interfaces_ip()
pprint(int_ip)
device.close()

eth1_0 = list(int_ip['Ethernet1/0']['ipv4'].keys())[0]
print(eth1_0)




