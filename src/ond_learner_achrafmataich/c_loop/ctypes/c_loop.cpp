#include <iostream>

using namespace std;

extern "C"
{
    char* loopy(int iter)
    {
        cout << "Hello " << iter << endl;
        for (int i = 0; i < iter; i++)
        {
            continue;
        }
        return "Done";
    }
}