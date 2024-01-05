# Anda bisa set parameter sentences untuk menentukan jumlah kalimat yang akan diambil dari halaman wiki

import wikipedia
wikipedia.set_lang("id")
print(wikipedia.summary("Indonesia", sentences = 2))