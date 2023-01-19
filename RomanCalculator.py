Roman_numbers_dict = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10,
'XI': 11, 'XII': 12, 'XIII': 13, 'XIV': 14, 'XV': 15, 'XVI': 16, 'XVII': 17, 'XVIII': 18, 'XIX': 19, 'XX': 20,
'XXI': 21, 'XXII': 22, 'XXIII': 23, 'XXIV': 24, 'XXV': 25, 'XXVI': 26, 'XXVII': 27, 'XXVIII': 28, 'XXIX': 29, 'XXX': 30,
'XXXI': 31, 'XXXII': 32, 'XXXIII': 33, 'XXXIV': 34, 'XXXV': 35, 'XXXVI': 36, 'XXXVII': 37, 'XXXVIII': 38, 'XXXIX': 39, 'XL': 40,
'XLI': 41, 'XLII': 42, 'XLIII': 43, 'XLIV': 44, 'XLV': 45, 'XLVI': 46, 'XLVII': 47, 'XLVIII': 48, 'XLIX': 49, 'L':50, 
'LI': 51, 'LII': 52, 'LII': 53, 'LIV': 54, 'LV': 55, 'LVI': 56, 'LVII': 57, 'LVIII': 58, 'LIX': 59, 'LX': 60,
'LXI': 61, 'LXII': 62, 'LXIII': 63, 'LXIV': 64, 'LXV': 65, 'LXVI': 66, 'LXVII': 67, 'LXVIII': 68, 'LXIX': 69, 'LXX': 70,
'LXXI': 71, 'LXXII': 72, 'LXXIII': 73, 'LXXIV': 74, 'LXXV': 75, 'LXXVI': 76, 'LXXVII': 77, 'LXXVIII': 78, 'LXXIX': 79, 'LXXX': 80,
'LXXXI': 81, 'LXXXII': 82, 'LXXXIII': 83, 'LXXXIV': 84, 'LXXXV': 85, 'LXXXVI': 86, 'LXXXVII': 87, 'LXXXVIII': 88, 'LXXXIX': 89, 'XC': 90, 
'XCI': 91, 'XCII': 92, 'XCIII': 93, 'XCIV': 94, 'XCV': 95, 'XCVI': 96, 'XCVII': 97, 'XCVIII': 98, 'XCIX': 99, 'C': 100}


# function of creating list of operations and roman numbers
def Roman_numbers_input():
    input_num = None
    input_operation = None
    while input_operation != 'exit':
        input_num = input('input num!').replace(' ','').upper()
        list_of_nums_and_operations.append(input_num)
        input_operation = input('input operation!').replace(' ','')
        if input_operation != 'exit':
            list_of_nums_and_operations.append(input_operation)

#create lists for roman numbers and operators
def Listing():
    for i in list_of_nums_and_operations:
        if i.isalpha() == True:
            num_list.append(i)
        else:
            continue
    
    for i in list_of_nums_and_operations:
        if i == '+' or i == '-' or i == '*' or i == '/':
            operators_list.append(i)
        else:
            continue
        
#body
list_of_nums_and_operations = []
num_list = []
operators_list = []

print('Greeting! This is rome numbers calculator! It can calculate rome numbers from 1 to 100')
print('Please, input only rome number!')

Roman_numbers_input()
Listing()

arab_num_list = []
# roman num to arab num
for i in num_list:
    a = Roman_numbers_dict[i]
    arab_num_list.append(a)
    
while len(arab_num_list) != 1:
	   for i in range(len(arab_num_list)-1):
	       total = 0
	       i = 0
	       a = arab_num_list[i]
	       b = arab_num_list[i+1]
	       op = operators_list[i]
	            
	       if op == "+":
	           total = total + a + b
	       elif op == "-":
	           total = total + (a - b)
	       elif op == "*":
	           total = total + (a * b)
	       elif op == "/":
	           total = total + (a/b)
	       arab_num_list.pop(i)
	       arab_num_list.pop(i)
	       arab_num_list.insert(0, total)
	       operators_list.pop(i)


for rome, num in Roman_numbers_dict.items():
    if num == total:
        print(rome)



