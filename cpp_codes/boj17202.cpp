#include <iostream>
#include <string>
using namespace std;

int ctoi(char c)
{
    return c - '0';
}

int main()
{
    string a, b;
    string temp = "";

    cin >> a;
    cin >> b;

    while (a.length() > 1)
    {
        temp = "";
        temp += to_string((ctoi(a[0]) + ctoi(b[0])) % 10);
        for (int i = 1; i < a.length() - 1; i++)
        {
            temp += to_string((ctoi(a[i]) + ctoi(b[i-1])) % 10);
            temp += to_string((ctoi(a[i]) + ctoi(b[i])) % 10);
        }
        temp += to_string((ctoi(a[a.length()-1]) + ctoi(b[a.length()-2])) % 10);
        if (a.length() == b.length())
            temp += to_string((ctoi(a[a.length()-1]) + ctoi(b[b.length()-1])) % 10);
        
        a = "";
        b = "";
        for (int i = 0; i < temp.length(); i++)
        {
            if (!(i % 2))
                a += temp[i];
            else
                b += temp[i];
        }
    }

    cout << a[0] << b[0] << endl;

    return 0;
}