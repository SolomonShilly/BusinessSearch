# Business Instagram Account Search Script

This Python script simulates searching for a business Instagram account using Linear and Binary Search. The script randomly selects an Instagram account ID from a list and demonstrates how both search methods work by counting the steps each takes to find the selected account.

## Features

- **Random Account Selection**: A random Instagram account is chosen from a list of account IDs.
- **Linear Search**: A step-by-step search through each account until the desired business account is found.
- **Binary Search**: A more efficient search method that divides the list in half to find the business account.

## How It Works

1. **Random Account Selection**: 
   - The script generates a list of Instagram account IDs and randomly selects one as the business account (VIP).
   
2. **Linear Search**:
   - Searches each account in the list one by one.
   - Prints the number of steps taken to find the business account.

3. **Binary Search**:
   - Uses a divide-and-conquer approach to search the list more efficiently.
   - Prints the number of steps taken to find the business account.

4. **Results**: 
   - The script displays how many steps each search method took to find the business account.

## Usage

Simply run the script, and it will:
- Display the list of account IDs.
- Perform both Linear and Binary searches to find the business account.
- Print the number of steps each search method took.

## Requirements
- Python 3.x
- `random` library (standard in Python)

## Installation

1. Clone or download this script.
2. Run the script using Python 3.x:
   ```bash
   python search_script.py

