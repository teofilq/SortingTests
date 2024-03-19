#include <iostream>
#include <fstream>
#include <random>
#include <chrono>

using namespace std;

int main() {
    unsigned seed = chrono::system_clock::now().time_since_epoch().count();
    default_random_engine generator(seed);

    ofstream f1("tests.txt");

    for (int N = 1000; N <= 10000000; N *= 10) { // pentru N de la 1000 la 10.000.000
        for (int MAXIM = 1000; MAXIM <= 10000000; MAXIM *= 10) { // și MAXIM de la 1000 la 10.000.000
            uniform_int_distribution<int> distribution(0, MAXIM - 1);

            f1 << N << endl << MAXIM << endl;
            for (int i = 0; i < N; i++) {
                f1 << distribution(generator) << " ";
            }
            f1 << endl;
        }
    }

    f1.close(); 

    cout << "Generare completă. Vectorii au fost salvați în 'tests.txt'." << endl;

    return 0;
}
