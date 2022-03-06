def powmod(base: int, exponent: int, mod: int) -> int:
    res = 1;
    while exponent != 0:
        if exponent & 1:
            res = int(res * base % mod)
            exponent -= 1
        else:
            base = int(base * base % mod);
            exponent >>= 1
    return res


def factor(number: int) -> list:
    fact = []
    i = 2
    n = number - 1
    # Same as [2, sqrt(n)]
    while i*i <= n:
        if n % i == 0:
            fact.append(i);
            while n % i == 0: n /= i;
        i += 1

    if n > 1:
        fact.append(n);
    return fact


def generate(number: int) -> int:
    res = 1
    
    fact = factor(number)

    while res <= number:
        is_primitive_root = True
        # res is primitive root if all powers ain't 1
        for i in fact:
            is_primitive_root &= (powmod(res, int((number-1)/i), number) != 1)

        if is_primitive_root:
            return res
        res += 1
    return -1;
