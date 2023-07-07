import time
import pandas as pd
from filelock import FileLock


class ContactDirectory:
    """This is class for Contact Management system"""

    def __init__(self, file):
        self.file_name = file
        lockfile = self.file_name+".lock"
        self.lock = FileLock(lockfile)

    def get_contact(self, index):
        df = pd.read_csv('contact.csv', dtype={'phone': str})
        return df.T[index].dropna().to_dict()

    def search_contact_exists(self, contact):
        '''
        check if contact exists, filter only those columsn enter by user.
        :param contact: Dict{}
        :return: True False
        '''
        """This function checks if the number provided by user exists in
        contact directory.
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
        This function, given a contact will add it to the csv
        :param contact: Dict({fname:, lname:, phone:, org:, email:})
        """

        self.lock.acquire()

        df = pd.read_csv(self.file_name, dtype={"phone": str})
        new_row = {k: [v] for k, v in contact.items()}
        new_contact_df = pd.DataFrame(new_row)
        merged_df = pd.concat([df, new_contact_df], ignore_index=True)
        merged_df.to_csv(self.file_name, index=False)
        self.lock.release()


    def update_contact(self, row_index, contact):
        '''
        take a index and contact dict to update
        :param index: int index
        :param contact: dict
        '''

        self.lock.acquire()

        df = pd.read_csv(self.file_name, dtype={"phone": str})
        df.loc[row_index] = contact
        df.to_csv(self.file_name, index=False)
        self.lock.release()



    def delete_contact(self, indexes):
        '''
        Given an index this functio will delete the contact from the csv.
        list[index]: list on indexes
        '''
        self.lock.acquire()
        df = pd.read_csv(self.file_name, dtype={"phone": str})
        indexes = list(map(int, indexes))
        df = df.drop(indexes)
        df.to_csv(self.file_name, index=False)
        self.lock.release()


    def display_all_contacts(self):
        """This function displays all the contacts of contact directory."""

        df_1 = pd.read_csv(self.file_name, dtype={"phone": str})
        print(df_1)



