import math

def circlecolide(x1, y1, x2, y2, raidius):
    if math.sqrt((x1-x2)**2 + (y1-y2)**2) < raidius:
        return True
    else:
        return False

print("Whats the first x corrd?")
a = int(input())
print("Whats the first y corrd?")
b = int(input())
print("Whats the second x corrd?")
c = int(input())
print("Whats the second y corrd?")
d = int(input())
print("Whats the first raidius")
e = int(input())

if circlecolide(a, b, c, d, e):
    print("YoU HAVE COLLIDED")
else:
    print("Not close")
