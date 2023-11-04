""" Basic example showing how to read and validate data from a file with pytdantic"""
import json
import pydantic


def main() -> None:
    """Main function"""

    with open("./data.json") as f:
        data = json.load(f)
        print(data[0])


if __name__ == "__main__":
    main()
