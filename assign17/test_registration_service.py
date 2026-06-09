import pytest

from registration_service import (
    InvalidEmailError,
    RegistrationService,
    UnderageError,
)


@pytest.fixture
def registration_config():
    return {
        "min_age": 18,
    }


@pytest.fixture
def service(registration_config):
    return RegistrationService(**registration_config)


def test_register_user_success(service):
    result = service.register_user("user@example.com", 25)

    assert result is True


def test_register_user_success_at_age_boundary(service):
    result = service.register_user("new.user+test@example.co.uk", 18)

    assert result is True


@pytest.mark.parametrize(
    "bad_email",
    [
        None,
        "",
        "   ",
        "plainaddress",
        "missing-at-symbol.com",
        "@missing-identifier.com",
        "missing-domain@",
        "missing-tld@example",
        "user@@example.com",
    ],
)
def test_register_user_raises_invalid_email_error(service, bad_email):
    with pytest.raises(InvalidEmailError) as exc_info:
        service.register_user(bad_email, 25)

    assert "Invalid email" in str(exc_info.value)


def test_register_user_raises_underage_error(service):
    with pytest.raises(UnderageError) as exc_info:
        service.register_user("teen@example.com", 17)

    assert "below the minimum age of 18" in str(exc_info.value)


def test_register_user_rejects_non_integer_age(service):
    with pytest.raises(TypeError):
        service.register_user("user@example.com", "18")


def test_service_rejects_invalid_min_age_configuration():
    with pytest.raises(ValueError, match="Minimum age cannot be negative"):
        RegistrationService(min_age=-1)


def test_register_user_asserts_service_invariant(service):
    object.__setattr__(service, "_email_pattern", None)

    with pytest.raises(AssertionError, match="email pattern is missing"):
        service.register_user("user@example.com", 25)
