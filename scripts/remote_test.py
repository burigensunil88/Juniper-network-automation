from jnpr.junos import Device

dev = Device(
    host='66.129.235.201',
    user='jcluser',
    passwd='Juniper!1',
    port=31001
)

dev.open()

print(dev.facts['hostname'])
print(dev.facts['version'])

dev.close()