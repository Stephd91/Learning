# Ressource : https://realpython.com/python-exceptions/
# TLDR : Here’s a quick recap of the various keywords used in Python to handle exceptions:
#  raise : allows you to trigger any exception at any time.
#  assert: enables you to verify if a certain condition is met and raise an exception if it isn’t.
#  try: executes all indented code until Python encounters an exception.
#  except: catches and handles the exceptions that Python encounters in the try clause.
#  else: lets you code sections that run only when Python encounters no exceptions in the try clause.
#  finally: enables you to execute sections of code that should always run, whether or not Python encountered an exception.

###########################################
# 1) Use specific Exceptions
###########################################
try:
    print("hello")
except ValueError:
    print("Invalid value encountered")
except IndexError:
    print("Invalid data format")
except Exception as e:
    print(f"An unexpected error occured: {e}")

###########################################
# 2) Implement error logging #####
###########################################
import logging

# configue logger
logging.basicConfig(filename="error.log", level=logging.ERROR)
try:
    # code that may raise an exception
    print("hello")
except Exception as e:
    logging.error(f"an error occured: {e}")


###########################################
# 3) Define custom Exception classes
###########################################
class CustomException(Exception):
    pass


try:
    if True:
        raise CustomException("Someting went wrong!")
except CustomException as ce:
    print("this were we handle the custom exception when happening")

###########################################
# 4) Handle Exceptions gracefully
###########################################
try:
    print("hello")
except KeyError:
    print("Catch probable errors & inform the user")
except Exception as e:
    print(f"An unexpected error occured: {e}")
else:
    # code that exceutes if no exceptions are raised
    print("world!")

###########################################
# 5) Use Finally statement for cleanup tasks
###########################################
try:
    print("hello")
except KeyError:
    print("Catch probable errors & inform the user")
except Exception as e:
    print(f"An unexpected error occured: {e}")
else:
    # code that exceutes if no exceptions are raised
    print("world!")
finally:
    # code that will always execute
    print("This is were we perform cleanup tasks")
