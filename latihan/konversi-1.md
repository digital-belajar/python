## Konversi Program (1)

Jika Anda pernah mempelajari bahasa pemrograman sebelumnya, salah satu cara untuk mempelajari bahasa pemrograman baru adalah dengan membuat perbandingan bahasa pemrograman yang pernah Anda pelajari.

Untuk latihan coba konversi program yang dibuat dalam C++ ke dalam python.

Jika tidak ada program C++ atau python, Anda bisa menggunakan [C++ Online Compiler](https://www.programiz.com/cpp-programming/online-compiler/) dan [Python Online COmpiler](https://www.programiz.com/python-programming/online-compiler/) 

**Soal 1**
```c++
#include<iostream>
using namespace std;

int main() {
    int p = 4;
    int l = 6;
    int luas = p * l;
    int keliling = 2 * (p+l);
    cout << "Keliling persegi adalah " << keliling << endl;
    cout << "Luas persegi adalah " << luas << endl;
}
```

**Soal 2**
```c++
#include<iostream>
using namespace std;

int main() {
    string depan, belakang, lengkap;
    depan = "Budi";
    belakang = "Raharjo";
    
    lengkap = depan + " " + belakang;

    cout << "Hallo " << lengkap;
    cout << "Apa kabar";
}
```

**Soal 3**
```c++
#include<iostream>
using namespace std;

int main() {
    string depan, belakang, lengkap, jeniskelamin;
    cout << "Nama Depan:";
    cin >> depan;
    cout << "Nama Belakang:";
    cin >> belakang;
    cout << "laki-laki/perempuan (l/p)?";
    cin >> jeniskelamin;

}
```

**Soal 4**
```c++
#include<iostream>
using namespace std;

int main() {
    string nama, jeniskelamin;
    int usia;
    cout << "Nama :";
    cin >> nama;    
    cout << "laki-laki/perempuan (l/p)?";
    cin >> jeniskelamin;
    cout << "Usia : ";
    cin >> usia;

    if(jeniskelamin=="l") {
        if(usia>25) {
            cout << "Halo, bapak " << nama;
        } else {
            cout << "Halo, de " << nama;
        }
    } else {
        if(usia>20) {
            cout << "Halo, ibu " << nama;
        } else {
            cout << "Halo, neng " << nama;
        }
    }

    lengkap = depan + " " + belakang;

    if(jeniskelamin=="l") {
        cout << "Selamat siang, bapak " << lengkap;
    } else {
        cout << "Selamat siang, ibu " << lengkap;
    }

}
```

**Soal 5**
```c++
#include<iostream>
using namespace std;

int main() {
    string nama;
    int nilai;

    cout << "Nama: "; cin >> nama;
    cout << "Nilai "; cin >> nilai;

    if(nilai<0 || nilai>100) {
        cout << "Nilai salah";
    } else {
        if(nilai>60) {
            cout << "Lulus";
        } else if (nilai>40 && nama=="Budi") {
            cout << "Remidial";
        } else {
            cout << "Tidak lulus";
        }
    }
}
```