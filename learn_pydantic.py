""" 
Basic example showing how to read and validate data from a file with pytdantic.
Source : https://www.youtube.com/watch?v=Vj-iU-8_xLs&list=PLC0nd42SBTaNuP4iB4L6SJlMaHE71FG6N&index=27
"""
import json
import pydantic
from typing import Optional, List


class ISBN10FormatError(Exception):
    """Custom error that is raised when ISBN10 does not have the right format."""

    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)


class ISBNMissingError(Exception):
    """Custome error that is raised when both isbn10 and isbn13 are missing."""

    def __init__(self, title: str, message: str) -> None:
        self.title = title
        self.message = message
        super().__init__(message)


class Book(pydantic.BaseModel):
    """Represents a book that you can read from a JSON file."""

    # class Config:
    #     """Pydantic config class"""

    #     # Make Book an immutable object
    #     allow_mutation = False
    #     anystr_lower = True

    # class Settings:
    #     """Read environment variables from some config file""

    # Define our model (from the data.json file)
    title: str
    author: str
    publisher: str
    price: float
    isbn_10: Optional[str] = pydantic.Field(frozen=True)
    isbn_13: Optional[str]
    subtitle: Optional[str] = None

    @pydantic.root_validator(pre=True)
    @classmethod
    def check_isbnb10_or_isbn13(cls, values):
        """Make sure there is either an isbn10 or isbn13 value defined."""
        if "isbn_10" not in values and "isbn_13" not in values:
            raise ISBNMissingError(
                title=values["title"],
                message="Document should have either an ISBN10 or ISBN13",
            )
        return values

    @pydantic.validator("isbn_10")
    @classmethod
    def isbn10_valid(cls, value):
        """Validator to check if isbn10 is valid."""
        chars = [c for c in value if c in "0123456789xX"]
        if len(chars) != 10:
            raise ISBN10FormatError(value=value, message="ISNB10 should be 10 digits.")

        def char_to_int(char: str) -> int:
            if char in "Xx":
                return 10
            return int(char)

        # digit sum of isbn10 should be divisable by 11
        weighted_sum = sum((10 - i) * char_to_int(x) for i, x in enumerate(chars))
        if weighted_sum % 11 != 0:
            raise ISBN10FormatError(
                value=value,
                message="ISNB10 digit weighted sum should be divisible by 11.",
            )
        return value


def main() -> None:
    """Main function"""

    # Read data from a JSON file
    with open("./data.json") as f:
        data = json.load(f)
        books_raw = [item for item in data]
        books_pydantic: List[Book] = [Book(**item) for item in data]
        print("\n ************* Basics ***************** \n")
        print("Raw data extracted without pydantic options: ", books_raw[0]["title"])
        print("Data extracted with our pydantic model: ", books_pydantic[0].title)
        print("\n ************** Data transformation **************** \n")
        books_pydantic[0].title = "New title"
        print("Changed title: ", books_pydantic[0].title)
        print("\n ************** Data serialization **************** \n")
        # Transform our Book object into a python dictionary.
        # We can use include or exclude arguments to take what we want from the object
        print(books_pydantic[0].model_dump(include="author"))
        copy_book = books_pydantic[0].model_copy()
        print(copy_book)


if __name__ == "__main__":
    main()
