// C++ PROGRAM FOR RC4 CRYPTOGRAPHIC SYSTEM
// CODED BY PRAJWAL SUNDAR, CSE-B, THIRD YEAR, ROLL NO 106121092

#include "bits/stdc++.h"
using namespace std;

int main()
{
    cout << "Welcome to C++ RC4 Cyrptosystem Key Stream Generator !" << endl << endl;

    int n; // size of state array
    cout << "Enter the size of your state array : ";
    cin >> n;
    vector<int> S (n); // State-Array
    for (int i = 0; i < n; i++) S[i] = i;

    int k; // size of key array
    cout << "Enter the size of your key array : ";
    cin >> k;
    vector<int> K (k); // Key-Array
    cout << "Enter the elements of your key array : ";
    for (int i = 0; i < k; i++) cin >> K[i];

    vector<int> T (n); // T-array
    for (int i = 0; i < n; i++) T[i] = K[i%k];

    // Key-Generation
    int i, j = 0;
    for (i = 0; i < n; i++)
    {
        j = (j + S[i] + T[i]) % n;
        swap(S[i], S[j]);
    }

    // Stream-Generation
    int l;
    cout << "Enter the length of your desired key-stream : ";
    cin >> l;
    i = j = 0;
    vector<int> keys (l);
    for (int x = 0; x < l; x++)
    {
        i = (i+1) % n;
        j = (j+S[i]) % n;
        swap(S[i], S[j]);
        int t = (S[i] + S[j]) % n;
        keys[x] = S[t];
    }

    cout << "The Generated Key Stream is : ";
    for (int & key : keys) cout << key << " ";

    cout << endl << endl << "Thank you for using C++ RC4 Cyrptosystem Key Stream Generator. Bye Bye !";
}