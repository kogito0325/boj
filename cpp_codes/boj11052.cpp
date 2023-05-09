#include <iostream>
using namespace std;

const int MAXN = 1001;
int dp[MAXN][MAXN];
int cost[MAXN];

int main()
{
    int n;
    cin >> n;

    for (int i = 1; i <= n; i++)
    {
        cin >> cost[i];
        for (int j = 1; j <= n; j++)
        {
            if (i <= j)
                dp[i][j] = max(cost[i] + dp[i][j - i], dp[i-1][j]);
            else
                dp[i][j] = dp[i-1][j];
        }
    }

    cout << dp[n][n] << endl;
    
    return 0;
}

