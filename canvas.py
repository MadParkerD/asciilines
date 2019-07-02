import sys

if len(sys.argv) < 2:
    print("needs filename")
    sys.exit()
a1 = sys.argv[1]
with open(a1) as fp:
    s = fp.readline().split()
    if len(s) > 2:
        sys.exit()
    h = int(s[0])
    v = int(s[1])
    canvas = [["." for i in range(v)] for j in range(h)]
    for line in fp:
        if len(line) < 5:
            sys.exit()
        ln = line.split()
        character = ln[0]
        hoffset   = int(ln[1])
        voffset   = int(ln[2])
        direction = ln[3]
        length    = int(ln[4])
        drawn = 0
        message = "Take a long look at that .tvg file, because it tried to print a line     completely outside the canvas"
        if direction in "h":
            if h < 0:
                print(message)
                sys.exit()
            for x in range(v):
                if x >= voffset and  drawn < length:
                    canvas[hoffset][x] = character
                    drawn+=1
        elif direction in "v":
            if v < 0:
                print(message)
                sys.exit()
            for x in range(h):
                if x >= hoffset and  drawn < length:
                    canvas[x][voffset] = character       
                    drawn+=1
for x in canvas:
    for y in x:
        print(y, end='')
    print('')
