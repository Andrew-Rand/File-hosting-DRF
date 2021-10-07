from django.core.exceptions import ValidationError
from re import match


MIN_AGE = 5
MAX_AGE = 110


def validate_age(value: int) -> None:
    if value < MIN_AGE:
        raise ValidationError(f'Min age is {MIN_AGE}, sorry, you are too young')
    if value > MAX_AGE:
        raise ValidationError(f'Max age is {MAX_AGE}, but you have a great health!')


def validate_name(value: str) -> None:
    reg_ex = r'^[a-zA-z]+$'
    if not match(reg_ex, value):
        raise ValidationError(f'{value} is not a name, please use only A-z letters')


def validate_password(value: str) -> None:
    reg_ex = r'/(?=.*[0-9])(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*]{10,}/g'
    """ (?=.*[0-9]) - contains at least one number;
        (?=.*[!@#$%^&*]) - contains at least one spec char;
        (?=.*[a-z]) - contains at least one lowercase Latin letter;
        (?=.*[A-Z]) - contains at least one uppercase Latin letter;
        [0-9a-zA-Z!@#$%^&*]{10,} - contains at least 10 of all this symbols.
    """
    if not match(reg_ex, value):
        raise ValidationError(f'{value} must be 8 and contains at least'
                              f' number, lowercase and upper case, spec char')
