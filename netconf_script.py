from ncclient import manager

# Device connection details
host = "192.168.178.147"  # Replace with the IP address of your CSR 1000v device
port = 830
username = "cisco"  # Replace with your username
password = "cisco123!"  # Replace with your password


def test_netconf_connectivity(host, port, username, password):
    try:
        with manager.connect(
                host=host,
                port=port,
                username=username,
                password=password,
                hostkey_verify=False
        ) as m:
            print("NETCONF connection successful!")
            print(f"Server Capabilities: {m.server_capabilities}")
            for capability in m.server_capabilities:
                print(capability)
    except Exception as e:
        print(f"Failed to connect to NETCONF server: {e}")


if __name__ == "__main__":
    test_netconf_connectivity(host, port, username, password)

