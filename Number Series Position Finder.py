#TASK 1
'''Write a Program for ending the series at the number where the last digit falls at
 the position provided by the user’s input'''

def print_number_series(n):
    result = ""
    num = 1
    while len(result) < n:
        result = result + str(num)
        num = num + 1
    print(result)
    
    print(f"The digit at position {n} is: {result[n-1]}")

n = int(input("ENTER A NUMBER : "))
print_number_series(n)

#TASK 2
'''REVERSED'''

def find_end_position_of_number_series(series):
    position = len(series)   
    digit = series[-1]
    print(f"The digit at which the series ends (position {position}) is: {digit}")

series_input = input("Enter the number series: ")
find_end_position_of_number_series(series_input) 


 
