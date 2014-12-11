public List<String> nearby_words(String word){
	if(word.Length() >0)
		return concatenate_permutations(permutations(word));
	else
		return new List<String>();
}

public string[][] get_permutations(string word){
	string[word.length][26] permutations = new string[word.length][26]();
	
	int counter = 0, letter = 0;
	
	foreach(char c in word){
		letter = 0;
		foreach(char d in get_nearby_chars(c)){
			permutations[counter][letter] = d;
			letter++;
		}
		counter++;
	}
	
	return permutations;
}

public List<String> concatenate_permutations(string[][] characters){
	List<String> words = new List<String>();
	
	for(int i = 0; i < characters.length(); i++){
		for(int j = 0; j < characters[i].length(); j++){
			String temp = characters[i][0];
			temp = characters[i][j] + temp;
			words.Add(temp);
		}
	}
	
	return words;
}