import math

Roman_numbers_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


# function of creating list of operations and roman numbers
def Roman_numbers_input():
    input_operation = None
    while input_operation != 'EXIT':
        roman_to_arab()                  # input and translating roman numbers to arab num
        exit_inp = opInp()
        if exit_inp == 'EXIT':
            input_operation = 'EXIT'
 
def opInp():     #function of creating list of operations
    try:
        input_operation = input('input operation or if you want to finish input "exit": ').replace(' ','').upper()
        if input_operation in op_list and input_operation != 'EXIT':
            operators_list.append(input_operation)
        elif input_operation == 'EXIT':
            equation()
            return 'EXIT'
        else:
            op_list.index(input_operation)
    except Exception:    # if wrong input - input again
        print('wrong input, input again!')
        opInp()
 
        
# function of translating roman numbers to arab numbers
def roman_to_arab():
    res = 0
    try:
        input_num = input('input num!').replace(' ','').upper().strip()
        input_num = input_num.upper().strip().replace("IV", "IIII").\
                replace("IX", "VIIII").\
                replace("XL", "XXXX").\
                replace("XC", "LXXXX").\
                replace("CD", "CCCC").\
                replace("CM", "DCCCC")
        for elem in input_num:
            res += Roman_numbers_dict.get(elem)
        if str(res).isdigit() == True:
            arab_num_list.append(res)
    except Exception:                # in case of error it starts the program again
        print('wrong number! please, input this num again')
        roman_to_arab()  # input num again
         
# Equation result
def equation():
    while len(arab_num_list) != 1:
    	   for i in range(len(arab_num_list)-1):
    	       total = 0
    	       i = 0
    	       a = int(arab_num_list[i])
    	       b = int(arab_num_list[i+1])
    	       op = operators_list[i]
    	            
    	       if op == "+":
    	           total += a + b
    	       elif op == "-":
    	           total += (a - b)
    	       elif op == "*":
    	           total += (a * b)
    	       elif op == "/":
    	           if a >= b:
    	               total +=  int((a/b))
    	           else:
    	               print("incorrect input! please, try again!")
    	               Roman_numbers_input()
    	       arab_num_list.pop(i)
    	       arab_num_list.pop(i)
    	       arab_num_list.insert(0, total)
    	       operators_list.pop(i)


# Arab number to Roman numbers and print result.
def integerToRoman(A):
    romansDict = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: 'D', 1000: 'M'}
    div = 1
    while A >= div:
        div *= 10
    div //= 10
    res = ""
    while A:
        # main significant digit extracted
        # into lastNum
        lastNum = (A // div)
        if lastNum <= 3:
            res += (romansDict[div] * lastNum)
        elif lastNum == 4:
            res += (romansDict[div] +
                          romansDict[div * 5])
        elif 5 <= lastNum <= 8:
            res += (romansDict[div * 5] +
            (romansDict[div] * (lastNum - 5)))
        elif lastNum == 9:
            res += (romansDict[div] +
                         romansDict[div * 10])
        A = math.floor(A % div)
        div //= 10
    print(res)



#body
op_list = ['+', '-', '/', '*','EXIT'] # list of operators for function
operators_list = []
arab_num_list = []

print('Greeting! This is rome numbers calculator! It can calculate rome numbers from 1 to 1000')
print('Please, input only rome number!')

Roman_numbers_input()

# If number is negative it starts the programm again
if arab_num_list[0] <= 0:
    print('Your score is negative! Please, try again!')
    arab_num_list.clear()      #clear subjects which were written before  
    operators_list.clear()     #clear subjects which were written before
    Roman_numbers_input()
if arab_num_list[0] > 1000:
    print('Your score is more than 1000! Please, try again!')
    arab_num_list.clear()      #clear subjects which were written before  
    operators_list.clear()     #clear subjects which were written before
    Roman_numbers_input()

#show result
integerToRoman(arab_num_list[0])












