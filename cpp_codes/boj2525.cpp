#include <iostream>
using namespace std;

int main()
{
    int hour, min, addmin;
    cin >> hour >> min;
    cin >> addmin;

    min += addmin;
    hour += min / 60;
    hour %= 24;
    min %= 60;

    cout << hour << ' ' << min;

    return 0;
}