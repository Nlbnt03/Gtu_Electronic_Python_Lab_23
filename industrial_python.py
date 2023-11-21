"""
fonksiyonlar : Bir işlemi kodda birden fazla yerde yapıcak isen fonksiyon yazarsın veya koduna otomtiklik katmak istiyorsan
----------------------------------
fonksiyon tanımlama :
def fonksiyon_ismi(parametre girilecek ise parametre(parametre yok ise boş bırakılır)):
    **docstring yazabilirsin**
    -------------------------
    fonksiyonun kodları
    return veya print ile sonlandırabilirsin
    -------------------------
return = çıktısını girdi olarak kullanacağın fonksiyonlarda return kullanılır
"""

def yas_kontrol(yas):
    """
    fonksiyon adı : yas_kontrol
    parametreler : yaş
    fonksiyon amacı : dışarıdan gelen yaş değerine göre ehliyet alma ya da almama durumunu 1 ve 0 olara sonuç döndürür
    """
    if yas >= 18:
        return (1)
    elif yas < 18:
        return (0)
    else:
        print("Hatalı yaş değeri !")

def  ismeOzel_ehliyet_kontrol(isim,yas):
    print(f"\nHoşgeldin {isim}\nYaşınız : {yas}")
    sonuc = yas_kontrol(yas)
    if sonuc == 1:
        print("Ehliyet alabilirsiniz")
    elif sonuc == 0:
        print("Ehliyet alamazsınız")
    else:
        print("İşlemde hata ile karşılaşıldı")

controller = 1
while (controller):
    print("""işlem yapmak için : 1
işlemden çıkmak için : 0""")
    tercih = int(input("Tercih :"))
    if (tercih == 1):
        isim = input("Lütfen isminizi giriniz :")
        yas = int(input("Lütfen yaşınızı giriniz :"))
        ismeOzel_ehliyet_kontrol(isim, yas)
    elif (tercih == 0):
        print("İşlemden çıkılıyor...")
        break
    else:
        print("Hatalı tercih !")
    print("------------------------------------------")
