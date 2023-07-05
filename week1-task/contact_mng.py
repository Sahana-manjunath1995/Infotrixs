from configparser import ConfigParser, ExtendedInterpolation
from custom_exception import EnterValidNumber
from contact_dir import ContactDirectory


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
