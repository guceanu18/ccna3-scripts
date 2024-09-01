from pprint import pprint

import napalm


def napalm_example(device_params):
    try:
        # Initialize the NAPALM driver for the device
        driver = napalm.get_network_driver(device_params['driver'])
        device = driver(
            hostname=device_params['hostname'],
            username=device_params['username'],
            password=device_params['password']
        )

        # Open the connection to the device
        device.open()

        # Retrieve interface IP addresses
        ip_interfaces = device.get_interfaces_ip()
        print("Interface IP Addresses:")
        pprint(ip_interfaces)

        # Close the connection
        device.close()
        return ip_interfaces

    except Exception as e:
        print(f"An error occurred: {e}")


# Define device connection parameters
device_params = {
    'driver': 'ios',  # Specify the NAPALM driver for the device (e.g., ios, iosxr, eos, junos, etc.)
    'hostname': '192.168.178.141',
    'username': 'admin',
    'password': 'admin'
}

# Execute the NAPALM example script
interfaces = napalm_example(device_params)
print(interfaces['Ethernet1/0']['ipv4'])

