//
// Created by Agnieszka on 02/03/2020.
//
#include <iostream>
#include <vector>
#include <chrono>
#include <fstream>
#include "JSONparser.h"
using namespace std;
template <typename T>
T zeta_fwd(T s, int n) // Riemann zeta function counted in ascending order
{
    T res = 0.0;
    for(int k=1; k<=n; k++){
        cout << "val nr "<<k<<" = "<<1/(pow(k, s))<<endl;
        cout<<" \nres before "<<res;
        res += 1/(pow(k, s));
        cout<<" res after "<<res;
    }
    return res;
}

template <typename T>
T eta_fwd(T s, int n){ // Dirichlet eta function counted in ascending order

}
template <typename T>
T zeta_bwd(T s, int n) // Riemann zeta function counted in descending order
{
    T res = 0.0;
    for(int k=n; k>=1; k--){
        cout << "val nr "<<k<<" = "<<1/(pow(k, s))<<endl;
        cout<<"\nres before "<<res;
        res += 1/(pow(k, s));
        cout<<"res after "<<res;
    }
    return res;
}

template <typename T>
T eta_bwd(T s, int n){ // Dirichlet eta function counted in descending order

}



int main() {
    float s[] = {2,3.6667,5,7.2,10};
    int n[] = {50,100,200,500,1000};
//    int el_nr =  (sizeof(n)/sizeof(*n));
int el_nr = 2;
    for(int i=0; i<el_nr; i++){
        cout<< "\n____Results for n= "<<n[i]<<" ____";
        cout << "\nzeta forward: "<<zeta_fwd<float>(2, n[i]);
        cout << "\nzeta backward: "<<zeta_bwd<float>(2, n[i]);

    }

}