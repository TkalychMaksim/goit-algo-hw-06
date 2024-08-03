from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value


    def __str__(self):
        return str(self.value)
    
    
    def __eq__(self, other):
        if isinstance(other, Field):
            return self.value == other.value
        return False


    def __hash__(self):
        return hash(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if len(value) != 10:
            raise ValueError("The phone number must not exceed 10 characters")
        else:
            super().__init__(value)
		

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
        
    def add_phone(self,value):
        phone = Phone(value)
        self.phones.append(phone)
        
        
    def remove_phone(self,value):
        phone_to_remove = Phone(value)
        if phone_to_remove in self.phones:
            self.phones.remove(phone_to_remove)
            print("The number has been deleted")
        else:
            print("The number has not founded")
            
            
    def edit_phone(self,old_value,new_value):
        old_phone = Phone(old_value)
        new_phone = Phone(new_value)
        if old_phone in self.phones:
            self.phones[self.phones.index(old_phone)] = new_phone
            print(f"Phone number {old_value} was changed by {new_value}")
        else:
            print(f"Phone number {old_value} not found")
            
            
    def find_phone(self,value):
        finding_phone = Phone(value)
        for phone in self.phones:
            if phone == finding_phone:
                return phone
        return None


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        
        
    def add_record(self,record):
        self.data[record.name.value] = record
        
        
    def find(self,value):
        if value in self.data.keys():
            return self.data[value]
        else:
            return None
        
        
    def delete(self,value):
        if value in self.data.keys():
            self.data.pop(value)
        else:
            print("Record not found")
            
            
    def __str__(self):
        return '\n'.join([f"{key}: {record}" for key, record in self.data.items()])
    
    
# Створення нової адресної книги
book=AddressBook()
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
print("-_-_-_-_-_-_-_-_-_")
# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555
print("-_-_-_-_-_-_-_-_-_")
# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555
print("-_-_-_-_-_-_-_-_-_")
# Видалення запису Jane
book.delete("Jane")
print(book)

