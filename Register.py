# Dictionary to store user credentials
credentials = {}

# Function to register a new user
def register():
    username = input("Enter a username: ")
    if username in credentials:
        print("Username already exists. Please try again.")
        return
    password = input("Enter a password: ")
    credentials[username] = password
    print("User registered successfully!")

# Function to login
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in credentials and credentials[username] == password:
        print("Login successful!")
        secure_page(username)
    else:
        print("Login failed. Invalid username or password.")

# Function to access a secured page
def secure_page(username):
    print(f"Welcome, {username}! You have accessed the secured page.")

# Main menu
def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()