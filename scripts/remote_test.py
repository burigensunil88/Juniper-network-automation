import os
from jnpr.junos import Device

dev = Device(
    host=os.environ["JUNOS_HOST"],
    user=os.environ["JUNOS_USER"],
    passwd=os.environ["JUNOS_PASSWORD"],
    port=int(os.environ["JUNOS_PORT"])
)

dev.open()

print(dev.facts["hostname"])
print(dev.facts["version"])
print("Remote NETCONF connectivity successful")

dev.close()