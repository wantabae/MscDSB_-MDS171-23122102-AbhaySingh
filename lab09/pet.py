from petstore import PetStore  # Assuming the PetStore class is in a file named petstore.py

def print_menu():
    print("Pet Store Management System")
    print("1. Add a new pet")
    print("2. Search for a pet")
    print("3. List all pets")
    print("4. Buy a pet")
    print("5. Exit")

def add_new_pet(pet_store):
    name = input("Enter pet name: ")
    species = input("Enter species (e.g., dogs, cats, rabbits, parrots): ")
    age = input("Enter pet age: ")
    price = input("Enter pet price: ")
    pet_store.store_new_pet(name, species, age, price)
    print(f"{name} has been added to the store.")

def search_pet(pet_store):
    name = input("Enter the name of the pet you want to search for: ")
    pet = pet_store.search_pet(name)
    if pet:
        print(f"Found pet: {pet}")
    else:
        print(f"No pet with the name {name} found in the store.")

def list_all_pets(pet_store):
    all_pets = pet_store.list_all_pets()
    if all_pets:
        print("List of all pets in the store:")
        for pet in all_pets:
            print(pet)
    else:
        print("The store has no pets currently.")

def buy_pet(pet_store):
    name = input("Enter the name of the pet you want to buy: ")
    pet = pet_store.search_pet(name)
    if pet:
        pet_store.sell_pet(name)
        print(f"You have successfully bought {name}.")
    else:
        print(f"No pet with the name {name} found in the store.")

if __name__ == "__main__":
    pet_store = PetStore()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_new_pet(pet_store)
        elif choice == "2":
            search_pet(pet_store)
        elif choice == "3":
            list_all_pets(pet_store)
        elif choice == "4":
            buy_pet(pet_store)
        elif choice == "5":
            print("Exiting the Pet Store Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
