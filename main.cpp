#include <iostream>
#include <math.h>
using namespace std;

double convert_to_deg(double x){
  return x*57.2958;
}

double partB(int sides){
  double Pi_approx = 0;
  //sides = sides^2;

  double CosInDeg = convert_to_deg(cos(180/sides));
  double SinInDeg = convert_to_deg(sin(180/sides));

  Pi_approx = CosInDeg*SinInDeg*sides;

//cout<< sides;
//cout<< CosInDeg;
  return Pi_approx;

  
}

int main()
{
  cout << partB(1000);
}