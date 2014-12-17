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