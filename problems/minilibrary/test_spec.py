"""
mini-library Test Dosyasi
Ogrenci: [Nazlı Karagöz]
Proje: mini-library
"""
import subprocess
import os

# --- Yardimci Fonksiyon ---
def kodu_calistir(argumanlar):
    """Programi terminalden calistirir ve ne yazdigini dondurur."""
    islem = subprocess.run(
        ["python", "solution_v0.py"] + argumanlar,
        capture_output=True,
        text=True
    )
    return islem.stdout.strip()

# --- TESTLER ---

def test_1_init_klasor_olusturuyor_mu():
    # .minilib klasoru var mi bak
    kodu_calistir(["init"])
    assert os.path.exists(".minilib") == True

def test_2_init_zaten_varsa_hata_veriyor_mu():
    kodu_calistir(["init"])
    sonuc = kodu_calistir(["init"])
    assert "Zaten" in sonuc

def test_3_kitap_ekleme_basarili_mi():
    kodu_calistir(["init"])
    sonuc = kodu_calistir(["add", "Nutuk"])
    assert "eklendi" in sonuc

def test_4_ikinci_kitap_id_kontrol():
    kodu_calistir(["init"])
    kodu_calistir(["add", "Kitap1"])
    sonuc = kodu_calistir(["add", "Kitap2"])
    # Ikinci kitap oldugu icin icinde 2 gecmeli
    assert "2" in sonuc or "Kitap2" in sonuc

def test_5_init_yapmadan_ekleme_hatasi():
    # Klasor yokken eklemeye calis
    if os.path.exists(".minilib"):
        # Test temiz olsun diye klasoru siliyoruz (opsiyonel)
        import shutil
        shutil.rmtree(".minilib")
        
    sonuc = kodu_calistir(["add", "Test"])
    assert "Hata" in sonuc

def test_6_yanlis_komut_girilirse():
    sonuc = kodu_calistir(["naber"])
    assert "Gecersiz" in sonuc

def test_7_eksik_bilgi_ekleme():
    kodu_calistir(["init"])
    sonuc = kodu_calistir(["add"]) # Kitap adi vermeden dene
    assert "Lutfen" in sonuc

def test_8_listeleme_henuz_yok():
    sonuc = kodu_calistir(["list"])
    assert "haftaya" in sonuc

def test_9_odunc_henuz_yok():
    sonuc = kodu_calistir(["borrow"])
    assert "haftaya" in sonuc

def test_10_iade_henuz_yok():
    sonuc = kodu_calistir(["return"])
    assert "haftaya" in sonuc


