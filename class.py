from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if len(value) <= 1:
            raise ValueError("Ім'я не може бути менше 1 букви")
        super().__init__(value)
        
        
            
        
        

class Phone(Field):
    def __init__(self, value):
        if len(value) != 10:
            raise ValueError("Невірна довжина номера")
        elif not value.isdigit():
            raise ValueError('Введіть лише цифри')
        super().__init__(value)

        
        

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self,phone):
        self.phones.append(Phone(phone))
        
    def find_phone(self,user_phone):
        for phone in self.phones:
            if phone.value == user_phone:
                return phone

    def edit_phone(self,old_phone, new_phone):
        
        for phone in self.phones:  
            if phone.value == old_phone:
                self.phones.remove(phone)
                self.phones.append(Phone(new_phone))
                return
        raise ValueError('Відсутній телефон')
                
            
    def remove_phone(self,remove):
        for phone in self.phones:  
            if phone.value == remove:
                self.phones.remove(phone)
                break
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    
    def add_record(self,rec):
        self.data[rec.name.value] = rec

    def find(self,obj):
        return self.data.get(obj)
    
    def delete(self,user):
        return self.data.pop(user)

    def __str__(self):
        return '\n'.join([str(x) for x in self.data.values()])


# Створення нової адресної книги
book = AddressBook()

    # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

    # Виведення всіх записів у книзі
     
print(book)

    # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
# john.remove_phone("1112223333")


print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # Видалення запису Jane
book.delete("Jane")
