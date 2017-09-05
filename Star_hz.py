import math
from fractions import Fraction
def hz_calc():
    print '-------------------------------------'
    print 'Stage 1 - Calculate Absolute Magnitude'
    m = float(raw_input('Enter apparent magnitude of host star: '))
    d = float(raw_input('Enter distance from earth in parsecs: '))
    dLog = d/10
    fiveLog = (math.log10(6.23/10)/2) * 10
    M = m - fiveLog
    print 'M = m - 5Log(d/10)'
    print 'm: %s' % m
    print 'd: %s' %d
    print 'Absolute Magnitude: %s' % M
    print '-------------------------------------'

    print 'Stage 2 - Calculate Bolometric Magnitude'
    BC = float(raw_input('Enter bolometric correction constant for star class: '))
    Mbol = M + BC
    print 'Mbol = M + BC'
    print "M: %s" %m
    print "BC: %s" %BC
    print 'Bolometric Magnitude: %s' % Mbol
    print '-------------------------------------'

    print 'Stage 3 - Calculate Absolute Luminosity'

    def round_up(x, place):
        return round(x + 5 * 10**(-1 * (place + 1)), place)

    PR = 2.5
    Mbol_sun = 4.72

    aLum = math.pow(10, (Mbol - Mbol_sun) / - PR)
    aLum = round_up(aLum, 3)
    print 'Lstar/Lsun = 10^[Mbol-star - Mbol-sun / -2.5]'
    print 'Mbol: %s' %Mbol
    print 'Mbol_sun: %s' %Mbol_sun
    print "Pogson's ration: - 2.5"
    print 'Absolute Luminosity: %s' %aLum


    print '-------------------------------------'

    print 'Stage 4 - Approximate the boundaries of the habitable zone for this star'

    IZC = 1.1
    OZC = 0.53
    Ri = round(math.sqrt(aLum/IZC), 2)
    Ro = round(math.sqrt(aLum/OZC), 2)

    print 'Ri = round(math.sqrt(aLum/IZC), 2)'
    print 'Ro = round(math.sqrt(aLum/OZC), 2)'

    print 'aLum: %s' % aLum
    print 'IZC: %s' % IZC
    print 'OZC %s' % OZC

    print 'Inner Radius: %s AU' % Ri
    print 'Outer Radius: %s AU' % Ro

while True:
    hz_calc()