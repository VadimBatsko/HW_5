
'''Четверте завдання'''
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd,*args
# Створюємо перевірки 
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Enter the argument for the command"
        except IndexError:
            return "Give me name and phone please."

    return inner

# Додавання контактів
@input_error
def add_contact(args, contacts):
        name, phone = args
        if name.isdigit() or not phone.isdigit():
            return 'Ups incorrect data (name\phone)'
        else:
            if name in contacts:
                return "Name is taken"
            else:
                contacts[name] = phone
                return "Contacts added."


# Зміна контактів
@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} is changes."

# Виведення контакту
@input_error
def show_phone(args, contacts):
    name = args[0]
    if name not in contacts:
        return "User not found"
    else:
        return f"Phone number {name}: {contacts[name]}"

# Вивід всіх контактів

def all(contacts):
    list = ''
    for i,k in contacts.items():
        list += f"Name: {i} number: {k}\n"
    return list
    


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "0"]:
            print("Good buy!")
            break
        elif command == "hello":
            print("How can i help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(all(contacts))
        else:
            print("Invalid command.")

if __name__ == '__main__':
    main()