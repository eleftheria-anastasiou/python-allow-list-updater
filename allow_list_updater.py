
from pathlib import Path


def update_allow_list(
    file_path: Path,
    remove_list: set[str],
) -> list[str]:
    """Remove specified addresses from an allow-list file."""

    addresses = file_path.read_text(
        encoding="utf-8"
    ).splitlines()

    updated_addresses = [
        address.strip()
        for address in addresses
        if address.strip() and address.strip() not in remove_list
    ]

    file_path.write_text(
        "\n".join(updated_addresses)
        + ("\n" if updated_addresses else ""),
        encoding="utf-8",
    )

    return updated_addresses


if __name__ == "__main__":
    file_path = Path("allow_list.txt")

    remove_list = {
        "192.0.2.10",
        "198.51.100.20",
    }

    updated = update_allow_list(file_path, remove_list)

    print(f"Updated allow-list: {len(updated)} addresses remain.")
    for address in updated:
        print(address)
