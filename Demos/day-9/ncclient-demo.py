from ncclient import manager

# Define device connection parameters
device_params = {
    "host": "sbx-nxos-mgmt.cisco.com",
    "port": 830, # Default NETCONF port
    "username": "anindita",
    "password": "zu_2T_D0P6_mE5ym",
    "device_params": {"name": "nexus"} # Targets device type (e.g., csr, nexus, juniper)
}

# Establish connection using a context manager
with manager.connect(**device_params) as m:
    print("--- Supported Server Capabilities ---")
    for capability in m.server_capabilities:
        print(capability)
