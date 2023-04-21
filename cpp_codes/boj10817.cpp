#include <iostream>
using namespace std;

int main()
{
    int nums[3];
    bool sorted = false;
    cin >> nums[0] >> nums[1] >> nums[2];

    while (!sorted)
    {
        sorted = true;
        for (int i = 0; i < 2; i++)
        {
            if (nums[i] > nums[i+1])
            {
                int temp = nums[i];
                nums[i] = nums[i+1];
                nums[i+1] = temp;
                sorted = false;
            }
        }
    }

    cout << nums[1];

    return 0;
}