#import <iostream>

std::string remove(std::string str, int pos){
	return str.erase(pos);
}

int main(int argc, char** argv){
	int cases = 0;
	std::cin >> cases;
	
	for(int i = 0; i < cases; i++){
		int count = 0;
		std::string inputStr = "";
		std::cin.clear();
		std::cin.ignore(INT_MAX);
		std::cin >> inputStr;
		
		int x = 0, y = inputStr.length();
		
		while (x < y){
			while(x + 1 < y && inputStr[x] == inputStr[x + 1]){
				inputStr = remove(inputStr, x + 1);
				y--;count++;
			}
			x++;
		}
	}
}