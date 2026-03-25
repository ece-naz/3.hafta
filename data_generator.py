import numpy as np
import pandas as pd

# 1. Ayarlar
n_satir = 1000
csv_dosya_adi = 'normal_dagilimli_veri.csv'

print(f"{n_satir} satırlık normal dağılımlı veri üretiliyor...")

# 2. Veri Üretimi
# Değişken 1: Boy (cm) - Ortalama: 175, Std: 7
boy = np.random.normal(loc=175, scale=7, size=n_satir)

# Değişken 2: Ağırlık (kg) - Ortalama: 70, Std: 10
agirlik = np.random.normal(loc=70, scale=10, size=n_satir)

# 3. DataFrame Oluşturma
df = pd.DataFrame({
    'Boy_cm': boy,
    'Agirlik_kg': agirlik
})

# 4. CSV Olarak Kaydetme
df.to_csv(csv_dosya_adi, index=False)
print(f"Veri başarıyla '{csv_dosya_adi}' dosyasına kaydedildi!")
