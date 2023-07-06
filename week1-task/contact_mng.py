import sys
import time
import inquirer
from configparser import ConfigParser, ExtendedInterpolation

from contact_dir import ContactDirectory
from custom_exception import EnterValidNumber, ContactAlreadyExists
from prompt import (
    user_choice_prompt, all_info_prompt, confirm_add_contact,
    confirm_delete_contact,  checkbox_prompt, try_again_prompt
)



def get_val():
    """This function returns input values for contact directory."""

    # name = input('Please enter the contact name:')
    # num = int(input('Please enter the contact number:'))
    # org = input('Please enter the organization name:')
    inp = [
        inquirer.Text("name", message="What's your name?"),
        inquirer.Text("num", message="What's your Contact number, {name}?"),
        inquirer.Text(
            "org",
            message="What is the name of your company, {name}?",
        ),
    ]
    inpt_val = inquirer.prompt(inp)
    val = [v for k, v in inpt_val.items()]
    print(val)
    return val

def get_config():

    config = ConfigParser(interpolation=ExtendedInterpolation())
    config.read('config.ini')
    return config


def delete_logic(c):
    contact = all_info_prompt('Enter the Contact info.', validation=False)
    exists, existing_df = c.search_contact_exists(contact)
    if exists:
        indexes = existing_df.index.tolist()
        lines = existing_df.to_string().split('\n')
        heading = lines[0]
        rows = lines[1:]
        choices = []
        for x in range(len(indexes)):
            choices.append((rows[x], indexes[x]))

        msg = (
            "Choose the contacts you would like to delete! \n"
            "[NOTE: Press -> to select, <- to unselect & Enter to submit!]\n"
            f"      {heading}"
        )
        indexes = checkbox_prompt(msg, choices)
        c.delete_contact(indexes)
    else:
        print('No contact found with the given information!')


if __name__ == '__main__':
    CONFIG = get_config()
    print(CONFIG['Data']['CONTACT_FILE'])
    c = ContactDirectory(CONFIG['Data']['CONTACT_FILE'])
    while True:

        inp1 = user_choice_prompt()

        if inp1 == 1:
            contact = all_info_prompt('Enter the New Contact info.')
            exists, existing_df = c.search_contact_exists(contact)

            if exists:
                print('The Given Contact Already Exists!')
                print(existing_df)
                confirm = confirm_add_contact(
                    'Do you still want to add this contact?'
                )
            else:
                confirm = confirm_add_contact(
                    'Are you sure you would like to add this contact?'
                )

            if confirm:
                c.insert_contact_num(contact)
                print('Contact successfully added!\n')
            else:
                print("Skipping and going back to the main screen.")
            time.sleep(2)


        elif inp1 == 2:

            inp_name = input('Please enter the contact name:')
            inp_num1 = int(input('Please enter the previous contact number:'))
            inp_num2 = int(input('Please enter the present number:'))
            c.update_contact_num(inp_name, inp_num1, inp_num2)

        elif inp1 == 3:
            while True:
                contact = all_info_prompt('Enter Any of the following information to Search.', validation=False)
                exists, existing_df = c.search_contact_exists(contact)

                if exists:
                    print('The following contact were found!')
                    print(existing_df)
                else:
                    print('No contact found with the given information!')
                time.sleep(2)
                choice = try_again_prompt('Search Again')
                if choice == 2:
                    break


        elif inp1 == 4:
            while True:
                delete_logic(c)
                choice = try_again_prompt('Delete More Contacts')
                if choice == 2:
                    break




        elif inp1 == 5:
            c.display_all_contacts()

        elif inp1 == 6:
            print("*" * 120)
            print("Thank you for using Contact directory system.")
            print("*" * 120)
            sys.exit("Goodbye, have a nice day ahead!")

        else:
            raise EnterValidNumber('Please enter valid number')
