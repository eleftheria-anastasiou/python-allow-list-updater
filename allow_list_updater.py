
# Define a function to remove unwanted IP addresses
def update_allow_list(ip_addresses, remove_list):
    updated_addresses = []

    for address in ip_addresses:
        if address not in remove_list:
            updated_addresses.append(address)

    return updated_addresses


# Run this part only when the file is executed directly
if __name__ == "__main__":

    # Open the file containing the allow-list
    with open("allow_list.txt", "r") as file:
        ip_addresses = file.read().split()

    # Create a list of IP addresses to remove
    remove_list = ["192.0.2.10", "198.51.100.20"]

    # Update the list using the function
    updated_addresses = update_allow_list(ip_addresses, remove_list)

    # Convert the updated list into a string
    ip_addresses = "\n".join(updated_addresses)

    # Write the updated list back to the file
    with open("allow_list.txt", "w") as file:
        file.write(ip_addresses)

    # Display the remaining IP addresses
    print("Updated allow-list:")
    for address in updated_addresses:
        print(address)
