#include <iostream>
using namespace std;

int main()
{   
    struct point
    {
        int x = 0;
        int y = 0;
    };

    struct point arr[3];

    for (int i = 0; i < 3; i++)
    {
        cin >> arr[i].x >> arr[i].y;
    }

    int ans[2];
    for (int i = 0; i < 3; i++)
    {
        int cnt_x = 0, cnt_y = 0;
        for (int j = 0; j < 3; j++)
        {
            if (arr[i].x == arr[j].x)
                cnt_x++;
            if (arr[i].y == arr[j].y)
                cnt_y++;
        }
        if (cnt_x == 1)
            ans[0] = arr[i].x;
        if (cnt_y == 1)
            ans[1] = arr[i].y;
    }

    cout << ans[0] << ' ' << ans[1];

    return 0;
}