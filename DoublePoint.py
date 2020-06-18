def mantissa64(mantissa):
    while True:
        mantissa = str(mantissa) + "0"
        if len(mantissa) == 52:
            return mantissa


def converter_mantissa64(number):
    first, fraction = str(number).split(".")
    value = "0." + fraction
    mantissa = " "
    while True:
        mantissa = mantissa.lstrip()
        value = float(value) * 2
        firstI, fractionI = str(value).split(".")
        mantissa = mantissa + firstI
        value = "0." + fractionI
        if float(value) == 0.0 or len(mantissa) == 52:
            return mantissa


def posi_Double(number):
    exp = 1023

    if(number < 0):
        number = number * -1

    if number > 9:
        while True:
            number = number / 2
            exp += 1
            if number < 2:
                break

    exponent = bin(exp).replace('0b', '')

    if len(exponent) < 11:
        while len(exponent) < 11:
            exponent = '0' + exponent

    exponent = exponent + "."

    mantissa = converter_mantissa64(number)

    if len(mantissa) < 52:
        mantissa = mantissa64(mantissa)
    elif len(mantissa) > 52:
        print("A mantissa é maior que 23!")
    result = str(exponent) + str(mantissa)
    return result


def small_number(number):
    exp = 1023

    if(number < 0):
        number = number * -1

    while True:
        number = number * 2
        exp -= 1
        if number >= 1:
            break

    exponent = bin(exp).replace('0b', '')
    if len(exponent) < 11:
        while len(exponent) < 11:
            exponent = '0' + exponent
    exponent = exponent + "."

    mantissa = converter_mantissa64(number)
    if len(mantissa) < 52:
        mantissa = mantissa64(mantissa)
    elif len(mantissa) > 52:
        print("A mantissa é maior que 23!")
    result = str(exponent) + str(mantissa)
    return result


def Double_converter(number):
    if number < 1 and number > 0:
        convert = "0." + small_number(number)
    elif number < 0 and number < -1:
        convert = "1." + posi_Double(number)
    elif number < 0 and number > -1:
        convert = "1." + small_number(number)
    else:
        convert = "0." + posi_Double(number)
    return convert
