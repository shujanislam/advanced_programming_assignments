from registration_service import RegistrationService, InvalidEmailError, UnderageError

service = RegistrationService()

try:
    result = service.register_user("xzishanx100@gmailm.m", 20)
    print("Registration successful:", result)
except InvalidEmailError as error:
    print("Email error:", error)
except UnderageError as error:
    print("Age error:", error)
