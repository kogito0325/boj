#include <iostream>
using namespace std;

long long dp[100001];

int main()
{
    int n, i = 5;
    dp[0] = 0;
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 2;
    dp[4] = 3;

    for (cin >> n; n > 0; n--)
    {
        int t;
        cin >> t;

        for (; i <= t; i++)
        {
            if (i % 2)
                dp[i] = dp[i-1];
            else
                dp[i] = (dp[i-1] + dp[i-3] + dp[i-5]) % 1000000009;
        }

        cout << dp[t] << endl;
    }

    return 0;
}
