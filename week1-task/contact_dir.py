import time
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
        df = pd.read_csv(
            'contact.csv',
            dtype={'fname': str, 'lname': str, 'phone': str, 'org': str}
        )
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

        df = pd.read_csv(self.file_name)
        new_row = {k: [v] for k, v in contact.items()}
        new_contact_df = pd.DataFrame(new_row)
        merged_df = pd.concat([df, new_contact_df], ignore_index=True)
        merged_df.to_csv(self.file_name, index=False)
        self.lock.release()


    def update_contact_num(self, name, num1, num2):
        '''
        take a index and contact dict to update
        :param index: int index
        :param contact: dict

        Note: user will be assed to enter the old contact info (user may
        not enter all the fields of the old info, you will have to create a
        prompt without strict validations, but will have a vlidation that will
        check that atleast fname or phone is entered by the user.)
        - after the user has enter old info, use the search function to get the df
        - if contact does not exist print a appropriate error msg to user
        - if contact exits, display the contact df to user and confirm the index or
        confirm with boolean if only one row present in the df(infer the index automaticaly),
        - after confirmation take the new contact details form the user using the same propt used for insert and
        use this index to update using this fuknction.

        > sahana, '', 4567890, '', ''
         sahana, 'bn' 567890, '', ''

        update:
         Name[sahana]:
         Fname['']:
         4567890
         ''
         ''

         the propt will returen an contact dict which has old contact merged with new contact,
         the new dict and index should be passed to the updated function


        '''
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


    def delete_contact(self, indexes):
        '''
        Given an index this functio will delete the contact from the csv.
        list[index]: list on indexes
        '''
        self.lock.acquire()
        df = pd.read_csv(self.file_name)
        indexes = list(map(int, indexes))
        df = df.drop(indexes)
        df.to_csv(self.file_name, index=False)
        self.lock.release()


    def display_all_contacts(self):
        """This function displays all the contacts of contact directory."""

        df_1 = pd.read_csv(self.file_name)
        print(df_1)



