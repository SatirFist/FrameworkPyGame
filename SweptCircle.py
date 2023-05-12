import math

#should probably use the vector math libraries, but to simplify I will just throw in a dot product for 2D vectors here instead
def dot(V1, V2):
    return V1[0] * V2[0] + V1[1] * V2[1]

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
def SphereSpehereSweep(ra, A0, A1, rb, B0, B1, u0, u1):
    va = A1 - A0; # vector from A0 to A1
    vb = B1 - B0; # vector from B0 to B1
    AB = B0 - A0; # vector from A0 to B0
    vab = vb - va; # relative velocity (in normalized time)
    rab = ra + rb;

    a = vab.dot(vab); # u * u coefficient
    b = 2 * vab.dot(AB); # u coefficient
    c = AB.dot(AB) - rab * rab; # constant term

    # check if they're currently overlapping
    if AB.dot(AB) <= rab * rab:        
        return (True, 0, 0);
    
    # check if they hit each other
    # during the frame
    res = QuadraticFormula( a, b, c)
    if res[0]:
        if res[1] > res[2]:
            return (True, res[2], res[1])
        else:
            return (True, res[1], res[2])                
    return (False, 0, 0)
