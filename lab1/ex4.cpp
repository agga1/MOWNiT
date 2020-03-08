//
// Created by Agnieszka on 03/03/2020.
//

#include <iostream>
#include <vector>
#include <chrono>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <cassert>
#include "JSONparser.h"
using namespace std;
//for each r in rs calculate values to which xn converges
vector<vector<float>> logistic_map_bif_diagram(float x0, const float *rs, int rs_len, int height=100){ //
    vector<vector<float>> bif_diagram;
    bif_diagram.resize(static_cast<const unsigned int>(rs_len), std::vector<float>(height));
    for(int i=0;i<rs_len;i++){
        float r  = rs[i];
        cout<<"\nr="<<r<<" x0="<<x0;
        float xn = x0;
        for(int j=0;j<600;j++){ // omit first 200 iterations
            xn = r*xn*(1-xn);
        }
        cout<<"\nafter 200 iter xn = "<<xn;
        for(int j=0; j<height;j++){
            xn = r*xn*(1-xn);
            bif_diagram[i][j]=(xn);
        }
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
template <class T>
int dist_to_0(T x0, T r=4.0f){
    int it = 0;
    T xprev =  x0;
    T xcurr;
    while(xprev>0){
        xcurr = r*xprev*(1-xprev);
        xprev = xcurr;
        it++;
        if(it==559) cout<<it<<" "<<xprev<<endl;
        if(it>10000) break;
    }
    return it;
}
float logistic(float x, float r){
    return r*x*(1-x);
}
int dist_to_0f(float x0, float r=4.0f){
    int it = 0;
    float x =  x0;
    while(x>0.0f){
        x = logistic(x, r);
        it++;
        if(it>10000) break;
    }
    return it;
}
void plot_bif_diagram(int rs_len=20, int height=100, float x0=0.7);
void compare_trajectories(float x0, float r, int N=70);
void distances_to_zero_r4(int nr_of_x0s=10);

int main(){
    assert(sizeof(float) == 4);
    float n;

    // compare trajectories between single and double precision
    float x0 = 0.7f, r=3.75f;
    compare_trajectories(x0, r);

    // deprecated-- see lab1vis.ipynb
    plot_bif_diagram(500, 500, x0);

    for(int i =0; i<100;i++){
        float x0 = (float)i/100;
        cout<<x0<<" "<<dist_to_0f(x0, 4)<<endl;
    }

    // counting nr of iterations needed for reaching 0 for r=4 and different x0s (single prec.)

}
// density of xs, ys, and x0
void plot_bif_diagram(int rs_len, int height, float x0){
    auto *rs = new float[rs_len];
    for(int i=0;i<rs_len;i++) rs[i]=1+3.0f*i/rs_len;
    vector<vector<float>> bif_diag = logistic_map_bif_diagram(x0, rs, rs_len, height);
    stringstream stream;
    stream << fixed << setprecision(2) << x0;
    string filename = (string)"bif_diagram"+stream.str()+".json";
    string filename_xs = (string)"bif_diagram"+stream.str()+"_xs.json";
    export_to_file(filename, parseVectorOfVs(bif_diag));
    export_to_file(filename_xs, parseArray(rs, rs_len));
}
void compare_trajectories(float x0, float r, int N){
    auto *t_float = new float[N];
    logistic_map_trajectory<float>(x0, r, t_float, N);
    auto *t_double = new double[N];
    logistic_map_trajectory<double>((double)x0, (double)r, t_double, N);
    int *xs = new int[N];
    for(int i=0;i<N;i++) xs[i]=i;
    export_to_file("t_float.json", parseArray(t_float, N));
    export_to_file("t_double.json", parseArray<double>(t_double, N));
    export_to_file("t_xs.json", parseArray(xs, N));
}
void distances_to_zero_r4(int nr_of_x0s){
    int *dists = new int[nr_of_x0s];
    float x0 = 1.0f/nr_of_x0s;
    for(int i=0; i<nr_of_x0s; i++){
        dists[i] = dist_to_0<float>(x0);
        x0+= 1.0f/nr_of_x0s;
    }
    export_to_file("to_zero.json", parseArray(dists, nr_of_x0s));
}
