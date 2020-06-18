def mantissa32(mantissa):
    while True:
        mantissa = str(mantissa) + "0"
        if len(mantissa) == 23:
            return mantissa


def converter_mantissa32(number):
    first, fraction = str(number).split(".")
    value = "0." + fraction
    mantissa = ""
    while True:
        mantissa = mantissa.lstrip()
        value = float(value) * 2
        firstI, fractionI = str(value).split(".")
        mantissa = mantissa + firstI
        value = "0." + fractionI
        if float(value) == 0.0 or len(mantissa) == 23:
            return mantissa


def posi_float(number):
    exp = 127

    if(number < 0):
        number = number * -1

    if number > 9:
        while True:
            number = number / 2
            exp += 1
            if number < 2:
                break

    exponent = bin(exp).replace('0b', '')

    if len(exponent) < 8:
        while len(exponent) < 8:
            exponent = '0' + exponent

    exponent = exponent + "."

    mantissa = converter_mantissa32(number)
    if len(mantissa) < 23:
        mantissa = mantissa32(mantissa)
    elif len(mantissa) > 23:
        print("A mantissa é maior que 23!")
    result = str(exponent) + str(mantissa)
    return result


def small_number(number):
    exp = 127

    if(number < 0):
        number = number * -1

    while True:
        number = number * 2
        exp -= 1
        if number >= 1:
            break

    exponent = bin(exp).replace('0b', '')
    if len(exponent) < 8:
        while len(exponent) < 8:
            exponent = '0' + exponent
    exponent = exponent + "."

    mantissa = converter_mantissa32(number)
    if len(mantissa) < 23:
        mantissa = mantissa32(mantissa)
    elif len(mantissa) > 23:
        print("A mantissa é maior que 23!")
    result = str(exponent) + str(mantissa)
    return result


def float_converter(number):
    if number < 1 and number > 0:
        convert = "0." + small_number(number)
    elif number < 0 and number < -1:
        convert = "1." + posi_float(number)
    elif number < 0 and number > -1:
        convert = "1." + small_number(number)
    else:
        convert = "0." + posi_float(number)
    return convert
