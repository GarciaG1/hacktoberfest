def show_menu():
    print("Select a programming language:")
    print("1. Python")
    print("2. JavaScript")
    print("3. Java")
    print("4. C++")
    print("5. Ruby")
    print("6. Exit")

def hello_world(lang_choice):
    messages = {
        1: "Python: print('Hello, World!')",
        2: "JavaScript: console.log('Hello, World!');",
        3: "Java: System.out.println('Hello, World!');",
        4: "C++: std::cout << 'Hello, World!' << std::endl;",
        5: "Ruby: puts 'Hello, World!'"
    }
    return messages.get(lang_choice, "Invalid option. Try again.")

def main():
    while True:
        show_menu()
        try:
            choice = int(input("Enter the number of your choice: "))
            if choice == 6:
                print("Exiting the program. Goodbye!")
                break
            print(hello_world(choice))
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
