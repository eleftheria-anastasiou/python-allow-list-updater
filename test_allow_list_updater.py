
from allow_list_updater import update_allow_list


# Test 1: Remove an address that exists in the file
ip_addresses = ["192.0.2.10", "192.0.2.25"]
remove_list = ["192.0.2.10"]

result = update_allow_list(ip_addresses, remove_list)

if result == ["192.0.2.25"]:
    print("Test 1 passed")
else:
    print("Test 1 failed")


# Test 2: Keep all addresses when nothing needs to be removed
ip_addresses = ["192.0.2.10", "192.0.2.25"]
remove_list = []

result = update_allow_list(ip_addresses, remove_list)

if result == ["192.0.2.10", "192.0.2.25"]:
    print("Test 2 passed")
else:
    print("Test 2 failed")


# Test 3: Keep addresses when the removal address is absent
ip_addresses = ["192.0.2.25"]
remove_list = ["198.51.100.20"]

result = update_allow_list(ip_addresses, remove_list)

if result == ["192.0.2.25"]:
    print("Test 3 passed")
else:
    print("Test 3 failed")
