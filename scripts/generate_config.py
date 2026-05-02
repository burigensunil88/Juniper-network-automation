import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined

# Load YAML data
with open('../inventory/device.yaml') as f:
    data = yaml.safe_load(f)

# Load template
env = Environment(
    loader=FileSystemLoader('../templates'),
    undefined=StrictUndefined
)
template = env.get_template('interface.j2')

# Generate configs
for device in data['devices']:

    config = template.render(
        hostname=device['hostname'],
        interface=device['interface'],
        description=device['description'],
        ip=device['ip'],
        prefix=device['prefix']
    )

    filename = f"../configs/{device['hostname']}.conf"

    with open(filename, 'w') as output:
        output.write(config)

    print(f"Generated config for {device['hostname']}")