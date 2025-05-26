from math import floor
class Category:
    """A class to represent a budget category."""

    def __init__(self, name: str) -> None:
        """Initialize a budget category with a name."""
        self.name = name
        self.ledger: list[dict] = []
        self.total: float = 0.0
        self.spent: float = 0.0

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

    def get_spent(self) -> float:
        """Check the total amount spent in the budget."""
        return self.spent

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
        self.spent += amount
        return True

    def transfer(self, amount: float, destination: 'Category') -> bool:
        """Transfer an amount to another budget category, Returns if successful."""
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f'Transfer to {destination.name}')
        destination.deposit(amount, f'Transfer from {self.name}')
        return True


def create_spend_chart(categories: list[Category]) -> str:
    """Create a spend chart for the given categories."""
    names = [category.name for category in categories]
    totals = [category.get_spent() for category in categories]
    total = sum(totals)
    percentages = [floor(item / total * 10) for item in totals]
    output_string = 'Percentage spent by category\n'
    output_string += build_chart_top(percentages)
    output_string += build_chart_bottom(names)
    return output_string


def build_chart_top(percentages: list[int]) -> str:
    """Build the percentages and dashes of the chart."""
    lines = [f'{line:>3}| ' for line in range(100, -1, -10)]
    for percentage in percentages:
        for line in range(11):
            content = 'o  ' if 10 - line < percentage + 1 else '   '
            lines[line] += content
    lines.append('    -' + '---' * len(percentages))
    return '\n'.join(lines) + '\n'


def build_chart_bottom(names: list[str]) -> str:
    """Build the labels of the chart."""
    length = max(len(name) for name in names)
    lines: list = ['     ' for _ in range(length)]
    for line in range(length):
        for name in names:
            lines[line] += f'{name[line]}  ' if line < len(name) else '   '
    return '\n'.join(lines)


chart_test_1 = [
    "Percentage spent by category",
    "100|          ",
    " 90|          ",
    " 80|          ",
    " 70|          ",
    " 60| o        ",
    " 50| o        ",
    " 40| o        ",
    " 30| o        ",
    " 20| o  o     ",
    " 10| o  o  o  ",
    "  0| o  o  o  ",
    "    ----------",
    "     F  C  A  ",
    "     o  l  u  ",
    "     o  o  t  ",
    "     d  t  o  ",
    "        h     ",
    "        i     ",
    "        n     ",
    "        g     ",
]

if __name__ == "__main__":
    print('Running test 1')

    food = Category('Food')
    food.deposit(2000, 'deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(100, 'restaurant and more food for dessert')

    clothing = Category('Clothing')
    food.transfer(500, clothing)
    clothing.withdraw(10.15, 'shirt')
    clothing.withdraw(200, 'pants')

    auto = Category('Auto')
    auto.deposit(1000, 'deposit')
    auto.withdraw(150, 'wheels')
    chart_1 = create_spend_chart([food, clothing, auto]).split('\n')

    # print('\n'.join(chart_1))

    for i, line in enumerate(chart_1):
        expected = chart_test_1[i]
        if line != expected:
            print(f'{line!a}')
            print(f'{expected!a}')