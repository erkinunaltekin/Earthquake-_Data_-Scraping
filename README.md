
# Deprem Veri Çekici

## Türkçe

### Genel Bakış
Bu Python betiği, Kandilli Rasathanesi ve Deprem Araştırma Enstitüsü'nün web sitesinden deprem verilerini çeker. Belirli bir anahtar kelimenin deprem listelerindeki geçişlerini arar.

### Nasıl Kullanılır
1. **URL Ayarı**: Betik, verileri `http://www.koeri.boun.edu.tr/scripts/lst0.asp` adresinden çekmek üzere ayarlanmıştır. Gerekirse URL güncellenebilir.
2. **Anahtar Kelime Arama**: Deprem verileri içinde aramak istediğiniz anahtar kelimeyi `search_word` değişkeni ile değiştirin, örneğin bir yer ismi.
3. **Betik Çalıştırma**: Betiği çalıştırarak anahtar kelimeniz için deprem verilerini arayın. Eşleşen girdiler yazdırılır; eşleşme bulunamazsa "Veri bulunamadı" mesajı yazdırılır.

### Bağımlılıklar
- `requests`: Web sayfalarını çekmek için.
- `BeautifulSoup` from `bs4`: HTML içeriğini ayrıştırmak için.

### Kurulum
Gerekli paketleri yüklemek için şu komutu çalıştırın:
```
pip install requests beautifulsoup4
```

## English

### Overview
This Python script extracts earthquake data from the Kandilli Observatory and Earthquake Research Institute's website. It specifically searches for occurrences of a specified keyword in the earthquake listings.

### How to Use
1. **Set the URL**: The script is currently set to scrape data from `http://www.koeri.boun.edu.tr/scripts/lst0.asp`. You can update the URL as needed.
2. **Keyword Search**: Replace the variable `search_word` with the desired keyword to search within the earthquake data, such as a location.
3. **Running the Script**: Execute the script to search the earthquake data for your keyword. Matching entries will be printed; if no matches are found, it will print "Data not found."

### Dependencies
- `requests`: To fetch web pages.
- `BeautifulSoup` from `bs4`: To parse HTML content.

### Installation
To install the required packages, run:
```
pip install requests beautifulsoup4
```
