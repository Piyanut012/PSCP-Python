"""Password"""

import hashlib
def main():
    """Input"""
    password = input().encode('utf-8')
    print(hashlib.sha512(password).hexdigest().upper())
main()
