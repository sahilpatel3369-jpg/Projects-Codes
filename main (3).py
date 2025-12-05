
""""
Sahil. This program asks the user to input an unknown number of positive numbers. You will have a way to print out all the values and calculate the average.
"""






#Lines 12-14 is defining the function that will be used to calculate the avg of nums.

def main():
  numbers = get_values()
  print_positions(numbers)
  avg = calculate_average(numbers)
  print_list(numbers, avg)
#Lines 18- 29 is getting the values, asking user to enter positive numbers until -1 is entered to stop.
def get_values():
  number_list = []
  while True:
      num = int(input("Enter a positive number (enter -1 to stop): "))
      if num == -1:
          break
      elif num < -1:
          print("Please enter a positive number.")
      else:
          number_list.append(num)
  return number_list
#Lines 31-37 is printing numbers in list and their positions.
def print_positions(number_list):
  indices = [3, 5, 8]
  for index in indices:
      if index < len(number_list):
          print(f"Value at index {index}: {number_list[index]}")
      else:
          print(f"Index {index} does not exist in the list.")
#Line 39-44 is calculating average of numbers and returning values.
def calculate_average(number_list):
  sum_values = 0
  for num in number_list:
      sum_values += num
  average = sum_values / len(number_list)
  return average

def print_list(number_list, average):
  print("Values in the list:", end=" ")
  print(*number_list, sep=" ")
  print("Average:", average)

if __name__ == "__main__":


  main()
