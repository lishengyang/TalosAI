import pyudev
import subprocess

# Define the mount point
mount_point = "/mount/udisk"

# Create a pyudev context
context = pyudev.Context()

# Define a function to mount the device
def mount_device(dev):
    device = pyudev.Devices.from_device_file(context, dev)
    if device.get('ID_FS_TYPE') == 'vfat':  # Change the filesystem type as needed
        subprocess.call(["mount", dev, mount_point])
        print("Device {} mounted to {}".format(dev, mount_point))

# Monitor for USB storage devices
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by('block', device_type='disk')
for device in iter(monitor.poll, None):
    if device.action == 'add':
        mount_device(device.device_node)

