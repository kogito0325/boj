#include <iostream>
using namespace std;

#define MAX(x, y) x > y ? x : y

int main()
{
    int cnt, s, b, max_s, max_b;
    
    for (cin >> cnt; cnt > 0; cnt--)
    {
        cin >> s >> b;
        max_s = max_b = 0;
        while (s--)
        {
            int temp; cin >> temp;
            max_s = MAX(max_s, temp);
        }
        while (b--)
        {
            int temp; cin >> temp;
            max_b = MAX(max_b, temp);
        }
        if (max_s >= max_b)
            cout << "S" << endl;
        else if (max_s < max_b)
            cout << "B" << endl;
        else
            cout << "C" << endl;
    }

    return 0;
}