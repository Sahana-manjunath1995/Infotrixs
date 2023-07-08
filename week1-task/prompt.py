import inquirer
from validations import Validations
from inquirer.themes import BlueComposure


THEME = BlueComposure()

def user_choice_prompt():
    """
    This function prompts the user to select the option of user menu,
    selected option number will be returned
    :return:int()
     desc: Selected option number
    """
    choices = [
        '1. Add Contact',
        '2. Edit the existing contact',
        '3. Search the Contact details',
        '4. Delete the Contact details',
        '5. Display all the Contact details',
        '6. Exit the Contact directory'
    ]
    questions = [
        inquirer.List("selected", message='Please select the option: ', choices=choices)
    ]
    choice = inquirer.prompt(questions, theme=THEME)
    return int(choice['selected'].split('.')[0])


def try_again_prompt(msg):
    """
    This function prompts the user with option to repeat the same tasks
    or to go back to the main menu. If the user select 1 option they can
    repeat the same task. It returns the selected user option number.

    :return:int()
     desc: Selected option number
    """

    choices = [
        f'1. {msg}',
        '2. Go to main screen'
    ]
    questions = [
        inquirer.List("selected", message='Please select an option: ', choices=choices)
    ]
    choice = inquirer.prompt(questions, theme=THEME)
    return int(choice['selected'].split('.')[0])


def all_info_prompt(msg, old_value={}, validation=True):
    """
    This function prompts the user to provide contact information, and
    it will be validated based on keyword argument, it will return Contact
    details entered by the user.

    :param msg:str()
           desc: Message to be displayed in the terminal
    :param old_value:Dict()
            desc: Old contacts provided by the users while updating the
            contact info
    :param validation:bool()
            desc: Provide it with True or False
    :return:
    """

    print(msg)
    v = Validations()
    inp = [
        inquirer.Text("fname", message="First Name", default=old_value.get('fname', None),
                      validate=v.fname_validation if validation else True),
        inquirer.Text("lname", message="Last Name", default=old_value.get('lname', None)),
        inquirer.Text("phone", message="Phone", default=old_value.get('phone', None),
                      validate=v.phone_validation if validation else True),
        inquirer.Text("org", message="Organization", default=old_value.get('org', None),)
    ]
    res = inquirer.prompt(inp, theme=THEME)


    return res

def get_confirmation(msg):
    """
    This function prompts the user to type y/N and returns bool answers
    :param msg:str()
          desc: Message to be displayed in the terminal
    :return: bool()
    """
    ques = [
        inquirer.Confirm("confirmation", message=msg),
    ]
    answers = inquirer.prompt(ques, theme=THEME)
    return answers['confirmation']


def update_prompt(msg, choices):
    """
    This function prompts the user to select the contact that they want to
    update, and it returns the selected row number.

    :param msg:str()
           desc: Message to be displayed in the terminal
    :param choices: list()
            desc: list containing row information and row index
    :return:int()
        desc: Returns row number selected by the user.
    """

    questions = [
        inquirer.List("selected", message=msg,
                      choices=choices)
    ]
    choice = inquirer.prompt(questions, theme=THEME)['selected']

    return choice


def checkbox_prompt(msg, choices):
    """
    This function provides checkbox prompt to the user to select the
    multiple contacts that they want to delete from their contact directory
    and returns row index
    """

    questions = [
        inquirer.Checkbox(
            "interests",
            message=msg,
            choices=choices,
        ),
    ]

    return inquirer.prompt(questions, theme=THEME)['interests']

# def confirm_delete_contact():
#
#     ques = [
#         inquirer.Confirm("Delete contact", message="Do you want to delete the Contact information?"),
#     ]
#     answers = inquirer.prompt(ques, theme=THEME)
#     return answers



# if __name__ == '__main__':
    # selected_choice_num = user_choice_prompt()
    # print(selected_choice_num)

    # info = all_info_prompt('Enter the Old contact info.')
    # print(info)
    # c = confirm_add_contact()
    # print(c)
    # d = update_prompt('Enter the info')
