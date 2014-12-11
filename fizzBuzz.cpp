#import <iostream>

void fizzBuzz(){
	int counter = 1;
	
	for(;counter <= 100; counter++){
		std::cout << (counter % 3 == 0 && counter % 5 == 0 ? "fizzbuzz" : (counter % 3 == 0 ? "fizz" : (counter % 5 == 0 ? "buzz" : std::to_string(counter)))) << std::endl;
	}
}

int main(int argc, char** argv){
	fizzBuzz();
}