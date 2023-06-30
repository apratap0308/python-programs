# pthon program to find 
# compound interest of given number


def compound_interest(principle, rate, time):


    # calculate compound interest
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    print("compound interest is" , CI)

# Driver code
compound_interest(1000, 10.25, 5)