#include <iostream>
#include <vector>
#include <memory.h>
using namespace std;


bool visit[1001];
int max_p = -1;
int ans;

int main()
{   
    int n;
    cin >> n;

    vector<vector<int>> v(n+1, vector<int>(n+1));

    for (int i = 0; i < n; i++)
        for (int j = 0; j < 5; j++)
            cin >> v[i][j];

    for (int i = 0; i < n; i++)
    {
        memset(visit, 0, sizeof(visit));
        int cnt = 0;
        for (int j = 0; j < 5; j++)
        {
            int class_num = v[i][j];
            for (int k = 0; k < n; k++)
            {
                if (i != k && class_num == v[k][j])
                {
                    if (!visit[k])
                    {
                        visit[k] = 1;
                        cnt++;
                    }
                }
            }
        }
        if (cnt > max_p)
        {
            max_p = cnt;
            ans = i+1;
        }
    }
    cout << ans;

    return 0;
}