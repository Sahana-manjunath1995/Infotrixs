import pandas as pd
from filelock import FileLock
from tabulate import tabulate


class ContactDirectory:
    """
    This class represents a contact management system that can create,
    update, search, delete, and display contacts.
    """

    def __init__(self, file):
        """
        This is a constructor for ContactDirectory class
        :param file: .csv file
               desc: Contact information storage file
               Example:
                    file = contact.csv
        """
        self.file_name = file
        lockfile = self.file_name+".lock"
        self.lock = FileLock(lockfile)

    def get_contact(self, index):
        """
        This function retrieves the contact information based on the selected
        row number.

        :param index: int()
            desc: Row number selection by the user.
            Example:
                index = 1
        :return: dict{}
            desc: Contact information based on selected row
            Example:
                contact_dict = {'name': 'sahana', lname: 'nm','phone': '12345'}
        """

        df = pd.read_csv('contact.csv', dtype={'phone': str})
        return df.T[index].dropna().to_dict()

    def search_contact_exists(self, contact):
        """
        This function checks the presence of the contact, filtering only the
        contact data provided by the user.

        :param contact: dict()
            desc: User's Contact data
            Example:
                contact = {'name': 'sahana', lname: 'nm', 'phone': '12345'}
        :return: tuple(bool(), pd.DataFrame())
            res = (True,
                          fname lname  phone  org
                       -----------------------------
                       1  Sahana    nm  12366  NaN)

        """

        contact = {k: v for k, v in contact.items() if v != ''}
        df = pd.read_csv('contact.csv', dtype={'phone': str})
        filter_df = df.copy()
        for k, v in contact.items():
            filter_df = filter_df[filter_df[k] == v]

        if filter_df.shape[0]:
            return True, filter_df
        else:
            return False, filter_df

    def insert_contact_num(self, contact):
        """
        This function adds a contact information, and stores it in csv file.

        :param contact: dict()
            desc: The information submitted by the user.
            Example:
                contact = {'name': 'sahana', lname: 'nm', 'phone': '12345'}
        """

        self.lock.acquire()
        df = pd.read_csv(self.file_name, dtype={"phone": str})
        new_row = {k: [v] for k, v in contact.items()}
        new_contact_df = pd.DataFrame(new_row)
        merged_df = pd.concat([df, new_contact_df], ignore_index=True)
        merged_df.to_csv(self.file_name, index=False)
        self.lock.release()

    def update_contact(self, row_index, contact):
        """
        This function updates the contact directory based on row number selected
        as well as add  new information provided by the user and stores it in
        csv file.

        :param row_index: int()
            desc: Row number selection by the user.
            Example:
                row_index: 5

        :param contact: dict()
            desc: Updated information provided by the user.
            Example:
                contact = {'name': 'Jhon', lname: 'tim', 'phone': '129665'}
        """

        self.lock.acquire()
        df = pd.read_csv(self.file_name, dtype={"phone": str})
        df.loc[row_index] = contact
        df.to_csv(self.file_name, index=False)
        self.lock.release()


    def delete_contact(self, indexes):
        """
        This function deletes the row selected by user.

        :param indexes: list()
            desc: List of rows(row indexes) selected by the user
            Example:
                indexes = [0,1,2]

        """
        self.lock.acquire()
        df = pd.read_csv(self.file_name, dtype={"phone": str})
        indexes = list(map(int, indexes))
        df = df.drop(indexes)
        df.to_csv(self.file_name, index=False)
        self.lock.release()


    def display_all_contacts(self):
        """This function displays all the contacts of contact directory."""

        df = pd.read_csv(self.file_name, dtype={"phone": str})
        table = tabulate(df.head(50), headers="keys", tablefmt="fancy_grid")
        print(table)



