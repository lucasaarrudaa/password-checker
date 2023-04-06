STATUS: WORKING

File: password_checker.py
The PasswordChecker class is a Python class that checks the strength of passwords based on provided keywords. It uses regular expressions for verification.

Usage:
Import the re module to use regular expressions.
Create an instance of the PasswordChecker class, passing two lists as arguments:
n: A list containing the passwords to be checked.
m: A list containing the keywords to check the strength of passwords.
Call the get_password_strength() method of the created instance to check the strength of passwords.
The get_password_strength() method returns a string with the strengths of passwords separated by line breaks.
The result can be used to display the strengths of passwords or for other necessary purposes.

Example Usage:
n = ["iliketoCoDe", "teaMAKEsmehappy", "abracaDabra", "pasSword", "blackcoffeelSthebest"]
m = ["coffee", "coding", "happy"]

# Create an instance of PasswordChecker class
checker = PasswordChecker(n, m)

# Get the strengths of passwords
strengths = checker.get_password_strength()

# Display the strengths of passwords
print(strengths)
