#include <iostream>
using namespace std;

int main()
{
    const int MAX = 26;
    char input[100];
    int list[MAX] = {0};

    cin >> input;
    for (int i = 0; input[i] != 0; i++)
    {
        list[input[i] - 'a']++;
    }

    for (int i = 0; i < MAX; i++)
    {
        cout << list[i] << ' ';
    }

    return 0;
}