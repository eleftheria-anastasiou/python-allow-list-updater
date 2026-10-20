# Python Allow-List Updater

## Overview

This project demonstrates how Python can automate the removal of IP addresses from an allow-list used to represent access permissions.

The project is based on an exercise completed as part of the Google Cybersecurity Professional Certificate. I am developing the original exercise into a standalone project with runnable code, testing, and documentation.

## Objective

The objective is to remove addresses that are no longer authorized from a local allow-list file while preserving the remaining entries.

## Technologies

- Python
- File handling with `pathlib`
- Lists, sets, loops, and conditional logic
- Automated testing with Python's `unittest` framework

## Methodology

1. Read the addresses from a local text file.
2. Compare the existing addresses against a removal list.
3. Build an updated list that excludes the specified addresses.
4. Write the updated list to the file.
5. Verify the result through automated tests.

## Security relevance

Maintaining accurate access lists is one part of access management. Removing entries that are no longer authorized can help reduce unnecessary access when the list is used by an appropriate access-control system.

This script operates on a local text file only. It does not enforce network access controls.

## Testing

Automated tests will cover address removal, addresses that are not present in the removal list, and preservation of unrelated entries.

## Limitations and future improvements

- Validate IPv4 addresses before processing them.
- Handle missing files and file-permission errors.
- Avoid overwriting the original file if an update fails.
- Add logging and a summary of changes.
- Expand test coverage for edge cases.

## Learning outcome

This project builds on Python fundamentals from the Google Cybersecurity Professional Certificate and explores how automation can support security-related administrative tasks.
