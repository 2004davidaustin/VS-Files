response = ""
accounts = []
balances = []



print("\nEnter the names and balances of bank accounts (type: quit when done)")


while response.lower() != "quit" :
    response = input("What's the name of this account? ")
    if response.lower() != "quit" : accounts.append(response)
    if response.lower() != "quit" : balances.append(float(input("What's it's balance? ")))


print("\nAccount Information:")

for i, account in enumerate(accounts) : 
    print(f"{account.title()} - {balances[i]}")

print(f"\nTotal: {sum(balances)}")
print(f"Average: {sum(balances)/len(balances)}")