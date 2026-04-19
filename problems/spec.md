# SPEC - Which Language System

## Functional Requirements
 FR1: Sistem kullanıcıdan programlama dili tercihi almalıdır.
 FR2: Sistem kullanıcıya uygun dil önerisi sunmalıdır.
 FR3: Hatalı girişlerde Türkçe hata mesajı verilmelidir.
 FR4: Kullanıcı girişleri kontrol edilmelidir.
 FR5: Sonuçlar düzenli gösterilmelidir.

## Non-Functional Requirements
 NFR1: Sistem hızlı çalışmalıdır.
 NFR2: Kullanıcı dostu olmalıdır.


 ## Kabul Kriterleri ve Hata Yönetimi (V2 update)

### Kabul Kriterleri
Doğruluk: Sistem, desteklenen dillerdeki (Tr, En) metinleri en az %90 doğrulukla tanımalıdır.
Hız: Dil tespiti işlemi 1 saniyenin altında tamamlanmalıdır.
Arayüz: Kullanıcı metni girdiği anda veya bir butona bastığında sonuç net bir şekilde ekranda belirmelidir.

### Hata Yönetimi
Boş Giriş: Kullanıcı metin alanını boş bıraktığında sistem "Lütfen bir metin girin" uyarısı vermelidir
Bilinmeyen Dil: Desteklenmeyen bir dilde metin girildiğinde sistem "Dil tespit edilemedi" mesajı dönmelidir
