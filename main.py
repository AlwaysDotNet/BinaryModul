from binary import *
a=float(input('Введите первое число : '))
b=float(input('Введите второе число : '))
bina=FloatToBin(a)
binb=FloatToBin(b)
print("В дяситчном: "+str(a)+'  В двоичном: '+bina)
print("В дяситчном: "+str(b)+'  В двоичном: '+binb)
ch=input("Операция(+-*/): ")
if ch=='+':
    r=flbinAdd(bina,binb)
    print('(10)=',BinToFloat(r))
elif ch=='-':
    cr='+'
    if(bina[:bina.find('.')]<binb[:binb.find('.')]):
        bina,binb=binb,bina
        cr='-'
    res=flsubtraction(bina,binb)
    if cr=='-':
        print(cr,end='')
    OutNoZero(res)
    print(BinToFloat(res))
elif ch=='*':
    if (a<b):
        bina, binb = binb, bina
    flmultiPlacation(bina,binb)
#деление работает только целим числам и поэтому берем только цилое
elif ch=='/':
    bina=roundBin(bina)
    binb=roundBin(binb)
    res=division(bina,binb)
    OutNoZero(res)
    print(BinToDec(res))