#include "stdlib.h"
#include "stdio.h"

double sqrt13( int n )
{
	// For loop to get the square root value of the entered number.
	for( int i = 0; i < n; i++)
	{
		x = 0.5 * ( x+a / x );
	}
 
	return x;
}

int main(int argc, char** argv){
	if(argc > 1){
		fprintf(stdout, "%f\n", sqrt13(atoi(argv[1])));
	}
	else{
		fprintf(stdout, "%f\n", sqrt13(4));
	}
}
