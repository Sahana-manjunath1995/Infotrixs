import re
import inquirer


class Validations:
    """
    This class validates the user details provided by users
    """

    def phone_validation(self, answers, current):
        """
        This function validates the phone number entered by the user, if the
        user tries to leave it blank or tries to enter characters other than
        digits it will raise the error.
        :param answers:Dict{}
        :param current:str()
            desc: User entered details
        :return:bool()
        """

        if not re.match(r"\+?\d[\d ]+\d", current):
            raise inquirer.errors.ValidationError("", reason="Invalid Phone Number!")

        return True

    def fname_validation(self, answers, current):
        """
        This function validates the firstname entered by the user, if the
        user leaves it blank it will raise the error. Any characters for
        fname is valid.
        :param answers:Dict{}
        :param current:str()
            desc: User entered details
        :return:bool()
        """

        if not re.match(r".+", current):
            raise inquirer.errors.ValidationError("", reason="Invalid Name!")

        return True



