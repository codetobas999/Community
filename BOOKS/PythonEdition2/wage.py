def calfirst(rate):
    return 40 * rate


def calextra(hr, rate):
    return (hr - 40) * (1.5 * rate)


def calwage(hr, rate):
    total = calfirst(hr) + calextra(hr, rate)
    return total
