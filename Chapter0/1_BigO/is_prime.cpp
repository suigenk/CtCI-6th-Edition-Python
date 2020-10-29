#include <bits/stdc++.h>

using namespace std;

// Complete the primality function below.
string primality(int n) {
    // Declare string to store result.
    string result;

    // Use sieve of Eratosthenes.
    // At first we calculate \sqrt{n}.
    // Note: we ceil value.
    int sqrt = std::ceil(std::sqrt(n));

    // To iterate include n, add + 1.
    sqrt += 1;

    // Now we iterate from 2 to \sqrt{n}.
    for (int i = 2; i < sqrt; i++) {
        // If i is divisor of n, n is not prime.
        if ((n % i) == 0) {
            result = "Not prime";
            break;
        } else {
            result = "Prime";
        }
    }

    // We take care special int.
    // 1 is not prime.
    if (n == 1) {
        result = "Not prime";
    // 2 is the only prime for even.
    } else if (n == 2) {
        result = "Prime";
    }
    return result;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int p;
    cin >> p;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int p_itr = 0; p_itr < p; p_itr++) {
        int n;
        cin >> n;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        string result = primality(n);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}