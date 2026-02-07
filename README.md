# Trendyol Scraper 🛒

Trendyol Scraper, **Playwright** ve **Tkinter** kullanarak Trendyol üzerindeki ürünleri kolayca çekmenizi sağlayan bir masaüstü uygulamadır.  
Ürün bilgilerini (marka, başlık, fiyat, eski fiyat, indirimli fiyat, link) toplar ve **Excel dosyasına** kaydeder.

## 🚀 Özellikler
- Kullanıcı dostu **GUI** (Tkinter ile)
- **Threading** desteği sayesinde donmadan çalışan arayüz
- Her sayfa için **log penceresi** ile ilerleme takibi
- Ürün bilgilerini **Excel (.xlsx)** dosyasına sheet bazlı kaydetme
- Çoklu fiyat tiplerini yakalama (normal, eski, indirimli)

## 📦 Kurulum

1. Repoyu klonla:
   ```bash
   git clone https://github.com/colaker92/Trendyol_Scraper.git
   cd Trendyol_Scraper/scraper


- Gerekli paketleri yükle:
pip install playwright pandas tk


- Playwright browser’larını kur:
playwright install

▶️ Kullanım- scraper klasöründe main.py dosyasını çalıştır:

python main.py
- GUI üzerinden:
- Trendyol kategori linkini gir
- Kaç sayfa scrape edileceğini belirt
- Excel sheet adını yaz
- Scrape Başlat butonuna bas
- Çekilen ürünler products.xlsx dosyasına kaydedilir.


📊 Örnek ÇıktıExcel dosyasında şu kolonlar bulunur:- brand

- title
- price
- old_price
- discount_price
- link

🔮 Geliştirme Planları- Progress bar ekleme

- Çoklu site desteği (Amazon, Walmart, Sahibinden)
- Ürün karşılaştırma algoritmaları (fuzzy matching, NLP)
- Otomatik zamanlanmış scraping


📄 LisansBu proje MIT lisansı ile sunulmaktadır. İstediğiniz gibi kullanabilir ve geliştirebilirsiniz.