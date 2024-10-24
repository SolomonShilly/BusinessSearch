import random  # Import random to pick the business account randomly

# Welcome message
print("Searching for a business Instagram account...")

# Create a list of random Instagram account IDs
accountIDs = list(range(0, 10))  # List of Instagram account IDs
vipAccount = random.choice(accountIDs)  # Randomly selects the business account

# Display the list of account IDs
print("Instagram account IDs:", accountIDs)  # Shows the account list
print("\nSearching for the business account...\n")

# --- Linear Search ---
def linear_search(accounts, vip):
    steps = 0  # Counts the number of steps
    for i in range(len(accounts)):  # Loop through each account ID
        steps += 1  # Count each search as a step
        print(f"Checking {accounts[i]}...")  # Checking account ID
        if accounts[i] == vip:  # If current account matches business
            print(f"business found: {accounts[i]} in {steps} steps")  # business found message
            return steps  # Return steps taken to find the business
    return steps  # Return steps if not found (though it will be found)

# --- Binary Search ---
def binary_search(accounts, vip):
    steps = 0  # Counts the number of steps
    low = 0  # Starting index
    high = len(accounts) - 1  # Ending index

    while low <= high:  # While there are accounts to search
        steps += 1  # Count each search as a step
        mid = (low + high) // 2  # Find the middle account
        print(f"Checking {accounts[mid]}...")  # Checking middle account

        if accounts[mid] == vip:  # If middle account is business
            print(f"business found: {accounts[mid]} in {steps} steps")  # business found message
            return steps  # Return steps taken to find VIP
        elif accounts[mid] < vip:  # If business is in the second half
            low = mid + 1  # Narrow down to second half
        else:  # If VIP is in the first half
            high = mid - 1  # Narrow down to first half

    return steps  # Return steps if not found (though it will be found)

# Perform the searches
print("\n--- Linear Search ---")
linearSteps = linear_search(accountIDs, vipAccount)  # Perform Linear Search

print("\n--- Binary Search ---")
binarySteps = binary_search(accountIDs, vipAccount)  # Perform Binary Search

# Recap
print(f"\nLinear Search took {linearSteps} steps.")
print(f"Binary Search took {binarySteps} steps.")