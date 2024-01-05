Program dibawah ini menampilkan list, dan mengganti setiap huruf vokal dengan tanda `*`

Perbaiki program dibawah ini sehingga menampilkan hasil seperti contoh output.

```python
daftar = ['Hendrawan', 'Rudianto', 'Rinawati', 'Gunawan', 'Santoso']

for nama in daftar
for huruf in nama
if huruf in ['a','e','i','o','u']
print("*", end="" )
else:
print(huruf,end=" ")
print()
```

Contoh output:
```
H*ndr*w*n
R*d**nt*
R*n*w*t*
G*n*w*n
S*nt*s*
```

---

Ganti `daftar` dengan kode _list_ berikut, lakukan perubahan pada program sebelumnya sehingga program tetap bisa menampilkan `*` ganti huruf vokal.
```python
daftar = ['Dyah Ayu', 'Ahmad', 'Ursila', 'Ortega', 'Emilia']
```

Contoh output:
```
Dy*h *y*
*hm*d
*rs*l*
*rt*g*
*m*l**
```