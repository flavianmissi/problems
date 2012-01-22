#include <iostream>
#include <vector>

using namespace std;


int mines_around(int pos_i, int pos_j, vector<vector<char> > field) {
    int len_i = field.size();
    int len_j = field[pos_i].size();
    int mines = 0;

    if (pos_i + 1 < len_i) {
        if(field[pos_i + 1][pos_j] == '*')
            mines++;

        if (pos_j + 1 < len_j && field[pos_i + 1][pos_j + 1] == '*') {
            mines++;
        }

        if (pos_j - 1 >= 0 && field[pos_i + 1][pos_j - 1] == '*')
            mines++;
    }

    if (pos_i - 1 >= 0) {
        if (field[pos_i - 1][pos_j] == '*')
            mines++;

        if (pos_j - 1 < len_j && field[pos_i - 1][pos_j - 1] == '*')
            mines++;

        if (pos_j + 1 < len_j && field[pos_i - 1][pos_j + 1] == '*')
            mines++;
    }

    if (pos_j + 1 < len_j && field[pos_i][pos_j + 1] == '*')
        mines++;

    if (pos_j - 1 >= 0 && field[pos_i][pos_j - 1] == '*')
        mines++;

    return mines;
}


int main () {
    vector< vector<char> > field (3, vector<char> (3, '.'));
    field[0][0] = '*';
    field[1][1] = '*';
    field[1][1] = '*';
    field[2][1] = '*';
    cout << mines_around(0, 1, field) << endl; // == 2
    cout << mines_around(0, 2, field) << endl; // == 1
    cout << mines_around(1, 0, field) << endl; // == 3
    return 0;
}


/*
 *     in   |   out
 *  * . . . | * 2 1 1
 *  . . * . | 1 2 * 1
 *  . . . . | 1 2 3 2
 *  . * . * | 2 * 2 *
 *  * . . * | * 2 3 *
 *
*/
