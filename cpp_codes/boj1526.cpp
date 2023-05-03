#include <iostream>
#include <string>
using namespace std;

#define MAX(x, y) x > y ? x : y

int main()
{
    string num;
    int max_num = 0;
    bool poss;

    cin >> num;
    for (int i = 4; i <= stoi(num); i++)
    {
        poss = true;
        for (int j = 0; j < to_string(i).length(); j++)
            if (to_string(i)[j] != '4' && to_string(i)[j] != '7')
            {
                poss = false;
                break;
            }
        if (poss)
            max_num = MAX(max_num, i);
    }
    
    cout << max_num << endl;
    return 0;
}