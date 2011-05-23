#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

string itos(int n){
    stringstream ss;
    ss << n;
    return ss.str();
}

string ctos(char c){
    stringstream ss;
    ss << c;
    return ss.str();
}

bool is_palindrome(int number){
    string original (itos(number));
    string reverse;
    string::reverse_iterator rit;
    for(rit = original.rbegin(); rit < original.rend(); rit++){
        reverse.append(ctos(*rit));
    }
    if(original.compare(reverse) == 0){
        return true;
    }
    return false;
}

int largest_palindrome(){
    //palindromes.push_back(2);
    int biggest = 111;
    for(int i = 111; i <= 999; i++){
        for(int j = 111; j <= 999; j++){
            if(is_palindrome(i*j)){
                if(i*j > biggest){
                    biggest = i*j;
                }
            }
        }
    }
    return biggest;
}

int main(){
    cout << "The largest palindrome is: " << largest_palindrome() << endl;
    return 0;
}
