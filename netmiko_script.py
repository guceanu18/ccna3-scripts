from netmiko import ConnectHandler


def configure_ospf(device_params, ospf_process_id, ospf_networks):
    try:
        connection = ConnectHandler(**device_params)

        config_commands = [f'router ospf {ospf_process_id}']

        for network in ospf_networks:
            config_commands.append(f'network {network["network"]} {network["wildcard_mask"]} area {network["area"]}')

        output = connection.send_config_set(config_commands)

        print(output)

        save_output = connection.save_config()
        print(save_output)

        connection.disconnect()

    except Exception as e:
        print(f"An error occurred: {e}")


def send_command(device_params, command):
    try:
        connection = ConnectHandler(**device_params)
        output = connection.send_command(command)
        print(output)
        connection.disconnect()
    except Exception as e:
        print(e)


device_params = {
    'device_type': 'cisco_ios',
    'host': '192.168.178.141',
    'username': 'admin',
    'password': 'admin',
}

ospf_process_id = 1
ospf_networks = [
    {'network': '10.0.0.0', 'wildcard_mask': '0.255.255.255', 'area': 0}
]

configure_ospf(device_params, ospf_process_id, ospf_networks)

send_command(device_params, "show ip ospf neighbor")

