def DecToBin(d):
    b = ''
    while True:
        if d == 0:
            break
        elif (d % 2) == 0:
            d = d // 2
            b = '0' + b
        else:
            d = d // 2
            b = '1' + b
    return b
def FloatToBin(number, places=3):
    #Разделит на два частя до точки целое а потом после точки
    whole, dec = str(number).split(".")
    whole = int(whole)
    dec = int(dec)
    res = DecToBin(whole)+'.'
    decproduct = dec
    counter=0
    while (counter <= places):
        decproduct = decproduct * (10 ** -(len(str(decproduct))))
        decproduct *= 2
        decwhole, decdec = str(decproduct).split('.')
        decwhole = int(decwhole)
        decdec = int(decdec)
        res+=str(decwhole)
        decproduct = decdec
        counter += 1
    return res
def decimal_converter(num):
    while num > 1:
        num /= 10
    return num
def BinToDec(binary):
    binary=binary[::-1]
    d = 0
    power = 0
    for i in range(len(binary)):
        d += int(binary[i]) * (2 ** power)
        power += 1
    return d
def BinToFloat(binar):
    whole,dec=binar.split('.')
    d=0
    pw=0
    d=BinToDec(whole)
    pw=-1
    for i in range(len(dec)):
        d+=int(dec[i])*2**pw
        pw+=-1
    return d
def OutNoZero(a):
    i=0
    print(' ',end='')
    while (i<len(a))and(a[i]=='0'):
        i+=1
        print(' ',end='')
    print(a[i:])
#Реализуем сложение 
def binAdd(s1, s2):
    if not s1 or not s2:#проверим строк на пустоту
        return ''
    #Нам нужно нормализироват оба строк к одинокой длины
    maxlen = max(len(s1), len(s2))
    #заполняем нулями (лидируюшый)
    s1 = s1.zfill(maxlen)
    s2 = s2.zfill(maxlen)
    result  = ''
    ostat   = 0#Остаток
    i = maxlen - 1
    #нужно начать в обратном порядки сложит как столбик
    while(i >= 0):
        s = int(s1[i]) + int(s2[i])
        if s == 2: #1+1
            if ostat == 0:
                ostat = 1
                result = "%s%s" % (result, '0')
            else:
                result = "%s%s" % (result, '1')
        elif s == 1: # 1+0
            if ostat == 1:
                result = "%s%s" % (result, '0')
            else:
                result = "%s%s" % (result, '1')
        else: # 0+0
            if ostat == 1:
                result = "%s%s" % (result, '1')
                ostat = 0
            else:
                result = "%s%s" % (result, '0')
        i = i - 1
    if ostat>0:
        result = "%s%s" % (result, '1')
    return result[::-1]#результат
#Реализуем дополнение нулями проавый часть
def zRightFill(s=str(''),max_len=int()):
    ans=s
    for i in range(max_len-len(s)):
        ans+='0'
    return ans

#Реализуем сложение чисел с плаваюшых точек
def flbinAdd(s1,s2):
    awh,adec=s1.split('.')
    bwh,bdec=s2.split('.')
    resWh=binAdd(awh,bwh)
    mxz=max(len(adec),len(bdec))
    adec=zRightFill(adec,mxz)
    bdec=zRightFill(bdec,mxz)
    resDec=binAdd(adec,bdec)
    res=resWh+'.'+resDec

    outA=awh+'.'+adec
    outB=bwh+'.'+bdec
    outA=outA.zfill(len(res))
    outB=outB.zfill(len(res))
    OutNoZero(outA)
    print('+')
    OutNoZero(outB)
    print(' '+res)
    return res

#Реализуем вычитание тоже как сложение
def subtraction(a, b):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    result = ''
    temp = 0
    for i in range(max_len - 1, - 1, - 1):
        num = int(a[i]) - int(b[i]) - temp
        if num % 2 == 1:
            result = '1' + result
        else:
            result = '0' + result
        if num < 0:
            temp = 1
        else:
            temp = 0
    if temp != 0:
        result = '01' + result
    if int(result) == 0:
        result = '0'
    return result
#тепер для чисел с плаваюшых точек
def flsubtraction(a,b):
    awh,adec=a.split('.')
    bwh,bdec=b.split('.')
    mx_len=max(len(awh),len(bwh))
    mx_zlen=max(len(adec),len(bdec))
    awh=awh.zfill(mx_len)
    bwh=bwh.zfill(mx_len)
    adec=zRightFill(adec,mx_zlen)
    bdec=zRightFill(bdec,mx_zlen)
    resa=awh+adec
    resb=bwh+bdec
    OutNoZero(awh+'.'+adec)
    print('-')
    OutNoZero(bwh+'.'+bdec)
    res=subtraction(resa,resb)
    res=res[:len(res)-mx_zlen]+'.'+res[len(res)-mx_zlen:]
    return res
"""
Теперь у нас есть сложение мы можем спокойно умножит только 
для визуализация нужно быт остоожно
 101
x 11
   101 
  101
  =
  1111
  Вот так должно произойти и нужно сохранит 
"""
def multiplication(a, b):
    max_len = max(len(a), len(b))
    min_len = min(len(a), len(b))
    result = ''
    temp_result = ''
    temp = []
    zeroes = 0
    temp_index =0
    for j in range(min_len - 1, - 1, - 1):
        temp_result = ''
        for i in range(max_len - 1, - 1, - 1):
            summ = int(a[i]) * int(b[j])
            if summ == 0:
                temp_result = '0' + temp_result
            elif summ == 1:
                temp_result = '1' + temp_result
        temp_result = temp_result + ('0' * zeroes)
        zeroes += 1
        temp.append(temp_result)
        if len(temp) == 2:
            result = binAdd(str(temp[0]), str(temp[1]))
        elif len(temp) > 2:
            temp_index = len(temp)
            temp_index += 1
            result = binAdd(str(result), str(temp[temp_index - 2]))
        else:
            pass
    return [result,temp]
#Реализуем умножение для чисел с плаваюшой точкой
def flmultiPlacation(a,b):
    aa=a[:a.find('.')]+a[a.find('.')+1:]
    bb = b[:b.find('.')] + b[b.find('.') + 1:]
    zcnt=len(a)-a.find('.')+len(b)-b.find('.')-2     #10.11
    print(zcnt)
    r,tm=multiplication(aa,bb)
    if (r == ''):
        r = tm[len(tm) - 1]
    r=r[:len(r)-zcnt]+'.'+r[zcnt:]
    mx = len(r)
    a = a.zfill(mx)
    b = b.zfill(mx)
    OutNoZero(a)
    print('x')
    OutNoZero(b)
    for i in range(len(tm)):
        print(tm[i].rjust(mx))
        if i != len(tm) - 1:
            print('+')
    print('=')
    print(r)
    print(BinToFloat(r))

#Реализуем функция round
def roundBin(bin):
    bans=''
    bans+=bin[:bin.find('.')]
    return bans
"""
Это раздел скрыто пока 
"""
def division(a, b):
    result = ''
    temp = '0'
    r = 0
    for i in range(len(a)):
        if int(b) > int(temp):
            result += '0'
            temp += a[i]
        else:
            r = subtraction(temp, b)
            if r == 0:
                temp = a[i]
                result += '1'
            else:
                r = str(r).lstrip('0')
                result += '1'
                temp = r + a[i]
    if temp != int(0):
        result = result + '0'
    return result