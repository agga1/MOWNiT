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
T zeta_fwd(T s, int n, bool print=false) // Riemann zeta function counted in ascending order
{
    T res = 0.0f;
    for(int k=1; k<=n; k++){
        float tmp = res+ (float)1/(pow(k, s));

        if(print){
        cout << "\nval nr "<<k<<" = "<<(float)1/(pow(k, s));
            cout<<"\ndiff nr "<<k<< "= "<<tmp-res;
        }
        res = tmp;
    }
    return res;
}

template <typename T>
T eta_fwd(T s, int n, bool print=false){ // Dirichlet eta function counted in ascending order
    T res = 0.0;
    for(int k=1;k<=n;k++){
        T el = (T)pow(-1, k-1)/(T)pow(k, s);
        T tmp = res+el;
        if(print){
            cout << "\nval nr "<<k<<" = "<<el;
            cout<<"\ndiff nr "<<k<< "= "<<tmp-res;
        }
        res = tmp;
    }
    return res;
}
template <typename T>
T zeta_bwd(T s, int n, bool print=false) // Riemann zeta function counted in descending order
{
    T res = 0.0;
    for(int k=n; k>=1; k--){
        float tmp = res+ (float)1/(pow(k, s));
        if(print){
            cout << "\nval nr "<<k<<" = "<<(float)1/(pow(k, s));
            cout<<"\ndiff nr "<<k<< "= "<<tmp-res;
        }
        res = tmp;
    }
    return res;
}

template <typename T>
T eta_bwd(T s, int n, bool print=false){ // Dirichlet eta function counted in descending order
    T res = 0.0;
    for(int k=n;k>=1;k--){
        T el = (T)pow(-1, k-1)/(T)pow(k, s);
        T tmp = res+el;
        if(print){
            cout << "\nval nr "<<k<<" = "<<el;
            cout<<"\ndiff nr "<<k<< "= "<<tmp-res;
        }
        res = tmp;
    }
    return res;
}



int main() {
//    float s[] = {2,3.6667,5,7.2,10};
    float s[] = {4};

//    int n[] = {50,100,200,500,1000};
    int n[] = {200};

    int n_nr =  (sizeof(n)/sizeof(*n));
    int s_nr =  (sizeof(n)/sizeof(*n));

    for(int j=0;j<s_nr;j++) {
        cout<<"\n____________Results for s= "<<s[j]<<"__________";
        cout<<setprecision(7);
        for (int i = 0; i < n_nr; i++) {
            auto resf = zeta_fwd<float>(s[j], n[i]);
            auto resb = zeta_bwd<float>(s[j], n[i]);
            cout << "\n____Results for n= " << n[i] << " ____";
            cout << "\neta forward: " << resf;
            cout << "\neta backward: " << resb;

//            cout << "\nzeta backward: " << zeta_bwd<float>(2, n[i])-zeta_bwd<float>(7.2, 10);
        }
    }
//    cout<< "\n\n---------DOUBLE PRECISION-----------";
//    for(int j=0;j<s_nr;j++) {
//        cout<<"\n____________Results for s= "<<s[j]<<"__________";
//        cout<<setprecision(9);
//        for (int i = 0; i < n_nr; i++) {
//            auto resf = eta_fwd<double>(s[j], n[i]);
//            auto resb = eta_bwd<double>(s[j], n[i]);
//            cout << "\n____Results for n= " << n[i] << " ____";
//            cout << "\neta forward: " << resf;
//            cout << "\neta backward: " << resb;
//
//            cout << "\nzeta backward: " << zeta_bwd<float>(2, n[i])-zeta_bwd<float>(7.2, 10);
//        }
//    }


}