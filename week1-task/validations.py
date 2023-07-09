import re
import inquirer


class Validations:
    """
    This class validates the user's contact information provided by the users.
    """

    def phone_validation(self, answers, current):
        """
        This function validates the phone number entered by the user, if the
        user leaves the phone number field blank or enter characters other than
        digits it will raise the error. If the user provides digits it will
        return True.

        :param answers:dict()
        :param current:str()
            desc: User entered details
            Example:
                current = '9880949899'
        :return:bool()
        """

        if not re.match(r"\+?\d[\d ]+\d", current):
            raise inquirer.errors.ValidationError("", reason="Invalid Phone Number!")

        return True

    def fname_validation(self, answers, current):
        """
        This function validates the firstname entered by the user, if the
        user leaves the first name field blank it will raise the error. If the
        user provides data it will return True.

        :param answers:dict()
        :param current:str()
            desc: User entered details
            Example:
                current = 'sahana'
        :return: bool()
        """

        if not re.match(r".+", current):
            raise inquirer.errors.ValidationError("", reason="Invalid Name!")

        return True



