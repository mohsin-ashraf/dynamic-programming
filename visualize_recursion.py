# Author: Bishal Sarang

# Import Visualiser class from module visualiser
from visualiser.visualiser import Visualiser as vs

# Add decorator
# Decorator accepts optional arguments: ignore_args , show_argument_name, show_return_value and node_properties_kwargs
@vs(node_properties_kwargs={"shape":"record", "color":"#f57542", "style":"filled", "fillcolor":"grey"})
def max_revenue(length,list_of_prices):
    if length == 0: return 0
    max_price = -1
    for i in range(0,length):
        temp_price = list_of_prices[length - i - 1] + max_revenue(i,list_of_prices)
        if temp_price > max_price:
            max_price = temp_price
    return max_price



#         1  2  3  4   5  6   7  8   9
prices = [1, 3, 5, 6, 11, 4, 13, 12, 2]
def main():
    # Call function
    print(max_revenue(5,prices))
    # Save recursion tree to a file
    vs.make_animation("fibonacci.gif", delay=1)
if __name__ == "__main__":
    main()