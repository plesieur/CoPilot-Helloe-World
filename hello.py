def load_states(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return {line.strip().lower() for line in f if line.strip()}

states = load_states("states.txt")
name = input("What is your name? ")
city = input("What city/town do you live in? ")
state_input = input("What state do you live in? ")
while state_input.strip().lower() not in states:
    print("State not found. Please check the spelling and try again.")
    state_input = input("What state do you live in? ")
state = state_input.strip().title()
print(f"Hello, {name}")
print(f"Welcome to {city}, {state}")
