#import <iostream>
#import <string>

void fizzBuzz(int upperLimit){
	for(int counter = 1;counter <= upperLimit; counter++){
        std::string toPrint = "";
        
        // New version only requires two modulo operations and two ternary operations
        counter % 3 == 0 ? toPrint += "fizz" : "";
        counter % 5 == 0 ? toPrint += "buzz" : "";
        
        std::cout << (toPrint.length() == 0 ? std::to_string(counter) : toPrint) << std::endl;
        
        // Previous way I thought was awesome
		//std::cout << (counter % 3 == 0 && counter % 5 == 0 ? "fizzbuzz" : (counter % 3 == 0 ? "fizz" : (counter % 5 == 0 ? "buzz" : std::to_string(counter)))) << std::endl;
	}
}

// This does not check to ensure the argument is a number, this is just made to be fast
int main(int argc, char** argv){
	if(argc < 2)
		fizzBuzz(100);
	else
		fizzBuzz(atoi(argv[1]));
}
