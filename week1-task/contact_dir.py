import sys
import pandas as pd
from filelock import FileLock
from custom_exception import (
    ContactAlreadyExists,
    ContactNotfound,
    ContactInfoUnFound
)


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