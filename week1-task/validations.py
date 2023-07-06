import re
import inquirer

def phone_validation(answers, current):
    # if current == '':
    #     return True
    if not re.match(r"\+?\d[\d ]+\d", current):
        raise inquirer.errors.ValidationError("", reason="Invalid Phone Number!")

    return True

def fname_validation(answers, current):

    if not re.match(r".+", current):
        raise inquirer.errors.ValidationError("", reason="Invalid Name!")

    return True

def lname_validation(answers, current):

    if not re.match(r".*", current):
        raise inquirer.errors.ValidationError("", reason="Invalid Name!")

    return True



