
class Phonebook:
    """A contact book that saves name, number, address, and email of a contact"""

    def __init__(self, contact = None):
        if contact is None:
            contact = {}
        self.master = contact 

    def __str__(self):
        return f"{self.master}"

    def add_contact(self, name, num = None, addr = None, em = None):
        self.master[name] = dict(Number = num, Address = addr, Email = em)
    
    def delete_contact(self, name):
        del self.master[name]

    def edit_contact(self, name, **kwargs):
        for key, value in kwargs.items():
            self.master[name][key] = value

    def edit_contact_name(self, old_name, new_name):
        self.master[new_name] = self.master[old_name]
        del self.master[old_name]

def main():
    contacts = {"Lily": {"Number": "917-615-8932"}}
    brian = Phonebook(contacts)
    print(brian)

    brian.add_contact("Brian", "857-271-6677", "275 2nd Ave", "btjoajadi1@babson.edu")
    print(brian)

    brian.delete_contact("Brian")
    print(brian)

    brian.edit_contact_name("Lily", "Lily Chi")
    print(brian)
    
    brian.edit_contact("Lily Chi", Address = "Shrewsbury", Email = "lchi1@babson.edu")
    print(brian)
if __name__ == '__main__':
    main()