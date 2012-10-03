#!/usr/bin/env python
"""Simple implementation of ohm's law"""
import decimal

def V(i, r):
    "V = I*R Volts"
    return i*r

def I(v, r):
    "I = V/R Amps"
    return v/r

def R(i, v):
    "R = V/I Ohms"
    return v/i

def W(v,i):
    "W = V*I Whatts"
    return v*i

def P(v=None, i=None, r=None):
    "Calculate power (in Whatts) from any two of V, I and R"
    if v is not None and i is not None:
        return W(v,i)
    elif v is not None and r is not None:
        return W(v, I(v,r))
    elif i is not None and r is not None:
        return W(V(i,r), i)
    else:
        raise ValueError, "Not enough arguments to calculate power"

if __name__ == '__main__':
    import sys
    v=None
    i=None
    r=None
    for a in sys.argv[1].split(' '):
        try:
            arg, val = a.split('=')
        except ValueError:
            continue
        arg = arg.lower()
        if arg == 'v':
            try:
                v = decimal.Decimal(val)
            except decimal.InvalidOperation:
                sys.stderr.write('Can\'t parse "%s" as a value for voltage.' % val)
                sys.exit(1)
            else:
                sys.stdout.write('V=%s\t' % v.to_eng_string())
        elif arg == 'i':
            try:
                i = decimal.Decimal(val)
            except decimal.InvalidOperation:
                sys.stderr.write('Can\'t parse "%s" as a value for current.' % val)
                sys.exit(1)
            else:
                sys.stdout.write('I=%s\t' % i.to_eng_string())
        elif arg == 'r':
            try:
                r = decimal.Decimal(val)
            except decimal.InvalidOperation:
                sys.stderr.write('Can\'t parse "%s" as a value for resistance.' % val)
                sys.exit(1)
            else:
                sys.stdout.write('R=%s' % r.to_eng_string())
        else:
            sys.stderr.write('Unexpected argument: "%s=%s"' % (arg, val))
    sys.stdout.write('\n==========\n\n')
    if v is not None and i is not None:
        sys.stdout.write('R=%s\n' % R(i, v).to_eng_string())
        sys.stdout.write('W=%s\n' % W(v, i).to_eng_string())
        sys.stdout.write('P=%s\n' % P(i=i, v=v).to_eng_string())
    if v is not None and r is not None:
        sys.stdout.write('I=%s\n' % I(v, r).to_eng_string())
        sys.stdout.write('P=%s\n' % P(v=v, r=r).to_eng_string())
    if i is not None and r is not None:
        sys.stdout.write('V=%s\n' % V(i, r).to_eng_string())
        sys.stdout.write('P=%s\n' % P(i=i, r=r).to_eng_string())
