class Address:
    def __init__(self, street, city, zipCode):
        self.street = street
        self.city = city
        self.zipCode = zipCode

    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, street):
        if street == "":
            raise ValueError("Street cannot be empty.")
        self._street = street

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        if city == "":
            raise ValueError("City cannot be empty.")
        self._city = city

    @property
    def zipCode(self):
        return self._zipCode

    @zipCode.setter
    def zipCode(self, zipCode):
        if zipCode == "":
            raise ValueError("Zip code cannot be empty.")
        self._zipCode = zipCode

    def display(self):
        print("Street:", self.street)
        print("City:", self.city)
        print("Zip Code:", self.zipCode)


class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.courses = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("Name cannot be empty.")
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age <= 0:
            raise ValueError("Age must be greater than 0.")
        if age < 16:
            raise ValueError("Student age must be at least 16.")
        self._age = age

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        if not isinstance(address, Address):
            raise ValueError("Address must be an Address object.")
        self._address = address

    @property
    def courses(self):
        return self._courses

    @courses.setter
    def courses(self, courses):
        if not isinstance(courses, list):
            raise ValueError("Courses must be a list.")
        self._courses = courses

    def add_course(self, course):
        if course == "":
            raise ValueError("Course name cannot be empty.")
        self.courses.append(course)

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

        print("Address:")
        self.address.display()

        print("Courses:", self.courses)


class ScholarshipStudent(Student):
    def __init__(self, name, age, address, scholarshipAmount):
        super().__init__(name, age, address)
        self.scholarshipAmount = scholarshipAmount

    @property
    def scholarshipAmount(self):
        return self._scholarshipAmount

    @scholarshipAmount.setter
    def scholarshipAmount(self, scholarshipAmount):
        if scholarshipAmount < 0:
            raise ValueError("Scholarship amount cannot be negative.")
        self._scholarshipAmount = scholarshipAmount

    def display(self):
        super().display()
        print("Scholarship Amount:", self.scholarshipAmount)


try:
    students = []

    print("===== Student System =====")
    print("1. Normal Student")
    print("2. Scholarship Student")

    choice = int(input("Enter student type: "))

    print("\nEnter Student Details")
    name = input("Enter name: ")
    age = int(input("Enter age: "))

    print("\nEnter Address Details")
    street = input("Enter street: ")
    city = input("Enter city: ")
    zipCode = input("Enter zip code: ")

    address = Address(street, city, zipCode)

    if choice == 1:
        student = Student(name, age, address)

    elif choice == 2:
        scholarshipAmount = float(input("Enter scholarship amount: "))
        student = ScholarshipStudent(name, age, address, scholarshipAmount)

    else:
        raise ValueError("Invalid student type.")

    numberOfCourses = int(input("\nHow many courses do you want to add? "))

    for i in range(numberOfCourses):
        course = input("Enter course name: ")
        student.add_course(course)

    students.append(student)

    print("\n===== Student Details =====")

    for s in students:
        s.display()
        print()

    # Showing mutable behavior
    print("Adding one more course to show list update...")
    newCourse = input("Enter another course: ")
    student.add_course(newCourse)

    print("\n===== Updated Student Details =====")
    student.display()

except ValueError as e:
    print("Error:", e)
