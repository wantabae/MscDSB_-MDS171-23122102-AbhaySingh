class PetStore:
    def __init__(self):
        self.pets = {
            "dogs": [],
            "cats": [],
            "rabbits": [],
            "parrots": []
        }

    def store_new_pet(self, name, species, age, price):
        pet = {'name': name, 'species': species, 'age': age, 'price': price}
        # Append the new pet to the appropriate species list
        if species in self.pets:
            self.pets[species].append(pet)

    def search_pet(self, name):
        for species, pet_list in self.pets.items():
            for pet in pet_list:
                if pet['name'] == name:
                    return pet
        return None

    def sell_pet(self, name):
        pet = self.search_pet(name)
        if pet:
            for species, pet_list in self.pets.items():
                if pet in pet_list:
                    pet_list.remove(pet)

    def list_all_pets(self):
        all_pets = []
        for species, pet_list in self.pets.items():
            all_pets.extend(pet_list)
        return all_pets
