#include <iostream>
using namespace std;

int main()
{
    int day;
    int carNum;
    int cnt = 0;

    cin >> day;

    for (int i = 0; i < 5; i++)
    {
        cin >> carNum;
        if (carNum == day)
            cnt++;
    }

    cout << cnt;

    return 0;
}