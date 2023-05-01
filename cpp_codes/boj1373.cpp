#include <iostream>
#include <string>
using namespace std;

int ctoi(char chr)
{
    return chr - '0';
}

int main()
{   
    string bin;
    cin >> bin;

    int len = bin.length();
    int i = len % 3;
    if (i == 2)
        cout << ctoi(bin[0]) * 2 + ctoi(bin[1]);
    else if (i == 1)
        cout << ctoi(bin[0]);
    for (; i < len; i+=3)
        cout << ctoi(bin[i]) * 4 + ctoi(bin[i+1]) * 2 + ctoi(bin[i+2]);

    return 0;
}