import re
from dataclasses import dataclass, field
from typing import Pattern


class InvalidEmailError(ValueError):
    """Raised when an email address is missing or has an invalid format."""

    def __init__(self, email: object, reason: str):
        self.email = email
        self.reason = reason
        super().__init__(f"Invalid email {email!r}: {reason}")


class UnderageError(PermissionError):
    """Raised when a user does not meet the minimum age requirement."""

    def __init__(self, age: int, minimum_age: int):
        self.age = age
        self.minimum_age = minimum_age
        super().__init__(
            f"Registration denied: applicant age {age} is below the minimum age of {minimum_age}."
        )


@dataclass(frozen=True)
class RegistrationService:
    min_age: int = 18
    email_regex: str = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    _email_pattern: Pattern[str] = field(init=False, repr=False)

    def __post_init__(self) -> None:
        if self.min_age < 0:
            raise ValueError("Minimum age cannot be negative.")

        object.__setattr__(self, "_email_pattern", re.compile(self.email_regex))

    def register_user(self, email: str, age: int) -> bool:
        """
        Validate a user's email and age before registration.

        Returns:
            True if registration data is valid.

        Raises:
            InvalidEmailError: If the email is missing, empty, or malformed.
            UnderageError: If the applicant is younger than the minimum age.
            TypeError: If age is not an integer.
        """

        assert self.min_age >= 0, "Service invariant violated: min_age must be non-negative."
        assert self._email_pattern is not None, "Service invariant violated: email pattern is missing."

        if email is None:
            raise InvalidEmailError(email, "email cannot be null.")

        if not isinstance(email, str):
            raise InvalidEmailError(email, "email must be a string.")

        if not email.strip():
            raise InvalidEmailError(email, "email cannot be empty.")

        if not self._email_pattern.fullmatch(email):
            raise InvalidEmailError(
                email,
                "email must contain a valid identifier, '@' symbol, and domain name.",
            )

        if not isinstance(age, int) or isinstance(age, bool):
            raise TypeError(f"Age must be an integer, got {type(age).__name__}.")

        if age < self.min_age:
            raise UnderageError(age, self.min_age)

        return True
