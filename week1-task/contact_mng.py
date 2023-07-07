import sys
import time
from configparser import ConfigParser, ExtendedInterpolation
from contact_dir import ContactDirectory
from logic import insert_logic, delete_logic,  try_again, search_logic, update_logic
from prompt import user_choice_prompt


def get_config():

    config = ConfigParser(interpolation=ExtendedInterpolation())
    config.read('config.ini')
    return config


if __name__ == '__main__':
    CONFIG = get_config()
    print(CONFIG['Data']['CONTACT_FILE'])
    c = ContactDirectory(CONFIG['Data']['CONTACT_FILE'])
    while True:
        inp1 = user_choice_prompt()

        if inp1 == 1:
            insert_logic(c)
            time.sleep(2)

        elif inp1 == 2:
            while True:
                update_logic(c)
                time.sleep(2)
                choice = try_again('Update more Contacts')
                if choice == 2:
                    break

        elif inp1 == 3:
            while True:
                search_logic(c)
                time.sleep(2)
                choice = try_again('Search Again')
                if choice == 2:
                    break


        elif inp1 == 4:
            while True:
                delete_logic(c)
                choice = try_again('Delete More Contacts')
                if choice == 2:
                    break


        elif inp1 == 5:
            c.display_all_contacts()

        elif inp1 == 6:
            print("*" * 120)
            print("Thank you for using Contact directory system.")
            print("*" * 120)
            sys.exit("Goodbye, have a nice day ahead!")


