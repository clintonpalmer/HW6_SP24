#region imports
from Rankine_stem import rankine, steam
#endregion


def run_rankine_cycle():
    '''
    Interactively configures and analyzes a Rankine cycle based on user inputs.

    The function prompts the user to define a Rankine cycle by specifying
    the high and low pressure limits. The user is then asked whether they have
    a specific high temperature (T_high) for the superheated steam at the turbine inlet.

    If the user has a specific T_high:
      - The user can specify T_high directly or provide a multiplier to calculate
        T_high based on the saturation temperature at the high pressure (T_sat).
      - If choosing to specify directly, the user inputs the value of T_high in degrees Celsius.
      - If opting for the multiplier, the user provides a factor that multiplies T_sat
        to determine T_high. T_sat is calculated using the steam properties at the
        provided high pressure with quality x=1 (saturated steam).

    If the user does not specify T_high, the cycle is assumed to use saturated vapor
    at the turbine inlet, corresponding to the saturated conditions at p_high.

    After gathering inputs, the function instantiates a Rankine cycle object with
    the specified parameters and calculates its efficiency. A summary of the cycle's
    efficiency and state properties is then printed.

    No arguments are required for this function as it sources all necessary data
    interactively from the user.

    :return: None
    '''
    # Gather user inputs for the high and low pressures of the cycle.
    p_high = float(input("Enter the high pressure (p_high) in kPa for the Rankine cycle: "))
    p_low = float(input("Enter the low pressure (p_low) in kPa for the Rankine cycle: "))

    # Ask if the user has a specific high temperature for the turbine inlet.
    has_t_high = input("Do you have a specific temperature or T_sat multiplier to enter? (y/n): ").strip().lower()

    if has_t_high == 'y':
        # Find out if the user will input a specific temperature or use a multiplier.
        temp_choice = input(
            "Enter 's' to provide a specific T_high or 'm' to use a multiplier for T_sat: ").strip().lower()

        if temp_choice == 's':
            # User provides a specific T_high.
            T_high = float(input("Enter the specific temperature (T_high) in degrees C: "))
            print("Summary for Rankine Cycle with User-Specified T_high:")
            rankine_cycle = rankine(p_low=p_low, p_high=p_high, t_high=T_high,
                                    name='Rankine Cycle with Specific T_high')

        elif temp_choice == 'm':
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

    elif has_t_high == 'n':
        # Proceed without specifying T_high; assume saturated vapor at turbine inlet.
        print("Summary for Rankine Cycle with Saturated Vapor:")
        rankine_cycle = rankine(p_low=p_low, p_high=p_high, name='Rankine Cycle with Saturated Vapor')

    else:
        print("Invalid input for T_high presence. The program will exit.")
        return

    # Calculate the efficiency and print the summary for the cycle.
    rankine_cycle.calc_efficiency()
    rankine_cycle.print_summary()


def main():
    '''
    This program uses the Rankine class from the Rankine_stem and steam from Steam_stem to analyze different Rankine
    power cycles.
    It assumes that the turbine and pump act isentropically.

    Calculates the cycle efficiencies and output a report for each cycle based on user inputs.


    :return: None
    '''
    while True:
        run_rankine_cycle()

        # Ask the user if they want to analyze another cycle.
        another_cycle = input("Do you want to analyze another Rankine cycle? (y/n): ").strip().lower()
        if another_cycle != 'y':
            break


# region function calls
if __name__ == "__main__":
    main()
# endregion
