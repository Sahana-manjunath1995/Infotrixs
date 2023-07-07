import re
import inquirer


class Validations:

    def phone_validation(self, answers, current):
        if not re.match(r"\+?\d[\d ]+\d", current):
            raise inquirer.errors.ValidationError("", reason="Invalid Phone Number!")

        return True

    def fname_validation(self, answers, current):
        if not re.match(r".+", current):
            raise inquirer.errors.ValidationError("", reason="Invalid Name!")

        return True



