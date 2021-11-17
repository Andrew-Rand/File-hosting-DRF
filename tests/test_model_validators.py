import pytest
from django.core.exceptions import ValidationError

from src.accounts.validators import validate_age, validate_name, validate_password


class TestValidateAge:

    def test_validate_age_if_age_is_low_limit(self) -> None:
        assert validate_age(value=5) is None

    def test_validate_age_if_age_is_40(self) -> None:
        assert validate_age(value=40) is None

    def test_validate_age_if_age_is_up_limit(self) -> None:
        assert validate_age(value=110) is None

    def test_validate_age_if_out_of_range_low(self) -> None:

        with pytest.raises(ValidationError):
            validate_age(value=4)

    def test_validate_age_if_out_of_range_up(self) -> None:

        with pytest.raises(ValidationError):
            validate_age(value=111)


class TestValidateName:

    def test_validate_name_if_valid(self) -> None:
        assert validate_name(value='test') is None

    def test_validate_name_if_incorrect_name(self) -> None:
        with pytest.raises(ValidationError):
            validate_name(value='&&&')


class TestValidatePassword:

    def test_validate_password_if_valid(self) -> None:
        assert validate_password(value='1234Abc%%%') is None

    def test_validate_password_if_incorrect(self) -> None:
        with pytest.raises(ValidationError):
            validate_password('password')

