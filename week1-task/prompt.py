import re
import inquirer
from validations import fname_validation, lname_validation, phone_validation


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
    choice = inquirer.prompt(questions)
    return int(choice['selected'].split('.')[0])


def try_again_prompt(msg):
    choices = [
        f'1. {msg}',
        '2. Go to main screen'
    ]
    questions = [
        inquirer.List("selected", message='Please select an option: ', choices=choices)
    ]
    choice = inquirer.prompt(questions)
    return int(choice['selected'].split('.')[0])


def all_info_prompt(msg, validation=True):
    print(msg)
    inp = [
        inquirer.Text("fname", message="First Name",
                      validate=fname_validation if validation else True),
        inquirer.Text("lname", message="Last Name",
                      validate=lname_validation if validation else True),
        inquirer.Text("phone", message="Phone",
                      validate=phone_validation if validation else True),
        inquirer.Text("org", message="Organization", default=None)
    ]
    return inquirer.prompt(inp)

def confirm_add_contact(msg):
    ques = [
        inquirer.Confirm("confirmation", message=msg),
    ]
    answers = inquirer.prompt(ques)
    return answers['confirmation']


def update_prompt(msg):
    print(msg)
    inp = [
        inquirer.Text("fname", message="First Name", validate=update_fname_validation),
        inquirer.Text("lname", message="Last Name"),
        inquirer.Text("phone", message="Phone", validate=update_phone_validation),
        inquirer.Text("org", message="Organization", default=None)
    ]
    answer = inquirer.prompt(inp)
    return answer

def confirm_delete_contact():
    ques = [
        inquirer.Confirm("Delete contact", message="Do you want to delete the Contact information?"),
    ]
    answers = inquirer.prompt(ques)
    return answers


def checkbox_prompt(msg, choices):
    questions = [
        inquirer.Checkbox(
            "interests",
            message=msg,
            choices=choices,
        ),
    ]
    return inquirer.prompt(questions)['interests']



if __name__ == '__main__':
    # selected_choice_num = user_choice_prompt()
    # print(selected_choice_num)

    # info = all_info_prompt('Enter the Old contact info.')
    # print(info)
    # c = confirm_add_contact()
    # print(c)
    d = update_prompt('Enter the info')
