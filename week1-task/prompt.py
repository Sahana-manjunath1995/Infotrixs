import inquirer
from validations import Validations
from inquirer.themes import BlueComposure


THEME = BlueComposure()

def user_choice_prompt():
    """
    This function prompts the user to select the option of the user menu,
    selected option number will be returned.
    :return:int()
        desc: Selected option number
        Example:
            res = 1
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
    This function prompts the user with the option to repeat the current task
    or to go back to the main menu. If the user selects 1st option they can
    repeat the current task, and it returns the user selected option number.

    :return:int() 
        desc: Selected option number
        Example:
            res = 1
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
    This function prompts the user to provide all the contact information, and
    it will be validated based on keyword argument, it will return Contact
    details entered by the user.

    :param msg: str()
        desc: Message to be displayed in the terminal
        Example: Enter the contact details.
    :param old_value: dict()
        desc: Old contact information provided by the users to update the
              existing contact information.
        Example:
             old_value = {'name': 'Jhon', lname: 'tim', 'phone': '129665'}

    :param validation: bool() default is True
        desc: True or False
    :return: dict()
        desc: Contact information provided by the user.
        Example:
            contact_dict = {'name': 'Jhon', lname: 'tim', 'phone': '129665'}
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
    This function prompts the user to type y/N and returns bool answers.

    :param msg: str()
          desc: Message to be displayed in the terminal
          Example:
            msg = 'Are you sure of adding the contact?'
    :return: bool()
    """

    ques = [
        inquirer.Confirm("confirmation", message=msg),
    ]
    answers = inquirer.prompt(ques, theme=THEME)
    return answers['confirmation']


def update_prompt(msg, choices):
    """
    This function prompts the user to select the desired contact to be
    updated, and it returns the selected row number.

    :param msg:str()
           desc: Message to be displayed in the terminal
           Example:
                msg = 'Select the desired contacts'
    :param choices: list(tuple())
            desc: list containing row information and row index
            Example:
                choices = [(0, 'Shashi','Kumar','988254768', '', 0)]
    :return:int()
        desc: Returns row number selected by the user.
        Example
            res = 1
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
    multiple desired contacts to be deleted from the contact directory
    and returns the row index of selected option.

    :param msg:str()
           desc: Message to be displayed in the terminal
           Example:
                msg = 'Select the desired contacts that you want to delete'
    :param choices: list(tuple())
            desc: list containing row information and row index
            Example:
                choices = [(0, 'Shashi','Kumar','988254768', '' 0)]
    :return: list()
            Example:
                res = [0,1,2]
    """

    questions = [
        inquirer.Checkbox(
            "interests",
            message=msg,
            choices=choices,
        ),
    ]

    return inquirer.prompt(questions, theme=THEME)['interests']

