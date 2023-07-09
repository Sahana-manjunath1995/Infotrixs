import sys
import time
from configparser import ConfigParser, ExtendedInterpolation
from contact_dir import ContactDirectory
from logic import insert_logic, delete_logic,  try_again, search_logic, update_logic
from prompt import user_choice_prompt


def get_config():
    """
    This function reads the config file and returns the ConfigParser object.
    :return: ConfigParser object
    """

    config = ConfigParser(interpolation=ExtendedInterpolation())
    config.read('config.ini')
    return config


if __name__ == '__main__':
    CONFIG = get_config()
    c = ContactDirectory(CONFIG['Data']['CONTACT_FILE'])
    while True:

        # User is prompted to select the option in the application
        inp1 = user_choice_prompt()

        # If the user selects 1st option contact information Contact will be added.

        if inp1 == 1:
            insert_logic(c)
            time.sleep(2)


        # If the user selects 2nd option update_logic is used to update the contact details

        elif inp1 == 2:
            while True:
                update_logic(c)
                time.sleep(2)
                choice = try_again('Update more Contacts')
                if choice == 2:
                    break

        # If the user selects 3rd option search_logic is used to search for contact details.

        elif inp1 == 3:
            while True:
                search_logic(c)
                time.sleep(2)
                choice = try_again('Search Again')
                if choice == 2:
                    break

        # If the user selects 4th option delete_logic is used to delete the contact details.

        elif inp1 == 4:
            while True:
                delete_logic(c)
                choice = try_again('Delete More Contacts')
                if choice == 2:
                    break

        # If the user selects 5th option all contact details will be displayed.

        elif inp1 == 5:
            c.display_all_contacts()
            time.sleep(6)

        # If the user selects 6th option the user will be exited from the Contact director application.

        elif inp1 == 6:
            print("*" * 120)
            print("Thank you for using Contact directory system.")
            print("*" * 120)
            sys.exit("Goodbye, have a nice day ahead!")


