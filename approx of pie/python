import math
def part_B(n): #where n is the number of sides
    Pi_approx = 0
    upper_bound = math.cos(math.radians(180/(n)))*math.sin(math.radians(180/(n)))*n
    lower_bound = math.tan(math.radians(180/(n)))*n

    Pi_approx = (upper_bound + lower_bound)/2
    return Pi_approx


def part_C():
    Pi_approx = 0
    n = 4

    while str(Pi_approx)[0:5+2] != str(math.pi)[0:5+2]:
        Pi_approx = math.cos(math.radians(180/(n)))*math.sin(math.radians(180/(n)))*n
        n += 1

    ans = str(Pi_approx)
    print(ans)

def extention(to_how_many_decial_places):
    D = int(to_how_many_decial_places)
    Pi_approx = 0
    n = 4

    while str(Pi_approx)[0:D+2] != str(math.pi)[0:D+2]:
        Pi_approx = math.cos(math.radians(180/(n)))*math.sin(math.radians(180/(n)))*n
        n += 1

    ans = str(Pi_approx)
    answer = ans[0:D+2]
    return answer

print(extention(10))
#print(part_B(100))


#print(Approximation_of_pi(5))





