from math import sqrt
def getInfo(x1, y1, x2, y2):
   return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

def solve(points):
   N = len(points)
   firstx, firsty, firstz = points[0]
   prevx, prevy = firstx, firsty
   res = 0

   for i in range(1, N):
      nextx, nexty, nextz = points[i]
      res = res + getInfo(prevx,prevy,nextx,nexty)
      prevx = nextx
      prevy = nexty
   res = res + getInfo(prevx,prevy,firstx,firsty)
   return res

def find_half(points):
    stop = 0
    firstx, firsty, firstz = points[0]
    prevx, prevy, prevz = firstx, firsty, firstz
    sum = 0
    perimeter = solve(points)
    print(perimeter)
    print(perimeter / 2)

    while sum < perimeter / 2:
      stop += 1
      nextx, nexty, nextz = points[stop]
      sum = sum + getInfo(prevx, prevy, nextx, nexty)
      prevx = nextx
      prevy = nexty
    print(sum)
    print(stop)

    return stop
    