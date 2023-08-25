from re import search


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidSymbolsInNameError(Exception):
    pass


MIN_LENGTH = 4
VALID_DOMAINS = [".com", ".bg", ".org", ".net"]

name_pattern = r"(?P<name>\w+)(@)"
domain_pattern = r"(?P<domain>\.[a-z]+(?:\.[a-z]+)*)"
email = input()

while email != "End":
    if email.count("@") > 1:
        raise MoreThanOneAtSymbolError("Email must contain only one @ symbol!")

    elif email.count("@") < 1:
        raise MustContainAtSymbolError("Email must contain @")

    elif len(email.split("@")[0]) <= MIN_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")

    elif search(name_pattern, email) is None or search(name_pattern, email).group("name") != email.split("@")[0]:
        raise InvalidSymbolsInNameError("Name must contain letters, digits, underscores.")

    elif search(domain_pattern, email) is None or search(domain_pattern, email).group("domain") not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    else:
        print("Email is valid")

    email = input()