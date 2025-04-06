// C++ PROGRAM FOR EL-GAMAL CRYPTOGRAPHIC SYSTEM
// CODED BY PRAJWAL SUNDAR, CSE-B, THIRD YEAR, ROLL NO 106121092
#include "bits/stdc++.h"
using namespace std;

int inverse(int R2, int R1) // Inverse using Extended Euclidean Algorithm
{
    int D = R1, T1 = 0, T2 = 1, Q, R, T;
    while (R2) // Run algorithm as long as R2 != 0
    {
        Q = R1 / R2; R = R1 % R2;
        T = T1 - Q*T2;
        R1 = R2; R2 = R;
        T1 = T2; T2 = T;
    }
    if (R1 != 1) return 0; // HCF != 1, so inverse does not exist
    else if (T1 > 0) return T1 % D; // positive remainder
    else return D - (-T1 % D); // convert negative remainder to positive remainder
}

int mod(int b, int e, int q) // Modular Exponentiation
{
    vector<int> V = {b}; // store results of powers of 2
    int r = b;
    while (e >= pow(2, V.size()))
    {
        r = (r*r) % q; // repeated squaring and taking modulus
        V.push_back(r);
    }
    int p = V.size()-1, n = e; r = 1;
    while (p >= 0)
    {
        if (n >= pow(2, p)) // consider the current power
        {
            n -= pow(2, p);
            r = (r*V[p]) % q; // consider remainder
        }
        p--;
    }
    return r;
}

int main() // Main Function
{
    cout << "Welcome to C++ ElGamal Cryptosystem !" << endl << endl;

    int q, a; // global public elements
    cout << "Enter the global prime number 'q' : ";
    cin >> q;
    cout << "Enter the primitive root of q, 'a' : ";
    cin >> a;

    int M; // plain text
    cout << "Enter your plain text (less than q) : ";
    cin >> M;

    // Key Generation
    int XA;
    cout << "Enter your choice of private key (less than q-1) : ";
    cin >> XA;
    int YA = mod(a, XA, q); // public key

    // Encryption using Public Key
    int k; // random number
    cout << "Enter your choice of 'k' (less than q) : ";
    cin >> k;
    int K = mod(YA, k, q); // one-time-key
    int C1 = mod(a, k, q); // cipher-text-part-1
    int C2 = (K*M) % q; // cipher-text-part-2
    cout << endl << "Cipher Text = (" << C1 << "," << C2 << ")";

    // Decryption using Private Key
    int KD = mod(C1, XA, q); // re-generate one-time-key
    int PT = (C2 * inverse(K, q)) % q; // plain-text
    cout << endl << "Regenerated Plain Text = " << PT;

    // Conclusion
    cout << endl << endl << "Thank you for using C++ ElGamal Cryptosystem. Bye Bye !";
}