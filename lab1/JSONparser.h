//
// Created by Agnieszka on 02/03/2020.
//

#ifndef LAB1_JSONPARSER_H
#define LAB1_JSONPARSER_H

#include <string>
#include <sstream>
#include <iomanip>
#include <vector>

using namespace std;
template <class T>
string parseArray(T *ar, int N){
    string res="[";
    for(int i=0;i<N-1;i++){
        res+=to_string(ar[i])+", ";
    }
    res+=to_string(ar[N-1]);
    res+="]";
    return res;
}
template <class T>
string parseVector(vector<T> vct){
    string res="[";
    for(auto el:vct){
        res+=to_string(el)+", ";
    }
    res.pop_back();
    res.pop_back();
    res+="]";
    return res;
}
template <class T>
string parseVectorOfVs(vector<vector<T>> vcts){
    string res="[";
    for(auto v: vcts){
        res += parseVector(v);
        res+= ", ";
    }
    res.pop_back();
    res.pop_back();
    res+="]";
    return res;
}
template <class T>
string parseArrayPrecision(T *ar, int N, int prec=6){
    ostringstream strObj;
    strObj << fixed << setprecision(prec);
    strObj <<"[";
    for(int i=0;i<N-1;i++){
        strObj <<ar[i]<<", ";
    }
    strObj<<ar[N-1];
    strObj<<"]";
    return strObj.str();
}

void export_to_file(std::string filename, std::string data);
#endif //LAB1_JSONPARSER_H
