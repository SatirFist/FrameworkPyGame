import math

#should probably use the vector math libraries, but to simplify I will just throw in a dot product for 2D vectors here instead
def dot2d(V1, V2):
    return V1[0] * V2[0] + V1[1] * V2[1]

def sub2d(v1,v2):
    return (v1[0] - v2[0], v1[1] - v2[1])

def add2d(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

def mult2dScaler(v1, s):
    return (v1[0] * s, v1[1] * s)

def normalize2D(V):    
    mag = V[0] * V[0] + V[1] * V[1]
    fact = math.sqrt(mag)
    if fact <= 0:
        #zero vector...error
        return [0,0]
    return (V[0] / fact, V[1] / fact)
    

def QuadraticFormula(a, b, c):
    q = b * b - 4 * a * c
    if q >= 0:
        sq = math.sqrt(q)
        d = 1 / (2 * a)
        r1 = ( -b + sq ) * d;
        r2 = ( -b - sq ) * d;
        return (True, r1, r2)
    else:
        return (False, 0, 0)

# ra = radius of sphere A
# A0 = previous position of sphere A
# A1 = current position of sphere A
# rb = radius of sphere B
# B0 = previous position of sphere B
# B1 = current position of sphere B
# u0 = normalized time of first collision
# u1 = normalized time of second collision
# returns a tuple of (boolean fot hit, u0, u1)
def SphereSpehereSweep(ra, A0, A1, rb, B0, B1):    
    va = sub2d(A1, A0) #va = A1 - A0; # vector from A0 to A1
    vb = sub2d(B1, B0) #vb = B1 - B0; # vector from B0 to B1
    AB = sub2d(B0, A0) #AB = B0 - A0; # vector from A0 to B0
    vab = sub2d(vb, va) # vab = vb - va; # relative velocity (in normalized time)
    rab = ra + rb;

    a = dot2d(vab,vab) # a = vab.dot(vab); # u * u coefficient
    b = 2 * dot2d(vab, AB) #  b = 2 * vab.dot(AB); # u coefficient
    c = dot2d(AB, AB) - rab * rab # c = AB.dot(AB) - rab * rab; # constant term

    # check if they're currently overlapping
    if dot2d(AB, AB) <= rab * rab:  
        print('overlapping')      
        return (True, 0, 0);
    
    # check if they hit each other
    # during the frame
    res = QuadraticFormula( a, b, c)
    if res[0] == True:
        print(A0,A1,B0,B1)
        print(va, vb, AB, vab, rab, a, b, c)
        print('collision')      
        if res[1] > res[2]:
            return (True, res[2], res[1])
        else:
            return (True, res[1], res[2])                
    return (False, 0, 0)

def dist2d(V1, V2):
    return math.sqrt((V1[0] - V2[0])*(V1[0] - V2[0]) + (V1[1] - V2[1])*(V1[1] - V2[1]))

def sphereoverlaps(ra, A0, A1, rb, B0, B1): 
    d1 = dist2d(A1, B1)    
    d2 = dist2d(A1, B0)    
    d3 = dist2d(A0, B1)    
    d4 = dist2d(A0, B0)    
    rsum = ra+rb
    if d1 <= rsum or d2 <= rsum or d3 <= rsum or d4 <= rsum:
        return [True,0,0]
    return [False,0,0]
