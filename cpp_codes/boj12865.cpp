#include <iostream>
using namespace std;

int obj_weight[101], obj_point[101], dp[101][100001];

int main()
{
	int n, max_weight;
	cin >> n >> max_weight;

	for (int i = 1; i <= n; i++)
		cin >> obj_weight[i] >> obj_point[i];

	for (int i = 1; i <= n; i++)
    {
		for (int j = 1; j <= max_weight; j++)
        {
            dp[i][j] = dp[i - 1][j];
			if (obj_weight[i] <= j)
				dp[i][j] = max(dp[i - 1][j], obj_point[i] + dp[i - 1][j - obj_weight[i]]);
		}
	}
	cout << dp[n][max_weight] << endl;
	return 0;
}