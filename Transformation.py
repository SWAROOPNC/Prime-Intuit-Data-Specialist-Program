def conv(a,c) :
    return (lambda x : (a*x)+c)
kms2miles = conv(0.62,0)
kms2feet =conv(3280.8,0)
mtr2feet = conv(3.28,0)
cent2inch = conv(0.39,0)
mile2inch = conv(0.039,0)

constant = 32
_constant = 22
__constant = 12