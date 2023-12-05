'''
Question2:- Using the following list: 

provinces = ['Prince Edward Island', 'Newfoundland And Labrador','Nova Scotia','New Brunswick','Quebec','Ontario','Manitoba','Saskatchewan','Alberta','British Columbia','Nunavut','Northwest Territories','Yukon']
Create a binary search that will ask the user for one of the provinces in Canada 
and then using the binary search will look for the province - display the number of searches it took to find the value.
'''

# Program- Binary Search Program
# Purpose- Created the list and use binary search algorithm
# Name- Saurabh Chawla
# Date- 1 December 2023

# Created the list 
import random  
provinces = ['Prince Edward Island', 'Newfoundland And Labrador','Nova Scotia','New Brunswick','Quebec','Ontario','Manitoba','Saskatchewan','Alberta','British Columbia','Nunavut','Northwest Territories','Yukon']
provinces.sort()

# Ask the user input to enter a province
look_for = input("Enter a province in Canada: ").strip().title()
# Use binary Search algorithm
start = 0
end = len(provinces) - 1
num_searches = 1

while end >= start:
    mid = (end + start) // 2

    if provinces[mid] < look_for:
        num_searches += 1
        start = mid + 1
    elif provinces[mid] > look_for:
        num_searches += 1
        end = mid - 1
    else:
        print(f'Found the province {look_for} after {num_searches} searches.')
        break

# Thank the user
print('Thank you for using our program. ')
