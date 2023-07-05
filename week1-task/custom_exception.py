class ContactAlreadyExists(Exception):
    """This exception is raised when a user try to insert the existing
    contact details in the Contact Directory.
    """


class ContactNotfound(Exception):
    """This exception is raised when a user tries to update non-existing
    contact details in the Contact Directory.
    """


class ContactInfoUnFound(Exception):
    """This exception is raised when a user tries to search non-existing
    contact details in the Contact Directory.
    """


class EnterValidNumber(Exception):
    """This exception is raised when a user enters invalid number that is not
    present in the menu of Contact Directory Application
    """