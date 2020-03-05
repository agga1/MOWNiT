//
// Created by Agnieszka on 03/03/2020.
//

#include <iostream>
#include <vector>
#include <chrono>
#include <fstream>
#include <iomanip>
#include "JSONparser.h"
using namespace std;
template <typename T>
//for each r in rs calculate values to which xn converges
T logistic_map_bif_diagram(T x0, T *rs, int rs_len){ //
    for(int i=0;i<rs_len;i++){

    }
    bif_diagram[0]=x0;
    for(int i=1;<100;i++){
        bif_diagram[i]=r*bif_diagram[i-1](1-bif_diagram[i-1]);
    }
    return bif_diagram;
}
template <typename T>
//// calculate trajectory of first @res_len iterations
void logistic_map_trajectory(T x0, T r, T *res, int res_len){
    res[0]=x0;
    for(int i=1; i<res_len; i++){
        res[i]=r*res[i-1](1-res[i-1]);
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

}