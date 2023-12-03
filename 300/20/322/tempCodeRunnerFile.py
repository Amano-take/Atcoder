sL, sR, sA, sL0, sR0, sA0, sAL = s
    tL, tR, tA, tL0, tR0, tA0, tAL = t
    if sL == sAL:
        aL = sL + tL
    else:
        aL = sL
    
    if tR == tAL:
        aR = tR + sR
    else:
        aR = tR

    if sL0 == sAL:
        aL0 = sL0 + tL0
    else:
        aL0 = sL0
    
    if tR0 == tAL:
        aR0 = tR0 + sR0
    else:
        aR0 = tR0
    
    aA = max(sR + tL, tA, sA)
    aA0 = max(sR0 + tL0, tA0, sA0)
    aAL = sAL + tAL

    return (aL, aR, aA, aL0, aR0, aA0, aAL)