
n = int(input("Enter a number greater than 6: "))
list1 = [i for i in range(1,n+1)]

print(f'Original List: {list1}')
ext_list1 = list1[:5]
print(f'Extracted first five elements: {ext_list1}')
ext_list1.reverse()
print(f'Reversed extracted element: {ext_list1}')
