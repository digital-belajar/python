# Baca File Text

## List dari file text
Berikut contoh kode program untuk mengisi _list_ dari file text. Setiap barisnya akan menjadi elemen dalam _list_.
```python
# membaca file txt
with open('C:/latihan/nama.txt') as f:
    lines = f.read().splitlines()

# menampilkan kembali
n = 1
for baris in lines:
    print("No",n,":",baris)
    n += 1
```
