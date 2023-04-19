#include <iostream>
using namespace std;

int main()
{
    int num1;
    char num2[4];
    int inum2[3];
    cin >> num1 >> num2;

    for (int i = 2; i >= 0; i--)
    {
        inum2[i] = (int)num2[i] - (int)'0';
        cout << num1 * inum2[i] << endl;
    }

    cout << num1 * (inum2[0]*100 + inum2[1]*10 + inum2[2]);

    return 0;
}