#!/usr/env python3
import os
import shutill
import sys

def check_reboot():
	"""Returns True if the computer has a pending reboot."""
	return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
	"""Returns True if there isn't enough disk space, False otherwise."""
	du = shutill.disk_usage(disk)
	# Calculate the percenage of free space
	percent_free = 100 * du.free / du.total
	# Calculate how many free gigabytes
	gigabytes_free = du.free / 2**30
	if percent_free < min_percent or gigabytes_free < min_gb:
		return True
	return False

def main():
	# pass
	if check_reboot():
		print("Pending Reboot.")
		sys.exit(1)
	if check_disk_full(disk="/", min_gb=2, min_percent=10):
			print("Disk Full.")
			sys.exit(1)
	print("Everthing ok.")
	sys.exit(0)

main()
