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
    D = int(to_how_many_decial_places) #making the input a number
    Pi_approx = 0
    n = 4

    while str(Pi_approx)[0:D+2] != str(math.pi)[0:D+2]: 
        #while the number of deciaml places of calulating pi does not equal to the- 
        #number of decmial places of the actual vaule of pi
        Pi_approx = math.cos(math.radians(180/(n)))*math.sin(math.radians(180/(n)))*n
        n += 1
        #does the equation and adds one to n
        #the upper and lower bound is not used beacuse it would take longer than it is

    ans = str(Pi_approx) #turns the answer into a string - eaiser to return 
    answer = ans[0:D+2] #returns the value of pi to D number of decimal places
    return answer

print(extention(10))
#print(part_B(100))


#print(Approximation_of_pi(5))





