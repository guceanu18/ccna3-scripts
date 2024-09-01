from ncclient import manager

# Device connection details
host = "192.168.178.147"  # Replace with the IP address of your CSR 1000v device
port = 830
username = "cisco"  # Replace with your username
password = "cisco123!"  # Replace with your password
loopback_id = '1'
loopback_ip = '1.1.1.1'

loopback_config = f"""
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>Loopback{loopback_id}</name>
      <description>Configured by NETCONF</description>
      <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
      <enabled>true</enabled>
      <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
        <address>
          <ip>{loopback_ip}</ip>
          <netmask>255.255.255.0</netmask>
        </address>
      </ipv4>
    </interface>
  </interfaces>
</config>
"""


def configure_loopback(host, port, username, password, netconf_config):
    try:
        with manager.connect(
                host=host,
                port=port,
                username=username,
                password=password,
                hostkey_verify=False,
                device_params={'name': 'csr'},
                look_for_keys=False,
                allow_agent=False
        ) as m:
            # Send the configuration
            response = m.edit_config(target="running", config=netconf_config)
            print("NETCONF Response:")
            print(response)
    except Exception as e:
        print(f"Failed to configure NETCONF: {e}")


if __name__ == "__main__":
    configure_loopback(host, port, username, password, loopback_config)

