
def add_no_arri(a,b):
    if b==0:
        return a
    sum=a^b
    carry=(a&b)<<1
    return add_no_arri(sum,carry)
