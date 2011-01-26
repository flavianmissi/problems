#include <stdio.h>
#include <iostream>
using namespace std;

int main(void){
    int n;
    int x;
    int soma = 0;
    scanf("%d", &n);
    if(n >= 0 and n <= 500){
        for(int i = 1; i <= n; i++)
        {
            scanf("%d", &x);
            soma += x;
        }
    }
    cout << soma;
    
}
