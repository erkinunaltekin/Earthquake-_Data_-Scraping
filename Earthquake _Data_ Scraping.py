import requests
from bs4 import BeautifulSoup

# Web sayfasının URL'si
url = 'http://www.koeri.boun.edu.tr/scripts/lst0.asp'

# Web sayfasından içeriği çekme
response = requests.get(url)
html_content = response.text

# Beautiful Soup nesnesi oluşturma
soup = BeautifulSoup(html_content, 'html.parser')

# Aranacak kelime
search_word = "van"

# Arama kelimesini büyük harfe çevirme
search_word_upper = search_word.upper()

# Tüm <pre> etiketlerini al
pre_tags = soup.find_all('pre')

# <pre> etiketleri içinde arama kelimesini içeren satırları bulma
found = False  # Eşleşme durumunu takip etmek için bir flag
for pre in pre_tags:
    lines = pre.text.split('\n')  # Metni satırlara ayırma
    for line in lines:
        if search_word_upper in line.upper():  # Arama kelimesini ve satırı büyük harfe çevirme
            print(line)  # Eşleşen satırı yazdırma
            found = True

if not found:
    print("Veri bulunamadı")  # Eğer hiçbir satır eşleşmezse bu mesajı yazdır
