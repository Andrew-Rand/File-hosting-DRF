import pytest
from django.core.exceptions import ValidationError

from src.accounts.validators import validate_age, validate_name, validate_password


class TestValidateAge:

    def test_validate_age_if_valid(self) -> None:

        assert validate_age(value=5) is None
        assert validate_age(value=40) is None
        assert validate_age(value=110) is None

    def test_validate_age_if_out_of_range(self) -> None:

        with pytest.raises(ValidationError):
            validate_age(value=4)
            validate_age(value=111)


class TestValidateName:

    def test_validate_name_if_valid(self) -> None:

        assert validate_name(value='test') is None
        assert validate_name(value='Andrew') is None
        assert validate_name(value='Dana') is None
        assert validate_name(value='Igor') is None
        assert validate_name(value='Oleg') is None

    def test_validate_name_if_incorrect_name(self) -> None:

        with pytest.raises(ValidationError):
            validate_name(value='&&&')
            validate_name(value='151354')
            validate_name(value='')


class TestValidatePassword:

    def test_validate_password_if_valid(self) -> None:

        assert validate_password(value='1234Abc%%%') is None
        assert validate_password(value='0Dc%0Dc%00') is None

    def test_validate_password_if_incorrect(self) -> None:

        with pytest.raises(ValidationError):
            validate_password('password')
            validate_password('Ab1%')
            validate_password('1234')
