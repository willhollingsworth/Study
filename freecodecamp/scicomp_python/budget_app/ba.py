

class Category:
    """A class to represent a budget category."""

    def __init__(self, name: str) -> None:
        """Initialize a budget category with a name."""
        self.name = name
        self.ledger: list[dict] = []
        self.total: float = 0.0

    def __str__(self) -> str:
        """Return a string representation of the budget category."""
        title = f"{self.name:*^30}\n"
        items = ''.join(
            f"{item['description'][:23]:<23}{item['amount']:>7.2f}\n"
            for item in self.ledger
        )
        total_str = f"Total: {self.total:.2f}"
        return title + items + total_str

    def get_balance(self) -> float:
        """Check the current balance of the budget."""
        return self.total

    def check_funds(self, amount: float) -> bool:
        """Check if there are sufficient funds for a withdrawal."""
        return amount <= self.get_balance()

    def deposit(self, amount: float, description: str = '') -> None:
        """Deposit an amount into the budget, creating a ledger entry."""
        self.ledger.append({'amount': amount, 'description': description})
        self.total += amount

    def withdraw(self, amount: float, description: str = '') -> bool:
        """Withdraw an amount from the budget, Returns if successful."""
        if not self.check_funds(amount):
            return False
        self.ledger.append({'amount': -amount, 'description': description})
        self.total -= amount
        return True

    def transfer(self, amount: float, destination: 'Category') -> bool:
        """Transfer an amount to another budget category, Returns if successful."""
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f'Transfer to {destination.name}')
        destination.deposit(amount, f'Transfer from {self.name}')
        return True


if __name__ == "__main__":
    print('Running tests...')
    food = Category('Food')
    food.deposit(1000, 'deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')

    clothing = Category('Clothing')
    food.transfer(50, clothing)
    print(food)
    print(clothing)
