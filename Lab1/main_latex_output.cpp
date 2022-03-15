#include <iostream>
#include <string.h>
#include <sstream>
#include "math.h"

using namespace std;
/*
Wyznaczyć wartości funkcji f(x) = sqrt(x^2+1)-1, g(x) = x^2/sqrt(x^2+1)+1
argumentu x = 8^-1, 8^-2, 8^-3, .... Sprawdzić, czy wyznaczone wartości dla obu funkcji
(matematycznie tożsamych) są takie same i spróbować uzasadnić ewentualne różnice.
Jak obliczać z kolei wartości dla dużych argumentów (np. x bliskiego największej
liczbie typu double) ?

 */


double f(double x) {
    return sqrt(pow(x, 2) + 1) - 1;
}

double g(double x) {
    return pow(x, 2) / (sqrt(pow(x, 2) + 1) + 1);
}

float f_float(float x) {
    return sqrtf(powf(x, 2) + 1) - 1;
}

float g_float(float x) {
    return powf(x, 2) / (sqrtf(powf(x, 2) + 1) + 1);
}


long double f_long(long double x) {
    return sqrtl(powl(x, 2) + 1) - 1;
}

long double g_long(long double x) {
    return powl(x, 2) / (sqrtl(powl(x, 2) + 1) + 1);
}
int common_digits(long double fx, long double gx, int precision=20){
    std::ostringstream fx_stream;
    fx_stream.precision(precision);
    fx_stream  << fx;

    std::ostringstream gx_stream;
    gx_stream.precision(precision);
    gx_stream  << gx;

    string fx_s = fx_stream.str();
    string gx_s = gx_stream.str();

    int common_digits = 0;
    while (fx_s[common_digits] == gx_s[common_digits]){
        common_digits++;
    }
    return common_digits-2;
}

int test_float(int max_iterations) {
    for (int i = 0; i < max_iterations; ++i) {
        float a = 8;
        long double x = powl(a, -i);
        float fx = f_float(x);
        float gx = g_float(x);
        double diff = fx - gx;
        int cd = common_digits(fx, gx);
        cout << x << "&" << fx << "&" << gx << "&" << cd << "\\\\ \n";
//        cout << "g(x) - f(x)" << gx-fx << "\n";
//        if (fx ==0)
//            return i;
    }
    return 0;
}







int test_double(int max_iterations){
    for (int i = 0; i < max_iterations; ++i) {
        double a = 8;
        long double x = powl(a, -i);
        double fx = f(x);
        double gx = g(x);

        int cd = common_digits(fx, gx);
        cout << x << "&" << fx << "&" << gx << "&" << cd << "\\\\ \n";
//        cout << "g(x) - f(x)" << gx-fx << "\n";
//        if (fx ==0)
//            return i;
    }
    return 0;
}

int test_long(int max_iterations){
    for (int i = 0; i < max_iterations; ++i) {
        long double a = 8;
        long double x = powl(a, -i);
        long double fx = f_long(x);
        long double gx = g_long(x);
        int cd = common_digits(fx, gx);
        cout << x << "&" << fx << "&" << gx << "&" << cd << "\\\\ \n";
//        cout << "g(x) - f(x):   " << gx-fx << "\n";
//        if (fx ==0)
//            return i;

    }
    return 0;
}

int main() {
    cout.precision(15);
    /*
         \begin{center}
        \begin{tabular}{ c c c }
        cell1 & cell2 & cell3 \\
        cell4 & cell5 & cell6 \\
        cell7 & cell8 & cell9
        \end{tabular}
        \end{center}

         */
    cout << "------------- TESTING FLOAT ------------ \n";
    cout << "\\begin{center} \n \\begin{tabular}{c c c c} \n";
//    test_float(100);
//    test_double(15);
    test_long(15);
    cout << "   \\end{tabular}\n\\end{center}\n";

//    cout << "------------- TESTING DOUBLE ------------ \n"<< test_double(15) << endl;
//    cout << "------------- TESTING LONG ------------ \n"<< test_long(100) << endl;


    return 0;
}




