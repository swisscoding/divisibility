#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg

# decoration
print(stylize("\n---- | Divisibility of n and m | ----\n", fg("red")))

# class
class Divisibility:
    def __init__(self, number, divisor):
        self.number = number
        self.divisor = divisor

    # output magic method
    def __repr__(self):
        divisible = self.check_divisibility(self.number, self.divisor)
        if divisible:
            return stylize(f"\n{self.number} is divisible by {self.divisor}\n", fg("green"))
        return stylize(f"\n{self.number} is not divisible by {self.divisor}\n", fg("red"))

    # methods
    def check_divisibility(self, num, div):
        if n % m == 0:
            return True
        return False

# main execution
if __name__ == "__main__":
    # user interaction
    n = float(input("Number: "))
    m = float(input("Divisor: "))

    print(Divisibility(n, m))
