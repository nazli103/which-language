# 🚀 Programming Language Recommendation Project

## 📌 Proje Açıklaması
Bu proje, kullanıcının ilgi alanına göre uygun programlama dilini öneren basit bir Python uygulamasıdır.

Kullanıcıdan "web", "oyun" veya "veri" seçeneklerinden biri alınır ve buna göre öneri yapılır.

---

## ⚙️ Kullanılan Gereksinim (SPEC)

Bu proje, aşağıdaki gereksinimi gerçekleştirmektedir:

> Kullanıcıdan ilgi alanı alınmalı ve buna uygun programlama dili önerilmelidir.

---

## 💻 Prompt (Codex'e verilen komut)

> Kullanıcıdan web, oyun veya veri alanlarından birini seçmesini isteyen bir Python programı yaz.  
> Eğer web seçerse JavaScript, oyun seçerse C++, veri seçerse Python öner.  
> Geçersiz girişte kullanıcıyı uyar.

---

## 🧠 Kod Açıklaması

Program şu şekilde çalışır:

1. Kullanıcıdan bir ilgi alanı alınır.
2. Girilen değer kontrol edilir:
   - `web` → JavaScript önerilir
   - `oyun` → C++ önerilir
   - `veri` → Python önerilir
3. Geçersiz girişlerde kullanıcı uyarılır.
4. Program `if __name__ == "__main__":` yapısı ile çalıştırılır.

---

## 📄 Kod

```python
def recommend_language():
    interest = input("Ne ile ilgileniyorsun? (web / oyun / veri): ").strip().lower()

    if interest == "web":
        print("Önerilen dil: JavaScript")
    elif interest == "oyun":
        print("Önerilen dil: C++")
    elif interest == "veri":
        print("Önerilen dil: Python")
    else:
        print("Geçersiz giriş! Lütfen web, oyun veya veri yaz.")

if __name__ == "__main__":
    recommend_language()
