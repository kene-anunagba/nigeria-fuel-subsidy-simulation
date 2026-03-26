"""
Nigeria Fuel Subsidy Simulation
Name: Kene Anunagba
This is a simple python practise that simulates how an increae in fuel cost due to subsidy removal can affect an individual's income. The program calculates the remaining income before and after the subsidy removal and the loss in income due to the increase in fuel cost.
"""

if __name__ == "__main__":
    print("Nigeria fuel subsidy simulation")

#input values
monthly_income = 100000
fuel_cost_before_subsidy = 5000
fuel_increase_percentage = 170

#process
fuel_cost_after_subsidy = fuel_cost_before_subsidy * (1 + fuel_increase_percentage / 100)
new_fuel_cost = fuel_cost_after_subsidy
remaining_income_before = monthly_income - fuel_cost_before_subsidy
remaining_income_after = monthly_income - new_fuel_cost
loss_in_income = remaining_income_before - remaining_income_after

#output
print("\nresults:")
print("Monthly income:", "₦", monthly_income)
print("Fuel cost before subsidy:", "₦", fuel_cost_before_subsidy)
print("Fuel cost after subsidy:", "₦", fuel_cost_after_subsidy)
print("New fuel cost:", "₦", new_fuel_cost)
print(f"Extra fuel cost due to subsidy removal: ₦{loss_in_income}")
print("Remaining income before subsidy:", "₦", remaining_income_before)
print("Remaining income after subsidy:", "₦", remaining_income_after)
print("Loss in income:", "₦", loss_in_income)
