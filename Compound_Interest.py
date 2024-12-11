print("Compound Interest Calculator!!!")


def calculate_compound_interest(amount, interest, years, dp):
    deposit = amount

    for year in range(1, years + 1):
        calc = deposit * (interest / 100)
        intr = calc + deposit
        deposit = intr
        print(f"Year {year} : £{deposit:.{dp}f}")

    return deposit


def calculate_compound_interest_intervals(amount, intervals, dp):
    deposit = amount

    for interval in range(1, intervals + 1):
        print(f"\n For Interval {interval} ---> ")
        no_of_years = int(input(f"How many years for Interval {interval} : "))
        am_of_intr = float(
            input(f"What is the interest rate (in %) for Interval {interval}? ")
        )

        for year in range(1, no_of_years + 1):
            calc = deposit * (am_of_intr / 100)
            com_int = calc + deposit
            deposit = com_int
            print(f"Year {year} : £{com_int:.{dp}f}")

    return deposit


def calculate_reverse_compound_interest(amount, interest, years, dp):
    money = amount

    for year in range(1, years + 1):
        com_int = money / (1 + (interest / 100))
        money = com_int
        print(f"Year {year} : £{money:.{dp}f}")

    return money


def main():
    option = int(
        input(
            "Choose calculation type: (1) Normal Compound Interest (2) Interval Compound Interest (3) Reverse Compound Interest: "
        )
    )

    if option == 1:
        amount = float(input("What is the Amount deposited: £"))
        years = int(input("How many years in total (ONLY DIGIT): "))
        interest = float(input("What is the interest rate (in %)? "))
        dp = int(input("Result In how many decimal place: "))
        print("\n")

        final_amount = calculate_compound_interest(amount, interest, years, dp)
        print(
            f"\nThe Final Amount at the end of {years} years is : £{final_amount:.{dp}f} \n"
        )
        print(
            f"And the Final Amount of interest is : £{(final_amount - amount):.{dp}f} \n"
        )

    elif option == 2:
        amount = float(input("What is the Amount deposited: £"))
        intervals = int(input("How many year intervals with interest change: "))
        dp = int(input("Result In how many decimal place: "))
        print("\n")

        final_amount = calculate_compound_interest_intervals(amount, intervals, dp)
        print(
            f"\nThe Final Amount at the end of all intervals is : £{final_amount:.{dp}f} \n"
        )
        print(
            f"And the Final Amount of interest is : £{(final_amount - amount):.{dp}f} \n"
        )

    elif option == 3:
        amount = float(input("What is the Final Amount: £"))
        years = int(input("How many years in total (ONLY DIGIT): "))
        interest = float(input("What is the interest rate (in %)? "))
        dp = int(input("Result In how many decimal place: "))
        print("\n")

        final_amount = calculate_reverse_compound_interest(amount, interest, years, dp)
        print(f"\nThe Amount at the beginning is : £{final_amount:.{dp}f} \n")
        print(f"With a total interest of : £{(amount - final_amount):.{dp}f} \n")

    else:
        print("Invalid Choice!!!")


main()
