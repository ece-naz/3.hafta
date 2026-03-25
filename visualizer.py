import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Dosya Ayarları
csv_dosya_adi = 'normal_dagilimli_veri.csv'
grafik_dosya_adi = 'normal_dagilim_grafigi.png'

try:
    # 2. Veriyi Yükleme
    df = pd.read_csv(csv_dosya_adi)
    print(f"'{csv_dosya_adi}' başarıyla yüklendi. Görselleştirme hazırlanıyor...")

    # 3. Görselleştirme
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # --- BOY (cm) Çizimi ---
    counts, bins, ignored = ax1.hist(df['Boy_cm'], bins=30, density=True, alpha=0.6, color='skyblue', edgecolor='black')
    mu1, std1 = df['Boy_cm'].mean(), df['Boy_cm'].std()
    pdf1 = (1 / (std1 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((bins - mu1) / std1) ** 2)
    ax1.plot(bins, pdf1, linewidth=2, color='red', label=f'Çan Eğrisi\n(μ={mu1:.1f})')
    ax1.set_title('Boy Dağılımı (cm)')
    ax1.legend()
    ax1.grid(alpha=0.3)

    # --- AĞIRLIK (kg) Çizimi ---
    counts2, bins2, ignored2 = ax2.hist(df['Agirlik_kg'], bins=30, density=True, alpha=0.6, color='lightgreen', edgecolor='black')
    mu2, std2 = df['Agirlik_kg'].mean(), df['Agirlik_kg'].std()
    pdf2 = (1 / (std2 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((bins2 - mu2) / std2) ** 2)
    ax2.plot(bins2, pdf2, linewidth=2, color='red', label=f'Çan Eğrisi\n(μ={mu2:.1f})')
    ax2.set_title('Ağırlık Dağılımı (kg)')
    ax2.legend()
    ax2.grid(alpha=0.3)

    # 4. Kaydetme ve Gösterme
    plt.suptitle('Sentetik Veri Normal Dağılım Analizi', fontsize=16)
    plt.tight_layout()
    plt.savefig(grafik_dosya_adi)
    print(f"Grafik '{grafik_dosya_adi}' olarak kaydedildi.")
    plt.show()

except FileNotFoundError:
    print(f"Hata: '{csv_dosya_adi}' bulunamadı. Lütfen önce veri üretim kodunu çalıştırın.")
