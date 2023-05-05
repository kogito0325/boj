#include <iostream>
#include <algorithm>
#include <queue>
#include <cstring>
using namespace std;

const int MAX = 300;
int h, w;
int matrix[MAX][MAX];
int tmp[MAX][MAX];
bool visit[MAX][MAX];
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

void check(int y, int x)
{
	queue<pair<int, int>>q;
	q.push({ y, x });

	while (!q.empty())
    {
		int y = q.front().first;
		int x = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++)
        {
			int ny = y + dy[i];
			int nx = x + dx[i];

            if (matrix[ny][nx] != 0 && !visit[ny][nx])
            {
                q.push({ ny, nx });
                visit[ny][nx] = true;
            }
		}
	}
}

void melt_ice()
{
	memset(tmp, 0, sizeof(tmp));

	for (int y = 0; y < h; y++)
    {
		for (int x = 0; x < w; x++)
        {
			if (matrix[y][x] == 0)
                continue;

			int water_cnt = 0;

			for (int i = 0; i < 4; i++)
            {
				int ny = y + dy[i];
				int nx = x + dx[i];

				if (matrix[ny][nx] == 0)
					water_cnt++;
			}

			int val = matrix[y][x] - water_cnt;
			val = val < 0 ? 0 : val;
                tmp[y][x] = val;
		}
	}

	for (int i = 0; i < h; i++)
		for (int j = 0; j < w; j++)
			matrix[i][j] = tmp[i][j];
}

int main()
{
	cin >> h >> w;
	for (int i = 0; i < h; i++)
		for (int j = 0; j < w; j++)
			cin >> matrix[i][j];

	int time = 0;
	while (true)
    {
	    memset(visit, false, sizeof(visit));
		int cnt = 0;
		for (int i = 0; i < h; i++)
        {
			for (int j = 0; j < w; j++)
            {
				if (matrix[i][j] != 0 && !visit[i][j])
                {
					check(i, j);
					cnt++;
				}
			}
		}

		if (cnt == 0)
        {
			cout << 0 << endl;
			break;
		}

		else if (cnt >= 2)
        {
			cout << time << endl;
			break;
		}

		melt_ice();
		time++;
	}

	return 0;
}