#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="", breed=""):
        self.name = name
        self.breed = breed

        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
        elif not isinstance(breed, str) or breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            print("Dog created successfully!")
