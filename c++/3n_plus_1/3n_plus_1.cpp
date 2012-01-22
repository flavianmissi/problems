#include <iostream>
using namespace std;

int even(int n) {
    return n / 2;
}

int odd(int n) {
    return n * 3 + 1;
}

int main() {
    bool flag;
    int i, j, n, cycle_length, max_cycle_length;
    cin >> i;
    cin >> j;
    max_cycle_length = 1;

    for (i; i <= j; i++) {
        cycle_length = 1;
        n = i;

        while (n != 1) {
            if (n % 2 == 0)
                n = even(n);
            else
                n = odd(n);

            cycle_length++;

            if (cycle_length > max_cycle_length)
                max_cycle_length = cycle_length;
        }
    }

    cout << max_cycle_length << endl;
}
