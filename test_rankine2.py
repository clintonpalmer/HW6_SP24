from Rankine_stem import rankine, steam


def run_rankine_cycle():
    # Gather user inputs for the high and low pressures of the cycle.
    p_high = float(input("Enter the high pressure (p_high) in kPa for the Rankine cycle: "))
    p_low = float(input("Enter the low pressure (p_low) in kPa for the Rankine cycle: "))

    # Ask if the user has a specific high temperature for the turbine inlet.
    has_t_high = input("Do you have a specific temperature for T_high? (yes/no): ").strip().lower()

    if has_t_high == 'yes':
        # Find out if the user will input a specific temperature or use a multiplier.
        temp_choice = input(
            "Enter 'specific' to provide a specific T_high or 'multiplier' to use a multiplier for T_sat: ").strip().lower()

        if temp_choice == 'specific':
            # User provides a specific T_high.
            T_high = float(input("Enter the specific temperature (T_high) in degrees C: "))
            print("Summary for Rankine Cycle with User-Specified T_high:")
            rankine_cycle = rankine(p_low=p_low, p_high=p_high, t_high=T_high,
                                    name='Rankine Cycle with Specific T_high')

        elif temp_choice == 'multiplier':
            # User provides a multiplier for T_sat to determine T_high.
            multiplier = float(input("Enter the multiplier to apply to T_sat for T_high: "))
            saturated_steam = steam(p_high, x=1)
            saturated_steam.calc()
            T_high = multiplier * saturated_steam.T
            print("Summary for Rankine Cycle with T_high Based on T_sat Multiplier:")
            rankine_cycle = rankine(p_low=p_low, p_high=p_high, t_high=T_high,
                                    name='Rankine Cycle with T_sat Multiplier')

        else:
            print("Invalid temperature choice. The program will exit.")
            return

    elif has_t_high == 'no':
        # Proceed without specifying T_high; assume saturated vapor at turbine inlet.
        print("Summary for Rankine Cycle with Saturated Vapor:")
        rankine_cycle = rankine(p_low=p_low, p_high=p_high, name='Rankine Cycle with Saturated Vapor')

    else:
        print("Invalid input for T_high presence. The program will exit.")
        return

    # Calculate the efficiency and print the summary for the cycle.
    rankine_cycle.calc_efficiency()
    rankine_cycle.print_summary()


def run_rankine_cycles():
    while True:
        run_rankine_cycle()

        # Ask the user if they want to analyze another cycle.
        another_cycle = input("Do you want to analyze another Rankine cycle? (yes/no): ").strip().lower()
        if another_cycle != 'yes':
            break


# Execute the function when the script is run directly.
if __name__ == "__main__":
    run_rankine_cycles()
