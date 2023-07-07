import time
from prompt import (
     all_info_prompt,
    get_confirmation,  checkbox_prompt, try_again_prompt, update_prompt
)


def try_again(msg):
    choice = try_again_prompt(msg)
    return choice


def row_info(existing_df):
    indexes = existing_df.index.tolist()
    lines = existing_df.to_string().split('\n')
    heading = lines[0]
    rows = lines[1:]
    choices = []
    for x in range(len(indexes)):
        choices.append((rows[x], indexes[x]))

    return heading, choices


def insert_logic(c):
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
    else:
        print("Skipping and going back to the main screen.")


def update_logic(c):
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
        contact = all_info_prompt('Enter the New Contact info.',
                                     old_contact, validation=False)
        c.update_contact(index, contact)
        print("Contact Updated")
    else:
        print('Contact does not exist in the Contact Directory')


def search_logic(c):
    contact = all_info_prompt(
        'Enter Any of the following information to Search.', validation=False)
    exists, existing_df = c.search_contact_exists(contact)

    if exists:
        print('The following contact were found!')
        print(existing_df)
    else:
        print('No contact found with the given information!')


def delete_logic(c):
    contact = all_info_prompt('Enter the Contact info.', validation=False)
    exists, existing_df = c.search_contact_exists(contact)
    if exists:
        heading, choices = row_info(existing_df)

        msg = (
            "Choose the contacts you would like to delete! \n"
            "[NOTE: Press -> to select, <- to unselect & Enter to submit!]\n"
            f"      {heading}"
        )
        indexes = checkbox_prompt(msg, choices)
        c.delete_contact(indexes)
    else:
        print('No contact found with the given information!')
