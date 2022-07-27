#include <iostream>
#include <math.h>

using namespace std;

double partB(int sides){
  double Pi_approx = 0;
  //sides = sides^2;

  double CosInDeg = cos(180/100)*57.2958;
  double SinInDeg = sin(180/100)*57.2958;

  Pi_approx = CosInDeg*SinInDeg*100;

//cout<< sides;
//cout<< CosInDeg;
  return Pi_approx;

  
}

int main()
{
  cout << partB(1000);
  return 0;
}