import getpass

users = {
    'admin': '123',
    'carlos': 'abc123'
}
    
def show_help():
    print("\n--- Help Page ---")
    print("If you forgot your username or password: ")
    print("- Contato the system administrator.")
    print("- Or reset your password if you have access to the recovery email. \n")

def login():
    print("\n 💻 LOGIN PAGE")
    username = input("👤 Username: ")
    password = getpass.getpass("🔑 Password: ")

def register():
    print("\n 📝 REGISTER NEW USER")
    username = input("👤  Create a username: ")
    
    if username in users:
        print("⚠️ Username already exists. Try another one.")
        return
    
    password = input("🔑 Create a password: ")
    confirm_password = input("🔁 Confirm password: ")
    
    if password != confirm_password:
        print("❌ Passwords do not match.Try again.")
        return
    
    users[username] = password
    print(f"✅ User '{username}' registered successfully.")
        
    if username in users and users[username] == password:
        print(f"\n ✅ Welcome {username}! Access granted, have a nice day !!")
        return True
    else:
        print("\n ❌ Invalid username or password. Try again.")
        return False
    
    def show_help():
        print("\n 📘 HELP PAGE")
        print("Forgot your username or password?")
        print("-> Unfortunately, this simple version does not store data permanently. ")
        print("-> You must re-register if you forget you credentials. ")
        print("\n 💡 Tips: ")
        print("• Choose a username you won't forget.")
        print("• Use a memorable but secure password. ")
        print("• This system is for training purposes only (no data saved after closing).")
    
while True:
    print("\n 🔐 Main Menu ")
    print("1. Login")
    print("2. Register")
    print("2. Help")
    print("3. Exit")
    
    option = input("Choose an option:")
    
    if option == "1":
        login()
    elif option == "2":
        register()
    elif option == "3":
        show_help()
    elif option == "4":
        print("See later...!!👋")
        print("Thank you for using our Access Control System!")
        break
    else:
        print("❗ Invalid option. Try again.")