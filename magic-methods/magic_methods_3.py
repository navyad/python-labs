class HomeRent:

    def __init__(self, advance):
        self.advance = advance

    def __call__(self, month_rent):
        total = self.advance
        self.advance += month_rent
        return total 


if __name__ == '__main__':
    rent = HomeRent(50000)
    print rent(10000)
    print rent(10000)
    print rent(10000)
