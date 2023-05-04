#include <iostream>
using namespace std;

int main()
{   
    int rng, cnt=0;
    string word;
    for (cin >> rng; rng > 0; rng--)
    {
        bool check['z' - 'a'+1] = {false};
        bool is_poss = true;
        char now_ch = '0';
        cin >> word;
        for (int i = 0; i < word.length(); i++)
        {
            if (word[i] != now_ch)
            {
                if (!check[word[i] - 'a'])
                {
                    check[word[i] - 'a'] = true;
                    now_ch = word[i];
                    continue;
                }
                is_poss = false;
                break;
            }
        }
        if (is_poss)
            cnt++;
    }
    cout << cnt << endl;

    return 0;
}