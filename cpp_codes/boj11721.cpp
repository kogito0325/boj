#include <iostream>
using namespace std;

int main()
{
    string str;
    cin >> str;
    for (int i = 0; i < int(str.length()); i++)
    {
        cout << str[i];
        if (!((i+1) % 10))
            cout << endl;
    }

    return 0;
}