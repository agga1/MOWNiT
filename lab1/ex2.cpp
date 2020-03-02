//
// Created by Agnieszka on 02/03/2020.
//
int main() {
    tab
    float sum = 0.0f;
    float err = 0.0f;
    for (int i = 0; i < tab.length; ++i){
        float y = tab[i] - err;
        float temp = sum + y;
        err = (temp - sum) - y;
    }
    return 0;
}
