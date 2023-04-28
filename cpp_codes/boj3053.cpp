#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    double r, res1, res2;
    cin >> r;

    r *= r;
    res1 = r * M_PI;
    res2 = r * 2;

    cout.precision(15);
    cout << res1 << endl << res2;

    return 0;
}