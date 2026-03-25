# Sentetik Veri Seti: Fiziksel Özellikler Simülasyonu

Bu proje, istatistiksel analizler ve veri görselleştirme pratikleri için normal dağılıma (Gaussian distribution) uygun sentetik bir veri seti üretir.

## Veri Seti Kurgusu
Bu veri seti, rastgele seçilmiş 1000 bireyin fiziksel ölçümlerini (boy ve ağırlık) temsil etmektedir. Doğadaki birçok biyolojik özellik gibi, bu veriler de merkezi limit teoremi gereği "Çan Eğrisi" formunda dağılım sergiler. Veriler tamamen yazılım tarafından üretilmiş olup, gerçek kişileri yansıtmamaktadır.

## Değişkenler
Veri setinde en az 500 satır (şu an 1000) ve aşağıdaki 2 temel değişken bulunmaktadır:

| Değişken İsmi | Birim | Açıklama |
| :--- | :--- | :--- |
| **Boy_cm** | Santimetre (cm) | Bireyin boy uzunluğu. Ortalama 175 cm, standart sapma 7 cm olarak kurgulanmıştır. |
| **Agirlik_kg** | Kilogram (kg) | Bireyin vücut ağırlığı. Ortalama 70 kg, standart sapma 10 kg olarak kurgulanmıştır. |

## Dosya Yapısı ve Görevleri
Proje şu 4 temel dosyadan oluşmaktadır:

1.  **data_generator.py**: Rastgele normal dağılımlı veriyi üretip CSV olarak kaydeder.
2.  **normal_dagilimli_veri.csv**: Üretilen 1000 satırlık veri seti.
3.  **visualizer.py**: CSV dosyasını okuyup Matplotlib ile grafik üretimini gerçekleştirir.
4.  **normal_dagilim_grafigi.png**: Üretilen çan eğrisi grafiği.

## Nasıl Çalıştırılır?
Sırasıyla şu komutları çalıştırarak projeyi test edebilirsiniz:

1.  **Veri Üretme:**
    ```bash
    python data_generator.py
    ```
2.  **Görselleştirme:**
    ```bash
    python visualizer.py
    ```
