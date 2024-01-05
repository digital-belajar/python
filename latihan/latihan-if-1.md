## Latihan Program 1

Buat program menggunakan python yang mensimulasikan _memilih makanan_. Proses pemilihan makanan mengikuti diagram seperti berikut:

```mermaid
flowchart TD;
    A[Start]-->B{Makan pedas?}
    B-->|Ya| C{Berkuah}
    C-->|Ya| D[Semblak]
    C-->|Tidak| E[Indomie]
    B-->|Tidak| F{Manis?}
    F-->|Ya| G[Buah]
    F-->|Tidak| H[Bala-bala]
```

contoh hasil 1:
```
Makan pedas?y
Berkuah?y
Makanan = Semblak
```

contoh hasil 2:
```
Makan pedas?t
Manis?y
Makanan = Buah
```