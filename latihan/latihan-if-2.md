## Latihan IF #2

Coba jalankan program berikut, kemudian pelajari output dari masing-masing output dari angka yang berbeda.

```python
angka = int(input("Angka?"))

if angka>5:
    print("A")
    print("B")
    if angka>7:
        print("C")
    print("D")
else:
    print("E")
    if angka<3:
        print("F")
    else:
        print("G")
        print("H")
    print("I")
print("J")
```

**Pertanyaan:**
1. Bagaimana output dari input: `9` , `2`
2. Berapa angka yang perlu dimasukan jika mau memberikan output: `ABDJ`
3. Berapa angka yang perlu dimasukan jika mau memberikan output: `EGHIJ`
4. Apa fungsi `input()`?
5. Apa fungsi `int()`?