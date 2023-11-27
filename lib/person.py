#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="", job=""):
        self.name = name
        self.job = job

        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be a string between 1 and 25 characters.")
        elif not isinstance(job, str) or job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        elif not job:
            print("Job must be provided.")
        else:
            self.name = self.format_name(name)
            print("Person created successfully!")

    def format_name(self, name):
        return " ".join([part.capitalize() for part in name.split()])
