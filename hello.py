def load_states(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return {line.strip().lower() for line in f if line.strip()}


def load_countries(filename):
    with open(filename, "r", encoding="utf-8") as f:
        countries = set()
        for line in f:
            value = line.strip()
            if not value or value.endswith(":"):
                continue
            countries.add(value.lower())
        return countries

states = load_states("states.txt")
countries = load_countries("americas_countries.txt")

name = input("What is your name? ")
city = input("What city/town do you live in? ")
state_input = input("What state do you live in? ")
while state_input.strip().lower() not in states:
    print("State not found. Please check the spelling and try again.")
    state_input = input("What state do you live in? ")
state = state_input.strip().title()

country_input = input("What country do you live in? ")
while country_input.strip().lower() not in countries:
    print("You spelled the country wrong. Please try again.")
    country_input = input("What country do you live in? ")
country = country_input.strip().title()

print(f"Hello, {name}")
print(f"Welcome to {city}, {state}, {country}")
