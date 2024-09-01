from netmiko import ConnectHandler


def configure_ospf(device_params, process_id, networks):
    connection = ConnectHandler(**device_params)
    commands = [f"router ospf {process_id}"]
    for network in networks:
        commands.append(f"network {network['network']} {network['wildcard']} area 0")

    output = connection.send_config_set(commands)
    print(output)

    output = connection.send_command("show ip ospf int brief")
    print(output)

    connection.disconnect()


device_params = {
    'device_type': 'cisco_ios',
    'host': '192.168.178.144',
    'username': 'admin',
    'password': 'admin'
}

networks_r8 = [
    {'network': '192.168.0.0', 'wildcard': '0.0.255.255'},
    {'network': '8.8.8.8', 'wildcard': '0.0.0.0'}
]

configure_ospf(device_params, 1, networks_r8)

connection = ConnectHandler(**device_params)
output = connection.send_command("show ip ospf neigh")
print(output)

connection.disconnect()

