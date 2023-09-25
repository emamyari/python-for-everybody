def reverse_string(s):
    res=''
    for c in s:
        res=c+res
    return res

def count_char_digit(s):
    char=0
    digit=0
    for i in s:
        if i>='0' and i<='9':
            digit+=1
        if (i>='A' and i<='Z') or (i >= 'a' and i <= 'z'):
            char=char+1
    return [char,digit]

def find_largest_element(li):
    max=0
    for item in li:
        if item>max:
            max=item
    return max



def isPrime(n):
    res=True
    for item in range(2,n):
        if n%item==0:
            res=False
            break
    return res

def count_word(s):
    space=0
    for i in s:
        if i==' ':
            space+=1
    return space+1

def count_word2(s):
    a=s.count(' ')
    return a+1

# a=[]
# for i in range(1,10):
#     k=int(input('enter number : '))
#     a.append(k)

print(count_word2('hel lo wor ld'))