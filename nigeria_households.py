"""
Nigeria Fuel Subsidy Simulation - Households
Name: Kene Anunagba
This is another practice to compare how fuel subsidy removal affects different households in Nigeria. The program calculates the remaining income before and after the subsidy removal for two different households and the loss in income due to the increase in fuel cost.
"""

if __name__ == "__main__":
    print("Nigeria fuel subsidy simulation - Households")

    #policy change details
    fuel_increase_percentage = 170

    #diffeent households
    households = {
        "Household A": {
            "monthly_income": 100000,
            "fuel_cost_before_subsidy": 5000
        },
        "Household B": {
            "monthly_income": 250000,
            "fuel_cost_before_subsidy": 15000
        },
        "Household C": {
            "monthly_income": 500000,
            "fuel_cost_before_subsidy": 30000
        }
    }

    #process and output results for each household
    for household, details in households.items():
        monthly_income = details["monthly_income"]
        fuel_cost_before_subsidy = details["fuel_cost_before_subsidy"]
        fuel_cost_after_subsidy = fuel_cost_before_subsidy * (1 + fuel_increase_percentage / 100)

    #calculate remaining income and loss for each household  
        remaining_income_before = monthly_income - fuel_cost_before_subsidy
        remaining_income_after = monthly_income - fuel_cost_after_subsidy
        income_loss = remaining_income_before - remaining_income_after

    #output results for each household
        print(f"\n{household}:")
        print(f"  Monthly Income: ₦{monthly_income:,}")
        print(f"  Fuel Cost Before Subsidy Removal: ₦{fuel_cost_before_subsidy:,}")
        print(f"  Fuel Cost After Subsidy Removal: ₦{fuel_cost_after_subsidy:,.2f}")
        print(f"  Remaining Income Before: ₦{remaining_income_before:,}")
        print(f"  Remaining Income After: ₦{remaining_income_after:,.2f}")
        print(f"  Loss in Income: ₦{income_loss:,.2f}")