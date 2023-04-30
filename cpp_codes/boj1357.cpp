#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int rev(string str)
{
    reverse(str.begin(), str.end());
    int res = stoi(str);
    return res;
}

int main()
{
    string num1, num2;
    cin >> num1 >> num2;
    int res = rev(num1) + rev(num2);
    cout << rev(to_string(res));

    return 0;
}