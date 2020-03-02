#include <iostream>
#include <math.h>
#include <vector>
#include <chrono>
#include <fstream>
#include "JSONparser.h"
using namespace std;

const int N = 10000000;
float v = 0.53125;
vector<float> vct(N, v);

float easy_sum(){
    float sum = 0;
    for(auto val:vct)
        sum+= val;
    return sum;
}
float *sum_with_report(int step = 25000){
    auto *rel_err = new float[N/step];
    float sum = 0;
    for(int i =0 ;i<N/step;i++){
        for(int j=0; j<step; j++)
            sum+=v;
        float expected = v*(i+1)*25000;
        float actual = sum;
        rel_err[i] = abs((actual-expected)/expected);
    }
    return rel_err;
}
float merge_sum_body( int start, int end){
    if(start==end) return 0;
    if(start==end-1) return vct[start];
    int mid = start+(end-start)/2;
    return merge_sum_body(start, mid) + merge_sum_body(mid, end);
}
float merge_sum(){
    return merge_sum_body(0, vct.size());
}

void eval_sum(float eval_func()){
    chrono::steady_clock::time_point begin = chrono::steady_clock::now();
    float sum = eval_func();
    chrono::steady_clock::time_point end = chrono::steady_clock::now();

    cout<<"\nexperimentally determined x: "<< sum;
    cout<<"\nrelative error: "<< abs((sum-v*N)/(v*N));
    cout<<"\nabsolute error: "<< abs((sum-v*N));
    cout<<"\nelapsed time: "<< chrono::duration_cast<chrono::microseconds>(end - begin).count() << "[mikroseconds]" << endl;
}

int main() {
    cout<<"______Sum obtained using naive algorithm_____ ";
    eval_sum(easy_sum);
    cout<<"\n______Sum obtained using recursive algorithm_____ ";
    eval_sum(merge_sum);

/*
 * exporting progress of relative error for naive sum algorithm to JSON file.
 */
    int step = 25000;
    ofstream sum_error;
    sum_error.open("sum_error_progress.json");
    sum_error <<parseArray(sum_with_report(step), N/step);
    sum_error.close();
    return 0;
}



