# 🧪 Tox21 Molecular Toxicity Predictor

Kimyasal bileşiklerin toksisite (zehirlilik) özelliklerini tahmin etmek için geliştirilmiş bir makine öğrenmesi projesi.

## 📌 Proje Hakkında

Bu proje, **Tox21 Challenge** veri setini kullanarak kimyasal moleküllerin çeşitli biyolojik hedeflere (reseptörlere) karşı toksik etkilerini analiz eder.

### Hedef Reseptörler:
- **NR-AR:** Androjen Reseptörü (Hormon sistemi)
- **NR-ER:** Östrojen Reseptörü (Hormon sistemi)
- **SR-MMP:** Mitokondriyal Membran Potansiyeli (Hücre zarı)

---

## 🛠️ Kullanılan Teknolojiler

- **RDKit:** Molekül özelliklerini (descriptors) hesaplama
- **Pandas:** Veri manipülasyonu
- **Matplotlib:** Veri görselleştirme
- **Scikit-learn:** Makine öğrenmesi (gelecek adım)

---

## 🔬 Çıkarılan Moleküler Özellikler

Her SMILES stringinden şu özellikler hesaplanmıştır:

| Özellik | Açıklama |
|---------|----------|
| `mol_weight` | Moleküler ağırlık |
| `LogP` | Lipofiliklik (Yağda çözünürlük) |
| `NumHDonors` | Hidrojen bağı donör sayısı |
| `NumHAcceptors` | Hidrojen bağı alıcı sayısı |
| `NumRotatableBonds` | Dönebilen bağ sayısı |
| `NumAromaticRings` | Aromatik halka sayısı |

---

## 🚀 Nasıl Çalıştırılır?

### 1. Gereksinimleri Yükle
```bash
pip install -r requirements.txt
