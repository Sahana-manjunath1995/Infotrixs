import time
from prompt import (
     all_info_prompt, get_confirmation,
     checkbox_prompt, try_again_prompt, update_prompt
)
from tabulate import tabulate


def try_again(msg):
    """
    This function is used to get the try again prompt that prompts the user
    to select the options.

    :param msg: str()s
    :return: str()
    """

    choice = try_again_prompt(msg)
    return choice


def row_info(existing_df):
    """
    This function get the row information and row indexes that is existing in
    Contact Directory.
    :param existing_df: DataFrame()
            desc: Information selected by the user

    :return: tuple()
            desc: Returns headers and list of contact information
            with their index.
    """

    indexes = existing_df.index.tolist()
    lines = existing_df.to_string().split('\n')
    heading = lines[0]
    rows = lines[1:]
    choices = []
    for x in range(len(indexes)):
        choices.append((rows[x], indexes[x]))

    return heading, choices


def insert_logic(c):
    """
    This function provides a prompt for user information and checks for contact
    existence provided by the user. Prompt for the confirmation to add
    Prompt for the confirmation to add contact will be used for both existing
    and non-existing contact information in phone directory. Based on the
    conformation prompt contact will be added.

    :param c: contact object
          desc: Contact object created for ContactDirectory class
    """

    contact = all_info_prompt('Enter the New Contact info.')
    exists, existing_df = c.search_contact_exists(contact)

    if exists:
        print('The Given Contact Already Exists!')
        print(existing_df)
        confirm = get_confirmation(
            'Do you still want to add this contact?'
        )
    else:
        confirm = get_confirmation(
            'Are you sure you would like to add this contact?'
        )

    if confirm:
        c.insert_contact_num(contact)
        print('Contact successfully added!\n')
        c.display_all_contacts()
    else:
        print("Skipping and going back to the main screen.")


def update_logic(c):
    """
   This function checks for old contact information provided by the user,
   if the old contact exists it will display the contact information. Based
   on this, user will be provided with option to select the contact that
   they want to update, after selection user will be asked to enter the new
   information. Based on the user selected row and new information entered
   by users contact details will be updated.

   :param c: contact object
         desc: Contact object created for ContactDirectory class
    """

    contact = all_info_prompt('Enter the Old information: ',
                              validation=False)

    exists, existing_df = c.search_contact_exists(contact)

    if exists:
        print('\nFollowing are the existing Contacts:\n')
        print(existing_df)
        heading, choices = row_info(existing_df)

        msg = (
            "Choose the contacts you would like to update! "
            # f"\n    {heading}"
        )
        index = update_prompt(msg, choices)
        old_contact = c.get_contact(index)
        contact = all_info_prompt('Enter the New Contact info.',old_contact,
                                  validation=False)
        c.update_contact(index, contact)
        print("Contact Updated Successfully.")
        c.display_all_contacts()
    else:
        print('Contact does not exist in the Contact Directory')


def search_logic(c):
    """
    This function provides a prompt for user information. Based on the
    user details search is conducted. If the contact exists results will be
    displayed or else it will show no contacts were found.

   :param c: contact object
         desc: Contact object created for ContactDirectory class
       """

    contact = all_info_prompt(
        'Enter Any of the following information to Search.', validation=False)
    exists, existing_df = c.search_contact_exists(contact)

    if exists:
        print('The following contact were found!\n')
        table = tabulate(existing_df.head(7), headers="keys", tablefmt="fancy_grid")
        print(table)
        time.sleep(2)
    else:
        print('No contact found with the given information!')


def delete_logic(c):
    """
     This function provides the prompt to enter the contact information. Based
     on entered contact info search is conducted
     if the contact exists check box prompt will be displayed for users to
     select the contacts that they want to delete. Selection of rows provides
     row index, based on row index contact information will  e deleted.


     :param c: contact object
           desc: Contact object created for ContactDirectory class
      """

    contact = all_info_prompt('Enter the Contact info.', validation=False)
    exists, existing_df = c.search_contact_exists(contact)
    if exists:
        heading, choices = row_info(existing_df)

        msg = (
            "Choose the contacts you would like to delete!"
            "\n[NOTE: Press -> to select, <- to unselect & Enter to submit!]"

        )
        indexes = checkbox_prompt(msg, choices)
        c.delete_contact(indexes)
        print('Contact deleted successfully')
        c.display_all_contacts()
    else:
        print('No contact found with the given information!')
