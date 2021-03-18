def main():
    
    x = input()
    x=x.split()
    x= list(map(int, x))
    z=[]
    for i in x:
        z.append(factors(i))
    j=[]
    j=sorted(range(len(z)), key=lambda k: z[k])

    x2 = [x[i] for i in j] 
    x2
    return x2

def factors(nr):
    i = 2
    factors = []
    while i <= nr:
        if (nr % i) == 0:
            factors.append(i)
            nr = nr / i
        else:
            i = i + 1
    return factors

if __name__ == '__main__':
    print(main())