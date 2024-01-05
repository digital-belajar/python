---
layout: tutorial
title: Fungsi Python
permalink: /tutorial/fungsi-python
---

---

Fungsi adalah blok kode terorganisir dan dapat digunakan kembali yang digunakan untuk melakukan sebuah tindakan/action. Fungsi memberikan modularitas yang lebih baik untuk aplikasi Anda dan tingkat penggunaan kode yang tinggi.

### Mendefinisikan Fungsi Python

Anda dapat menentukan fungsi untuk menyediakan fungsionalitas yang dibutuhkan. Berikut adalah aturan sederhana untuk mendefinisikan fungsi dengan Python.

- Fungsi blok dimulai dengan def kata kunci diikuti oleh nama fungsi dan tanda kurung (()).
- Setiap parameter masukan atau argumen harus ditempatkan di dalam tanda kurung ini. Anda juga dapat menentukan parameter di dalam tanda kurung ini.
- Pernyataan pertama dari sebuah fungsi dapat berupa pernyataan opsional - string dokumentasi fungsi atau docstring.
- Blok kode dalam setiap fungsi dimulai dengan titik dua (:) dan indentasi.
- Pernyataan kembali [ekspresi] keluar dari sebuah fungsi, secara opsional menyampaikan kembali ekspresi ke pemanggil. Pernyataan pengembalian tanpa argumen sama dengan return None.

Contoh fungsi
{% highlight python %}
def cetak_bilangan():
    "Fungsi ini mencetak bilangan 1 sampai 3"
    i = 1
    while i < 4:
        print(i)
        i = i + 1
    return 

cetak_bilangan()
# output:
# 1
# 2
# 3
{% endhighlight %}

Kita bisa menambahkan parameter pada fungsi seperti berikut:

{% highlight python %}
def cetak_bilangan(n):
    "Fungsi ini mencetak bilangan 1 sampai n"
    i = 1
    while i<n:
        print(i)
        i = i + 1
    return

cetak_bilangan(4)

# output:
# 1
# 2
# 3
{% endhighlight %}

Kita juga bisa memiliki fungsi yang memiliki nilai kembali (_return value_) seperti berikut:

{% highlight python %}
def luas_persegi(panjang,lebar):
    luas = panjang * lebar
    return luas # return value

p = 3
l = 4
# cara memanggil fungsi
print("Luas Persegi =", luas_persegi(p,l))

# output:
# Luas Persegi = 12
{% endhighlight %}




> [Edit tutorial ini](https://github.com/belajarpythoncom/belajarpythoncom.github.io/edit/master/tutorials/fungsi-python.md)

<div class="row navigation-tutorial">
    <div class="col-md-6 prev-tutorial">
        <a href="/tutorial/tanggal-waktu-python"><i class="fas fa-arrow-circle-left"></i>Tanggal & Waktu Python</a>
    </div>
    <div class="col-md-6 next-tutorial">
        <a href="/tutorial/modul-python" class="hoverable">Modul Python<i class="fas fa-arrow-circle-right"></i></a>
    </div>
</div>
