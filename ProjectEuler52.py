def signature(num: str):
    signature = ""
    for d in range(10):
        if str(d) in num:
            signature += str(d)
    return signature


def sol52():
    number = 1
    while True:
        sig = signature(str(number))
        for mul in range(2, 7):
            number_mul = number * mul
            if signature(str(number_mul)) != sig:
                break
        else:
            return number
        number += 1


print(sol52())

