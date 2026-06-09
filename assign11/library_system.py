from abc import ABC, abstractmethod


class LibraryItem(ABC):
    item_count = 0   

    def __init__(self, title="Unknown", year=0):
        self.title = title
        self.year = year
        LibraryItem.item_count += 1

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if title == "":
            raise ValueError("Title cannot be empty.")
        self._title = title

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if year < 0:
            raise ValueError("Year cannot be negative.")
        self._year = year

    @abstractmethod
    def displayInfo(self):
        pass

    @staticmethod
    def getItemCount():
        return LibraryItem.item_count


class Book(LibraryItem):
    def __init__(self, title="Unknown", year=0, author="Unknown"):
        super().__init__(title, year)
        self.author = author

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if author == "":
            raise ValueError("Author cannot be empty.")
        self._author = author

    def displayInfo(self):
        print("Item Type: Book")
        print("Title:", self.title)
        print("Year:", self.year)
        print("Author:", self.author)
        print()


class DVD(LibraryItem):
    def __init__(self, title="Unknown", year=0, duration=0, genre="Unknown"):
        super().__init__(title, year)
        self.duration = duration
        self.genre = genre

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        if duration < 0:
            raise ValueError("Duration cannot be negative.")
        self._duration = duration

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        if genre == "":
            raise ValueError("Genre cannot be empty.")
        self._genre = genre

    def displayInfo(self):
        print("Item Type: DVD")
        print("Title:", self.title)
        print("Year:", self.year)
        print("Duration:", self.duration, "minutes")
        print("Genre:", self.genre)
        print()


try:
    library_items = []

    numberOfItems = int(input("How many library items do you want to add? "))

    for i in range(numberOfItems):
        print("\nChoose item type:")
        print("1. Book")
        print("2. DVD")

        choice = int(input("Enter choice: "))

        title = input("Enter title: ")
        year = int(input("Enter year: "))

        if choice == 1:
            author = input("Enter author: ")
            item = Book(title, year, author)

        elif choice == 2:
            duration = int(input("Enter duration in minutes: "))
            genre = input("Enter genre: ")
            item = DVD(title, year, duration, genre)

        else:
            raise ValueError("Invalid item type.")

        library_items.append(item)

    print("\n===== Library Items =====")

    for item in library_items:
        item.displayInfo()

    print("Total Library Items:", LibraryItem.getItemCount())

except ValueError as e:
    print("Error:", e)
