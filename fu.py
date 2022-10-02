n,m,s = map(int,input().split())
summ = 0
mas = []
prefixb = []
prefixa = []
for i in range(max(n,m)):
    a, b = [x for x in input().split(' ')]
    if i + 1 <= n:
        a = int(a)
    else:
        a = 10000 + 1
    if i + 1 <= m:
        b = int(b)
    else:
        b = 10000 + 1
    if summ > s:
        if (a - prefixb[-1]) < (b - prefixa[-1]):
            if (a - prefixb[-1]) < 0:
                summ += a - prefixb[-1]
                del prefixb[-1]
                prefixa.append(a)
        else:
            if (b - prefixa[-1]) < 0:
                summ += b - prefixa[-1]
                del prefixa[-1]
                prefixb.append(b)
    else:
        if a != 10000 + 1:
            summ += a
            prefixa.append(a)
        if b != 10000 + 1:
            summ += b
            prefixb.append(b)
while summ > s:
    if prefixa[-1] < prefixb[-1]:
        summ -= prefixb[-1]
        del prefixb[-1]
    else:
        summ -= prefixa[-1]
        del prefixa[-1]
                
print(len(prefixa) + len(prefixb))
print(prefixa)
print(prefixb)
    
