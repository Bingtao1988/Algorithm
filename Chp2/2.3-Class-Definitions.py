# Example
class CreditCard:
    """A consumer credit card"""

    def __init__(self, customer, bank, acnt, limit):
        """
        Create a new credit card instnace
        The initial balance is zero
        
        customer   The name of the customer
        bank       The name of the bank
        acnt       The account identifier
        limit      The credit limit
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return the name of the customer"""
        return self._customer

    def get_bank(self):
        """Return the name of the bank"""
        return self._bank

    def get_account(self):
        """Return the account identifier"""
        return self._account

    def get_limit(self):
        """Return the limit of this card"""
        return self._limit

    def get_balance(self):
        """Return the balance of this card"""
        return self._balance

    def charge(self, amount):
        """
        Charge given price to the card, assuming sufficient credit limit

        Return True if charge was processed; False if charge was denied
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += amount
            return True

    def make_payment(self, amount):
        """
        Process customer payment that reduces balance
        """
        self._balance -= amount


class Vector:
    """Represent a vector in a multidimensional space"""
    def __init__(self, d):
        """Used to initialize the Vector"""
        self._coords = [0] * d

    def __len__(self):
        """Return the length of the Vector"""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth of the dimension"""
        return self._coords[j]

    def __setitem__(self, j, value):
        """Set jth of the dimension to be value"""
        self._coords[j] = value

    def __add__(self, other):
        if len(other) != len(self):
            raise ValueError('Dimension length should be same length')
        else:
            result = Vector(len(other))
            for indexNum in range(len(other)):
                result[indexNum] = self[indexNum] + other[indexNum]
            return result
    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords
    def __ne__(self, other):
        """Return True if vector differes from others."""
        return not self.coords == other._coords
    def __str__(self):
        """Produce string representation of vector"""
        return '<' + str(self._coords)[1:-1] + ">"


