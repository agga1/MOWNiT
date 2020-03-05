//
// Created by Agnieszka on 03/03/2020.
//

#include <iostream>
#include <vector>
#include <chrono>
#include <fstream>
#include <sstream>
#include <iomanip>
#include "JSONparser.h"
using namespace std;
template <class T>
//for each r in rs calculate values to which xn converges
T logistic_map_bif_diagram(T x0, T *rs, int rs_len){ //
    for(int i=0;i<rs_len;i++){

    }
    bif_diagram[0]=x0;
    for(int i=1;i<100;i++){
        bif_diagram[i]=r*bif_diagram[i-1](1-bif_diagram[i-1]);
    }
    return bif_diagram;
}
template <class T>
//// calculate trajectory of first @res_len iterations
void logistic_map_trajectory(T x0, T r, T *res, int res_len){
    res[0]=x0;
    for(int i=1; i<res_len; i++){
        res[i] = res[i-1]*r*(1-res[i-1]);
    }
}
template <typename T>
int iter_to_0(T x0, T r=4){
    int it = 0;
    T xprev =  x0;
    T xcurr;
    while(xprev>0){
        xcurr = r*xprev(1-xprev);
        xprev = xcurr;
        it++;
    }
    return it;
}
int main(){
    // compare trajectories between single and double precision
    float x0 = 0.7f, r=3.75f;
    int N = 70;
    auto *t_float = new float[N];
    logistic_map_trajectory<float>(x0, r, t_float, N);
    auto *t_double = new double[N];
    logistic_map_trajectory<double>((double)x0, (double)r, t_double, N);

    export_to_file("t_float.json", parseArray(t_float, N));
    export_to_file("t_double.json", parseArray<double>(t_double, N));



    // counting nr of iterations needed for reaching 0 for r=4 and different x0s (single prec.)

}