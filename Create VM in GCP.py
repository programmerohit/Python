from google.cloud import compute

# Define the name of the VM and the zone
instance_name = 'my-website-vm'
zone = 'us-central1-a'

# Create a compute client
compute_client = compute.Client()

# Create a configuration for the VM
config = compute.types.InstanceConfig(
    machine_type='f1-micro',
    labels={'website': 'true'},
    image_project='ubuntu-os-cloud',
    image_family='ubuntu-2004-lts',
    boot_disk_size_gb=10
)

# Create the VM
operation = compute_client.create_instance(instance_name, zone, config)
operation.result()

# Install Apache web server
operation = compute_client.run_shell_command(instance_name, zone, ['sudo', 'apt-get', 'update'])
operation.result()
operation = compute_client.run_shell_command(instance_name, zone, ['sudo', 'apt-get', 'install', '-y', 'apache2'])
operation.result()

# Copy the website files to the VM
compute_client.scp_files(instance_name, zone, '/path/to/website/*', '/var/www/html/')

# Start the Apache service
operation = compute_client.run_shell_command(instance_name, zone, ['sudo', 'systemctl', 'start', 'apache2'])
operation.result()

# Print the external IP address of the VM
instance = compute_client.get_instance(instance_name, zone)
print(instance.network_interfaces[0].access_configs[0].nat_ip)
