#include <iostream>
#include <cstring>
using namespace std;

int main()
{
    char str[501];
    while (true)
    {
        cin.getline(str, 501);
        if (!strcmp(str, "END"))
            break;
    
        int i = 0;

        for (i = strlen(str)-1; i >= 0; i--)
            cout << str[i];
        cout << endl;
    }
    return 0;
}