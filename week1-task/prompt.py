import inquirer
from validations import Validations
from inquirer.themes import Default


THEME = Default()

def user_choice_prompt():
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
    ques = [
        inquirer.Confirm("confirmation", message=msg),
    ]
    answers = inquirer.prompt(ques, theme=THEME)
    return answers['confirmation']


def update_prompt(msg, choices):

    questions = [
        inquirer.List("selected", message=msg,
                      choices=choices)
    ]
    choice = inquirer.prompt(questions, theme=THEME)['selected']

    return choice


def confirm_delete_contact():
    ques = [
        inquirer.Confirm("Delete contact", message="Do you want to delete the Contact information?"),
    ]
    answers = inquirer.prompt(ques, theme=THEME)
    return answers


def checkbox_prompt(msg, choices):
    questions = [
        inquirer.Checkbox(
            "interests",
            message=msg,
            choices=choices,
        ),
    ]

    return inquirer.prompt(questions, theme=THEME)['interests']



# if __name__ == '__main__':
    # selected_choice_num = user_choice_prompt()
    # print(selected_choice_num)

    # info = all_info_prompt('Enter the Old contact info.')
    # print(info)
    # c = confirm_add_contact()
    # print(c)
    # d = update_prompt('Enter the info')
