print("""Geometrik Şekil Bulma Programa Hoşgeldiniz.\nLütfen Bulmak istediğiniz Dörtfen Tipini Yazınız(Dörtgen,Üçgen)""")
istenen_sekil = input("Bulmak İstediğiniz Şekli Yazınız:").lower()
if istenen_sekil == "dörtgen":
    print("Lütfen Dörtgenin Kenar Uzunluklarını Yazınız:")
    kenar_1 = int(input("Birinci Kenar:"))
    kenar_2 = int(input("İkinci Kenar:"))
    kenar_3 = int(input("Üçüncü Kenar:"))
    kenar_4 = int(input("Dördüncü Kenar:"))
    if kenar_1 == kenar_2 and kenar_1==kenar_3 and kenar_1 == kenar_4 :
        print("-Yazdığınız Kenar UZunluklarına Göre Şekil--> Kare ")
    elif kenar_1 == kenar_2 and kenar_3 == kenar_4:
        print("-Yazdığınız Kenar Uzunluklarına Göre Şekil--> Dikdörtgen")
    else:
        print("-Yazdığınız Kenar Uzunluklarına Göre Şekil Bir--> Dörtgen")
elif istenen_sekil == "üçgen":
    print("Lütfen Üçgenin Kenar Uzunluklarını Yazınız:")
    kenar_1 = int(input("Birinci Kenar:"))
    kenar_2 = int(input("İkinci Kenar:"))
    kenar_3 = int(input("Üçüncü Kenar:"))
    #Python'da abs fonksiyonu sayıların mutlak değerlerini almak için kullanılır.
    if (abs(kenar_1 + kenar_2) > kenar_3 and abs(kenar_1 + kenar_3) > kenar_2 and abs(kenar_2 + kenar_3) > kenar_1):
        if (kenar_1 == kenar_2 and kenar_1 == kenar_3):
            print("""-Yazdığınız Kenar Uzunluklarına Göre Şekil--> Eşkenar Üçgen\nÜçgenin Açılarına Göre Çeşidini De Öğrenmek İster Misiniz?""")
            istek = input("İstiyorsanız 'Evet' İstemiyorsanız 'Hayır' Yazınız:").lower()
            if istek == "evet":
                print("Lütfen Üçgenin AÇılarını Yazınız")
                acı_1 = int(input("Açı-1:"))
                acı_2 = int(input("Açı-2:"))
                acı_3 = int(input("Açı-3:"))
                if acı_1 and acı_2 and acı_3 < 90:
                    print("-Verdiğiniz Değerlere Göre Üçgenin Açılarına Göre Çeşidi--> Dar Açılı Üçgen")
                elif acı_1 or acı_2 or acı_3 == 90:
                    print("-Verdiğiniz Değerlere Göre Üçgenin Açılarına Göre Çeşidi--> Dik Açılı Üçgen")
                else:
                    print("""-Verdiğiniz Değerlere Göre Üçgenin Açılarına Göre Çeşidi--> Geniş Açılı Üçgen""")
            else:
                print("İyi Günler")
        elif ((kenar_1 == kenar_2 and kenar_2 != kenar_3) or (kenar_1 == kenar_3 and kenar_1 != kenar_2) or (kenar_2 == kenar_3 and kenar_2 != kenar_1)):
            print("""-Yazdığınız Kenar UZunluklarına Göre Şekil--> İkizkenar Üçgen\nÜçgenin Açılarına Göre Çeşidini De Öğrenmek İster Misiniz?""")
            istek = input("İstiyorsanız 'Evet' İstemiyorsanız 'Hayır' Yazınız:").lower()
            if istek == "evet":
                print("Lütfen Üçgenin AÇılarını Yazınız:")
                acı_1 = int(input("Açı-1:"))
                acı_2 = int(input("Açı-2:"))
                acı_3 = int(input("Açı-3:"))
                if acı_1 and acı_2 and acı_3 < 90:
                    print("-Verdiğiniz Değerlere Göre Üçgenin Açılarına Göre Çeşidi--> Dar Açılı Üçgen")
                elif acı_1 or acı_2 or acı_3 == 90:
                    print("-Verdiğiniz Değerlere Göre Üçgenin Açılarına Göre Çeşidi--> Dik Açılı Üçgen")
                else:
                    print("""-Verdiğiniz Değerlere Göre Üçgenin Açılarına Göre Çeşidi--> Geniş Açılı Üçgen""")
            else:
                print("İyi Günler")
        else:
            print("""-Yazdığınız Kenar UZunluklarına Göre Şekil--> Çeşitkenar Üçgen\nÜçgenin Açılarına Göre Çeşidini De Öğrenmek İster Misiniz?""")
            istek = input("İstiyorsanız 'Evet' İstemiyorsanız 'Hayır' Yazınız:").lower()
            if istek == "evet":
                print("Lütfen Üçgenin AÇılarını Yazınız:")
                acı_1 = int(input("Açı-1:"))
                acı_2 = int(input("Açı-2:"))
                acı_3 = int(input("Açı-3:"))
                if acı_1 and acı_2 and acı_3 < 90:
                    print("-Verdiğiniz Değerlere Göre Üçgenin Açılarına Göre Çeşidi--> Dar Açılı Üçgen")
                elif acı_1 or acı_2 or acı_3 == 90:
                    print("-Verdiğiniz Değerlere Göre Üçgenin Açılarına Göre Çeşidi--> Dik Açılı Üçgen")
                else:
                    print("""-Verdiğiniz Değerlere Göre Üçgenin Açılarına Göre Çeşidi--> Geniş Açılı Üçgen""")
            else:
                print("İyi Günler")
    else:
        print("Yazdığınız Kenar Uzunluklarına Göre Şekil Üçgen belirtmiyor")
