//
// Created by Agnieszka on 02/03/2020.
//
#include <iostream>
#include <vector>
#include <chrono>
#include <fstream>
#include <iomanip>
#include "JSONparser.h"
using namespace std;

template <typename T>
// Riemann zeta function counted in ascending order
T zeta_fwd(T s, int n)
{
    T res = 0.0f;
    for(int k=1; k<=n; k++){
        res = res + (float)1/(pow(k, s));
    }
    return res;
}

template <typename T>
// Dirichlet eta function counted in ascending order
T eta_fwd(T s, int n){
    T res = 0.0;
    for(int k=1;k<=n;k++){
        T next = (T)pow(-1, k-1)/(T)pow(k, s);
        res = res+next;
    }
    return res;
}
template <typename T>
// Riemann zeta function counted in descending order
T zeta_bwd(T s, int n) {
    T res = 0.0;
    for(int k=n; k>=1; k--){
        res = res+ (float)1/(pow(k, s));
    }
    return res;
}

template <typename T>
// Dirichlet eta function counted in descending order
T eta_bwd(T s, int n){
    T res = 0.0;
    for(int k=n;k>=1;k--){
        T next = (T)pow(-1, k-1)/(T)pow(k, s);
        res = res+next;
    }
    return res;
}



int main() {
    float s[] = {2,3.6667,5,7.2,10};
//    float s[] = {4};

    int n[] = {50,100,200,500,1000};
//    int n[] = {200};

    int n_nr =  (sizeof(n)/sizeof(*n));
    int s_nr =  (sizeof(n)/sizeof(*n));

//    cout<<"\n\n________________FLOAT________________";
//
//    for(int j=0;j<s_nr;j++) {
//        cout<<"\n\n____________Results for s= "<<s[j]<<"__________";
//        cout<<setprecision(14);
//        for (int i = 0; i < n_nr; i++) {
//            auto resf = zeta_fwd<double>(s[j], n[i]);
//            auto resb = zeta_bwd<double>(s[j], n[i]);
//            cout << "\n____Results for n= " << n[i] << " ____";
//            cout << "\nzeta forward: " << resf;
//            cout << "\nzeta backward: " << resb;
//
//        }
//    }
    cout<< "\n\n---------DOUBLE PRECISION-----------";
    for(int j=0;j<s_nr;j++) {
        cout<<"\n____________Results for s= "<<s[j]<<"__________";
        cout<<setprecision(8);
        for (int i = 0; i < n_nr; i++) {
            auto resf = eta_fwd<float>(s[j], n[i]);
            auto resb = eta_bwd<float>(s[j], n[i]);
            cout << "\n____Results for n= " << n[i] << " ____";
            cout << "\neta forward: " << resf;
            cout << "\neta backward: " << resb;

        }
    }


}