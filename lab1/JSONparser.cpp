//
// Created by Agnieszka on 02/03/2020.
//
#include "JSONparser.h"
#include <iostream>
#include <fstream>

using namespace std;

void export_to_file(std::string filename, std::string data){
    ofstream file;
    std::string dir = R"(D:\Agnieszka\Documents\Studia\4semestr\MOWNiT\lab1\data\)";
    file.open(dir+filename);
    file << data;
    file.close();
}
