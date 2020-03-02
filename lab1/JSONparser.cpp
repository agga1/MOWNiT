//
// Created by Agnieszka on 02/03/2020.
//
#include "JSONparser.h"
#include <iostream>
using namespace std;
string parseArray(float *ar, int N){
    string res="[";
    for(int i=0;i<N-1;i++){
        res+=to_string(ar[i])+", ";
    }
    res+=to_string(ar[N-1]);
    res+="]";
    return res;
}