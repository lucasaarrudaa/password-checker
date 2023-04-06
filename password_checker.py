import re

class PasswordChecker:
    """
    Class to check the strength of passwords based on keywords.
    """

    def __init__(self, n, m):
        """
        Initializes the PasswordChecker class.

        Args:
            n (list): List of passwords to be checked.
            m (list): List of keywords to check the strength of passwords.
        """
        self.n = n
        self.m = m

    def get_password_strength(self):
        """
        Checks the strength of passwords based on keywords.

        Returns:
            str: A string with the strengths of passwords separated by new lines.
        """
        strengths = ""  # Empty string to store the strengths of passwords
        if 1 <= len(self.n) <= 10**3 and 1 <= len(self.m) <= 10**5:
            for i in self.n:
                if 1 <= len(i) <= 20:
                    for x in self.m:
                        if 1 <= len(x) <= 20:
                            if re.findall(f'{x}', i) or re.findall(r'\d+', i) \
                                    or i.isupper() or i.islower() \
                                    or re.findall(r'.{1,6}', i):
                                t = 'weak'
                            else:
                                t = 'strong'
                    strengths += t + "\n"  # Adds the password strength as a new line in the string
        return strengths  # Returns the complete string with the strengths of passwords


# Example usage
n = ["iliketoCoDe", "teaMAKEsmehappy", "abracaDabra",
     "pasSword", "blackcoffeelSthebest"]
m = ["coffee", "coding", "happy"]

checker = PasswordChecker(n, m)
strengths = checker.get_password_strength()
print(strengths)
