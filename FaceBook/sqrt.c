#include "stdlib.h"
#include "stdio.h"

double sqrt13( int n )
{
	// double a = (eventually the main method will plug values into a)
	double a = (double) n;
	double x = 1;
 
	// For loop to get the square root value of the entered number.
	for( int i = 0; i < n; i++)
	{
		x = 0.5 * ( x+a / x );
	}
 
	return x;
}

double sqrt1(int n){
	double x = 1;
	for(int i = 0; i < n; i++){
		x = x / 2 + n / (2 * x);
	}
	
	return x;
}

int main(int argc, char** argv){
	if(argc > 1){
		fprintf(stdout, "%f\n", sqrt13(atoi(argv[1])));
		fprintf(stdout, "%f\n", sqrt1(atoi(argv[1])));
	}
	else{
		fprintf(stdout, "%f\n", sqrt13(4));
		fprintf(stdout, "%f\n", sqrt1(4));
	}
}