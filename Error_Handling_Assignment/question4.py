#Question 5: List Index Access

items = ["apple", "banana", "cherry"]
index = int(input("Enter the index of the item you want to access: "))
try:
    print("You selected:", items[index])
except IndexError:
    print(f"Heyya, Index '{index}' is not included.")