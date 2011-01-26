#include <stdio.h>
#include <iostream>
using namespace std;


int main(void)
{
    string letters[8];
    letters[0] = "ABC"; letters[1] = "DEF"; letters[2] = "GHI";
    letters[3] = "JKL"; letters[4] = "MNO"; letters[5] = "PQRS";
    letters[6] = "TUV"; letters[7] = "WXYZ";

    char c[30]; 
    int i;
    i = 0;

    cout << "Enter some chars...";

    while(scanf("%c\n", &c[i]) != EOF)
    {
       cout << "you typed the char" << c[i] << endl;
       i++; 
    }

    return 0;
}
