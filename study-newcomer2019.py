
import time




def input_name():
    name = input('名前を入力してください：')
    return name

def input_number():
    number = []
    print('Enter "q" then finish')
    while True:

        try:
            val = input('Enter value: ')
            val = int(val)
            number.append(val)
        except:
            if val == 'q':
                print('FINISH')
                break
            else:
                print('one more please')
    return number

# def pop_number():
#     sum = 0
#     x = 0
#     for i in number:
#         n = number.pop(x)
#         sum += n
#         x += 1
#         print(sum)
#     return sum



start = time.time()

name = input_name()
number = input_number()
#print(number)
#for i in number:
#    print(i.pop())
#number.pop()


#pop_number()


process_time = time.time() - start

print('input→' + name + ', 配列= ' + str(number))

print('name:' + name + ',  sum:' + str(sum(number))+ ',  配列 = ' + str(number) + '; time: ' + str(process_time))
