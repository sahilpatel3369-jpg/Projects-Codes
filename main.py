

def print_list(title, data):
    print(title)
    for i in range(0, len(data)):
        print(f'{data[i]:8.2f}', end=' ') 
     #Each value has 2 decimal places
        if (i + 1) % 8 == 0: 
          # 8 values should display from file
            print() 
          # Move to the next line after displaying 8 values
    print() 
  

def sort_list(data):
    for i in range(len(data)):
        min_idx = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]

def mean(data):
    return sum(data) / len(data)

def median(data):
    n = len(data)
    if n % 2 == 0:
        return (data[n//2 - 1] + data[n//2]) / 2
    else:
        return data[n//2]

def build_list(filename, number_list):
    infile = open(filename, 'r')
    text = infile.readline()
    while text != '':
        number_list.append(float(text)) 
      # TXT to float before appendings
        text = infile.readline()
    infile.close()
    return number_list

def main():
    filename = "progs7_nums.txt"
    unsorted_list = [] 
  #Needs an empty list for unsorted data
    unsorted_list = build_list(filename, unsorted_list)

    #Lines 50 to 53 is unsorted data list
    title = "Unsorted List"
    print_list(title, unsorted_list)

    sorted_list = unsorted_list.copy() 
  
    # ascend the list 
    sort_list(sorted_list)
    title = "Sorted List (Ascending)"
    print_list(title, sorted_list)

    # Mean and median values 
    mean_value = mean(sorted_list)
    print("Mean:", mean_value)

    #Calculating the mean and median values
    median_value = median(sorted_list)
    print("Median:", median_value)

main()
