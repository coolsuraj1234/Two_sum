def arr1():
    array = []
    no_of_elements = int(input("Please enter the number of elements that you wish to store in the array: "))
    for z in range(no_of_elements):
        numbers = int(input('Enter the numbers: '))
        array.append(numbers)

    print("Here is the array", array)
    choice = input("if the array is correct please type yes: ").upper()
    if choice == 'YES':
        return array
    else:
        return arr1()


array = arr1()
target = int(input("Please give a target: "))
n = len(array)
for i in range(0, n):
    for j in range(i+1, n):
        if array[i] + array[j] == target:
            print(f'Output is {i} , {j}')

