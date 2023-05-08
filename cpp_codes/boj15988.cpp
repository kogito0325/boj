#include <iostream>
using namespace std;

long long dp[1000001];

int main()
{
    int n, i = 4;
    dp[0] = 0;
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;

    for (cin >> n; n > 0; n--)
    {
        int t;
        cin >> t;

        for (; i <= t; i++)
            dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009;

        cout << dp[t] << endl;
    }

    return 0;
}