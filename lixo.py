import math
import sys

bins = {
    "none": ["white", ""],
    "lixo": ["#72859E", "Lixo"],
    "papl": ["#255FC9", "Papel"],
    "embl": ["#DED044", "Embalagens"],
}

days = ["Sun", "Mon", "Tues", "Wednes", "Thurs", "Fri", "Satur"]
schd = [["none"],
        ["lixo"],
        ["papl", "embl"],
        ["lixo"],
        ["papl"],
        ["lixo", "embl"],
        ["papl"]]

wh = sys.argv[1]
pps = 1.0/len(days)
rot = -0.25 - pps/2.0

def getXY(p, r, s):
    a = 2.0 * math.pi * (p * pps + rot)
    return s % (r * math.cos(a),
                r * math.sin(a))

def path(p, r):
    s = " %.2f %.2f "
    pa = "M"
    pa += getXY(p, r, s)
    pa += "A 1 1 0 0 1"
    pa += getXY((p+1), r, s)
    return pa

def text(fs, tid, t):
    print('''
    <text font-size="%s">
    <textPath startOffset="50%%" text-anchor="middle" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#%s">
    <tspan font-family="sans-serif">%s</tspan>
    </textPath>
    </text>''' % (fs, tid, t))

outerc = 0.98
innerc = 0.5
centrec = 0.1

print('<svg xmlns="http://www.w3.org/2000/svg" viewBox="-1 -1 2 2" width="%s" height="%s">' % (wh, wh))

for p in range(len(days)):
    c = outerc
    tp = 0.85
    for s in schd[p]:
        b = bins[s]
        print('<path d="%s" fill="%s"/>' % (path(p, c) + "L 0 0", b[0]))

        tid = "type%d%s" % (p, b[1])
        print('<path d="%s" fill="transparent" id="%s"/>' % (path(p, tp), tid))
        text("0.08", tid, b[1])
        c += innerc
        c /= 2
        tp += innerc
        tp /= 2
        tp -= 0.04

for p in range(len(days)):
    print('<line stroke="black" stroke-width="0.02"' +
          getXY(p, outerc, ' x1="%.2f" y1="%.2f"') +
          getXY(p, innerc, ' x2="%.2f" y2="%.2f"') + "/>")

print('''
<circle cx="0" cy="0" r="%f" fill="white" stroke="black" stroke-width="0.02"/>
<circle cx="0" cy="0" r="%f" fill="black"/>
<circle cx="0" cy="0" r="%f" fill="white"/>
<circle cx="0" cy="0" r="%f" fill="transparent" stroke="black" stroke-width="0.02"/>''' % (innerc, centrec, centrec/2, outerc))

for p in range(len(days)):
    tid = "day%d" % p
    print('<path d="%s" fill="transparent" id="%s"/>' % (path(p, 0.45), tid))
    text("0.05", tid, days[p]+"day")

print("</svg>")


