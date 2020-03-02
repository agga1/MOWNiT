//
// Created by Agnieszka on 02/03/2020.
//
#include <iostream>
#include <vector>
#include <chrono>

using namespace std;
const int N = 10000000;
float v = 0.53125;
vector<float> vct(N, v);

float kahan_sum(){
    float sum = 0.0f;
    float err = 0.0f;
    for (float i : vct) {
        float y = i - err;
        float temp = sum + y;
        err = (temp - sum) - y;
        sum = temp;
    }
    return sum;
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
    return 0;
}
