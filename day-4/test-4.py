line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
letter = position[0].lower()
abc = ["a","b","c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")



'''
# İlk olarak, haritayı oluşturuyoruz. Her bir satır, bir listeye eşittir ve üç kare içerir.
line1 = ["⬜️","️⬜️","️⬜️"]  # Haritanın ilk satırı
line2 = ["⬜️","⬜️","️⬜️"]    # Haritanın ikinci satırı
line3 = ["⬜️️","⬜️️","⬜️️"]   # Haritanın üçüncü satırı

# Şimdi, bu üç satırı birleştirerek bir harita oluşturuyoruz.
map = [line1, line2, line3]

# Kullanıcıya hazineyi nereye saklayacağını sormak için bir mesaj gösteriyoruz.
print("Hiding your treasure! X marks the spot.")

# Kullanıcıdan hazineyi saklamak istediği konumu alıyoruz.
position = input()  # Kullanıcıdan giriş al

# 🚨 Kodun yukarısını değiştirmeyin 👆
# Kodunuzu aşağıdaki satırların üzerine ekleyin 👇

# Kullanıcının girdisini işliyoruz. İlk harfi alıp küçük harfe dönüştürüyoruz.
letter = position[0].lower()

# Harita sütunlarını temsil eden bir alfabe listesi oluşturuyoruz.
abc = ["a","b","c"]

# Kullanıcının girdisindeki ikinci karakteri (rakamı) alıyoruz ve bir çıkarıyoruz, çünkü indeksler sıfırdan başlar.
number_index = int(position[1]) - 1

# Haritadaki doğru konumu bulmak için kullanıcı girdisini kullanıyoruz ve oraya bir hazine (X) yerleştiriyoruz.
map[number_index][abc.index(letter)] = "X"

# Kodunuzu buraya ekleyin 👆
# 🚨 Kodun aşağısını değiştirmeyin 👇

# Güncellenmiş haritayı ekrana basıyoruz.
print(f"{line1}\n{line2}\n{line3}")



'''