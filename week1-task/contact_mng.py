import sys
import pandas as pd
from filelock import FileLock
import configparser
from configparser import ConfigParser, ExtendedInterpolation



class ContactAlreadyExists(Exception):
    """This exception is raised when a user try to insert the existing
    contact details in the Contact Directory.
    """


class ContactNotfound(Exception):
    """This exception is raised when a user tries to update non-existing
    contact details in the Contact Directory.
    """


class ContactInfoUnFound(Exception):
    """This exception is raised when a user tries to search non-existing
    contact details in the Contact Directory.
    """


class EnterValidNumber(Exception):
    """This exception is raised when a user enters invalid number that is not
    present in the menu of Contact Directory Application
    """


class ContactDirectory:
    """This is class for Contact Management system"""

    def __init__(self, file):
        self.file_name = file
        lockfile = self.file_name+".lock"
        self.lock = FileLock(lockfile)

    def directory_options(self):
        """This function displays the menu for the users."""

        print('*' * 120, '\nWelcome to Contact Directory Application!'
                'Now you can Proceed with following options\n',
                '*' * 120)

        print(
            'Please enter 1 to insert the contact details\n',
            '\nPlease enter 2 to update the contact details\n',
            '\nPlease enter 3 to search the contact details\n',
            '\nPlease enter 4 to delete the contact details\n',
            '\nPlease enter 5 to display the contact details\n',
            '\nPlease enter 6 to exit the contact directory\n'
        )

    def num_exists(self, num):
        """This function checks if the number provided by user exists in
        contact directory.
        """

        df_1 = pd.read_csv(self.file_name)
        if num in df_1['Phonenum'].values:
            return True
        return False

    def insert_contact_num(self, name, num, org):
        """This function adds new contact to contact directory"""

        if self.num_exists(num):
            raise ContactAlreadyExists(
                'Contact already exists please enter new number'
            )

        self.lock.acquire()
        df_1 = pd.read_csv(self.file_name)
        new_row = {'Name': [name], 'Phonenum': [num], 'Org': [org]}
        df_2 = pd.DataFrame(new_row)
        df_3 = pd.concat([df_1, df_2], ignore_index=True)
        df_3.to_csv(self.file_name, index=False)
        self.lock.release()
        print('Contact successfully added')

    def update_contact_num(self, name, num1, num2):
        """This function updates the existing contact in contact directory."""

        if self.num_exists(num1):
            self.lock.acquire()
            df_1 = pd.read_csv(self.file_name)
            name_index = df_1.index[df_1['Name'] == name].tolist()
            num_index = df_1[df_1['Phonenum'] == num1].index[0]
            for ind in name_index:
                if ind == num_index:
                    df_1.at[ind, 'Phonenum'] = num2
                    df_1.to_csv(self.file_name, index=False)
                    self.lock.release()
                    return 'Contact updated successfully'

        else:
            raise ContactNotfound('Contact name or number not found')

    def search_contact_details(self, name):
        """This function searches for existing contact in contact directory"""

        df_1 = pd.read_csv(self.file_name)
        if name in df_1['Name'].values:
            contact_details = df_1[df_1['Name'] == name]
            print(contact_details)
        else:
            raise ContactInfoUnFound(
                'Contact details not found, please enter a valid Contact name'
            )

    def delete_contact(self, name, num):
        """This function deletes the existing contact in contact directory."""
        self.lock.acquire()
        df_1 = pd.read_csv(self.file_name)
        if name in df_1['Name'].values:
            name_index = df_1.index[df_1['Name'] == name].tolist()
            num_index = df_1[df_1['Phonenum'] == num].index[0]
            for ind in name_index:
                if ind == num_index:
                    df_2 = df_1.drop(ind)
                    df_2.to_csv(self.file_name, index=False)
                    self.lock.release()
                    return 'Contact_details deleted successfully'

        else:
            raise ContactInfoUnFound(
                'Contact details not found, please enter a valid Contact name'
                )

    def display_all_contacts(self):
        """This function displays all the contacts of contact directory."""

        df_1 = pd.read_csv(self.file_name)
        print(df_1)

    def exit_contact_directory(self):
        """This function exits contact directory."""

        print("*"*120)
        print("Thank you for using Contact directory system.")
        print("*"*120)
        sys.exit("Goodbye, have a nice day ahead!")


def get_val():
    """This function returns input values for contact directory."""

    name = input('Please enter the contact name:')
    num = int(input('Please enter the contact number:'))
    org = input('Please enter the organization name:')
    return name, num, org

def get_config():

    config = ConfigParser(interpolation=ExtendedInterpolation())
    config.read('config.ini')
    return config


if __name__ == '__main__':
    CONFIG = get_config()
    print(CONFIG['Data']['CONTACT_FILE'])
    c = ContactDirectory(CONFIG['Data']['CONTACT_FILE'])
    while True:

        c.directory_options()
        inp1 = int(input('Please enter the number:'))

        if inp1 == 1:
            inp_val = get_val()
            c.insert_contact_num(inp_val[0], inp_val[1], inp_val[2])

        elif inp1 == 2:
            inp_name = input('Please enter the contact name:')
            inp_num1 = int(input('Please enter the previous contact number:'))
            inp_num2 = int(input('Please enter the present number:'))
            c.update_contact_num(inp_name, inp_num1, inp_num2)

        elif inp1 == 3:
            inp_name = input('Please enter the contact name: ')
            c.search_contact_details(inp_name)

        elif inp1 == 4:
            inp_name = input('Please enter the contact name: ')
            inp_num = int(input('Please enter the contact number: '))
            c.delete_contact(inp_name, inp_num)

        elif inp1 == 5:
            c.display_all_contacts()

        elif inp1 == 6:
            c.exit_contact_directory()

        else:
            raise EnterValidNumber('Please enter valid number')
