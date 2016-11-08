# Gjettespill!
# Dette er en kommentar. Python ignorerer alt som kommer
# etter en hask(#)

low = 0
high = 100

def guess():
    total = high + low          # f.eks 75 + 50 = 125
    average = total / 2         # 125/2 = 62.5
    next_guess = int(average)   # int(62.5) = 62
    return next_guess

def lower():
    # global lar oss endre en global variabel
    # inne i en funksjon
    global high
    high = guess() - 1
    return guess()

def higher():
    global low
    low = guess() + 1
    return guess()

def correct():
    return "Yippie!!!"
