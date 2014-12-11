#include <iostream>
#include <cmath>

int chop(int, int*, int);

int main(int argc, char** argv){
	int array[10] = {1,2,3,4,5,6,7,8,9,10};
	int sizeOfArray = sizeof(array)/sizeof(array[0]);
	std::cout << chop(8, array, sizeOfArray) << std::endl;
	std::cout << chop(1, array, sizeOfArray) << std::endl;
	std::cout << chop(3, array, sizeOfArray) << std::endl;
}

int chop(int x, int* array, int size){
	int min = 0, max = size;
	
	while(true){
		int y = floor((min + max) / 2);
		
		if(min > max)
			return -1;
		
		if(array[y] > x)
			max = y;
		else if(array[y] < x)
			min = y;
		else
			return y;
	}
	
}