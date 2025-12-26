# 1. Aşama: Python 3.9'un hafif bir versiyonunu temel al
FROM python:3.9-slim

# 2. Aşama: Uygulama dosyalarının yaşayacağı klasörü oluştur
WORKDIR /app

# 3. Aşama: Gerekli kütüphanelerin listesini kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Aşama: Tüm proje dosyalarını kopyala
COPY . .

# 5. Aşama: Flask portunu aç
EXPOSE 5000

# 6. Aşama: Uygulamayı başlat
CMD ["python", "app.py"]