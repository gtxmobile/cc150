
def swapoddeven(a):
    return ((a & 0xaaaaaaaa)>>1)|((a & 0x55555555)<<1)

print(swapoddeven(16))
