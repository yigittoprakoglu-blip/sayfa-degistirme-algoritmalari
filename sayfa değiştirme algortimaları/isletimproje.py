def bellek_durumu(bellek,cerceve_sayisi):
    """bellek durumunu istenene formata getirmek için kullanılan yardımcı fonkisyon"""
    gosterim = bellek.copy()
    while len(gosterim) < cerceve_sayisi:
        gosterim.append("-")
    gosterim_str="["+",".join(str(eleman) for eleman in gosterim)+"]"
    return gosterim_str
    

def istatisk_yazdir(toplam_referans,page_fault_sayisi,page_hit_sayisi): #oranları yazdırmak için kullandığımız fonksiyon
    page_fault_orani = (page_fault_sayisi/toplam_referans)*100
    page_hit_orani =(page_hit_sayisi/toplam_referans)*100
    
    print("\nSonuçlar")
    print(f"toplam referans sayisi={toplam_referans}")
    print(f"page fault sayisi={page_fault_sayisi}")
    print(f"page hit sayisi={page_hit_sayisi}")
    print(f"page fault oranı ={page_fault_orani}")
    print(f"page hit oranı ={page_hit_orani}")
    return page_fault_sayisi, page_hit_sayisi, f"{page_fault_orani:.2f}%", f"{page_hit_orani:.2f}%"    

def fifo_algoritması(referans_dizi,cerceve_sayisi): #fifo algoritması
    print("\n FİFO ALGORİTMASI")
    print(f"{'Referans':<10} | {'Bellek Durumu':<20} | {'Sonuç'}") #tabloyu düzgün hizalamak için 
    bellek = [] #boş liste tanımlıyoruz ram çerçeveleri için 
    page_fault_sayisi=0
    page_hit_sayisi=0
    
    for sayfa in referans_dizi: #her sayfa isteği döngüye alınıyor
        if sayfa in bellek: #sayfa bellekte varsa hit 
            page_hit_sayisi+=1
            sonuc="Hit"
        else: #yoksa fault 
            page_fault_sayisi+=1
            sonuc="Fault"
            if len(bellek)==cerceve_sayisi: #bellek kapasitesi kadar dolmuş mu kontrolü
                bellek.pop(0) #bellek doluysa ilk giren çıkarılır
            bellek.append(sayfa)
        print(f"{sayfa:<10} | {bellek_durumu(bellek, cerceve_sayisi):<20} | {sonuc}")
    return istatisk_yazdir(len(referans_dizi),page_fault_sayisi,page_hit_sayisi)

def lru_algoritması(referans_dizi,cerceve_sayisi): #lru algoritması
    print("\n LRU ALGORİTMASI")
    print(f"{'Referans':<10} | {'Bellek Durumu':<20} | {'Sonuç'}")
    bellek=[]
    page_fault_sayisi = 0 
    page_hit_sayisi = 0 
    
    for sayfa in referans_dizi:
        if sayfa in bellek:
            page_hit_sayisi +=1
            sonuc="Hit"
            bellek.remove(sayfa)  #sayfayı bulunduğu indeksten siliyoruz
            bellek.append(sayfa)  #listenin sonuna taşıyoruz
        else:
            page_fault_sayisi +=1
            sonuc="Fault"
            if len(bellek) == cerceve_sayisi:
                bellek.pop(0)
            bellek.append(sayfa)
        print(f"{sayfa:<10} | {bellek_durumu(bellek, cerceve_sayisi):<20} | {sonuc}")
    return istatisk_yazdir(len(referans_dizi),page_fault_sayisi,page_hit_sayisi)
        
def lfu_algoritması(referans_dizi,cerceve_sayisi): #lfu algoritması
    print("\n LFU ALGORİTMASI")
    print(f"{'Referans':<10} | {'Bellek Durumu':<20} | {'Sonuç'}")
    bellek = []
    frekanslar={} #hangi sayfanın kaç kere kullandığını tutmak için 
    gelis_zamanı={}
    zaman_sayaci=0
    
    page_fault_sayisi=0
    page_hit_sayisi=0
    
    for sayfa in referans_dizi:
        zaman_sayaci+=1 #her yeni sayfa ihtiyacında zamanı 1 arttırıyoruz
        if sayfa in bellek:
            page_hit_sayisi+=1
            sonuc="Hit"
            frekanslar[sayfa]+=1#sayfa bellekte var frekans 1 artar
        else:
            page_fault_sayisi+=1
            sonuc="Fault"
            
            if len(bellek)<cerceve_sayisi:
                bellek.append(sayfa)
                frekanslar[sayfa]=1#yeni sayfanın frekansı 1 den başlar 
                gelis_zamanı[sayfa]=zaman_sayaci
            else:
                en_dusuk_frekans =float('inf') #en düşük frekanslıyı buluyoz
                for mevcut_sayfa in bellek:
                    if frekanslar[mevcut_sayfa]< en_dusuk_frekans:
                        en_dusuk_frekans = frekanslar[mevcut_sayfa]
                aday_sayfalar =[mevcut_sayfa for mevcut_sayfa in bellek if frekanslar[mevcut_sayfa]==en_dusuk_frekans]#düşük frekanslı sayfaları aday listesine topluyoruz
                
                degisecek_sayfa=aday_sayfalar[0] #eğer hepsi aynıysa ilk gelen atılır 
                en_eski_zaman =gelis_zamanı[degisecek_sayfa]
                for aday in aday_sayfalar:
                    if gelis_zamanı[aday]<en_eski_zaman:
                        en_eski_zaman = gelis_zamanı[aday]
                        degisecek_sayfa = aday
                bellek_index = bellek.index(degisecek_sayfa)
                bellek[bellek_index]=sayfa
                
                del frekanslar[degisecek_sayfa] #atılan sayfanın bilgilerini siliyoz
                del gelis_zamanı[degisecek_sayfa]
                
                frekanslar[sayfa]=1
                gelis_zamanı[sayfa]=zaman_sayaci
         
        print(f"{sayfa:<10} | {bellek_durumu(bellek, cerceve_sayisi):<20} | {sonuc}")
    return istatisk_yazdir(len(referans_dizi),page_fault_sayisi,page_hit_sayisi)

def optimal_algoritması(referans_dizi,cerceve_sayisi): #optimal algoritması
    print("\n OPTİMAL ALGORİTMASI")
    print(f"{'Referans':<10} | {'Bellek Durumu':<20} | {'Sonuç'}")
    
    bellek=[]
    page_fault_sayisi=0
    page_hit_sayisi=0
    
    for i in range(len(referans_dizi)): #indeksileri kullanmak için alıyoruz 
        sayfa = referans_dizi[i]
        
        if sayfa in bellek:
            page_hit_sayisi+=1
            sonuc="Hit"
        else:
            page_fault_sayisi+=1
            sonuc="Fault"
            if len(bellek)<cerceve_sayisi: #bellek boşsa ekliyor direk 
                bellek.append(sayfa)
            else:#ama bellek doluysa 
                en_uzak_mesaje = -1
                degisecek_sayfa_indeksi = -1
                
                for bellek_indeksi in range(len(bellek)): #bellekte bulunan her sayfaı inceler
                    bellekteki_sayfa=bellek[bellek_indeksi]
                    if bellekteki_sayfa not in referans_dizi[i+1:]: #burada gelecekte kullanılmayacak kurbanı şeçiyoruz
                        degisecek_sayfa_indeksi = bellek_indeksi
                        break
                    else: #ama eğer o sayfa kullanılcaksa en geç hangisi kullanılcağı buluyoruz
                        sonra_kullanım_indeksi = referans_dizi[i+1:].index(bellekteki_sayfa)
                        if sonra_kullanım_indeksi > en_uzak_mesaje:
                            en_uzak_mesaje=sonra_kullanım_indeksi
                            degisecek_sayfa_indeksi = bellek_indeksi
                bellek[degisecek_sayfa_indeksi]=sayfa
        print(f"{sayfa:<10} | {bellek_durumu(bellek, cerceve_sayisi):<20} | {sonuc}")
    return istatisk_yazdir(len(referans_dizi),page_fault_sayisi,page_hit_sayisi)

def karsilastirma_tablosu(sonuclar): #karşılaştırma tablosu fonk.
    print("\nKARŞILAŞTIRMA TABLOSU")
    print(f"{'Algoritma':<12} | {'Page Fault':<10} | {'Page Hit':<10} | {'Fault Oranı':<12} | {'Hit Oranı':<10}")
    
        
    for algoritma,degerler in sonuclar.items():
        fault,hit,f_orani,h_orani = degerler
        print(f"{algoritma:<12} | {fault:<10} | {hit:<10} | {f_orani:<12} | {h_orani:<10}")
        
        
        
def main(): # main 
    print("Algoritma denemeleri")
    referans_girdi = input("sayfa referans dizisini giriniz(aralara boşlul bırakın)")
    referans_dizi = [int(sayi) for sayi in referans_girdi.strip().split()]
    cerceve_sayisi = int(input("çerçeve sayısını giriniz."))
    
    
    while True: #menüyü çıkış yapılmadığı sürece tekrar açması için döngü
        print("\n MENÜ")
        print("1. FİFO")
        print("2.LRU")
        print("3.OPTİMAL")
        print("4.LFU")
        print("5.ALGORİTMLARI ÇALIŞTIR VE KARŞILAŞTIR")
        print("0.ÇIKIŞ")
        
        secim = input("hangi algoritmayı kullanmak istiyorsunuz") 
        
        if secim == '0':                 #secime göre kullanıcını istediği işlemi yaptırma 
            print("çıkış yapılıyor")
            break
        elif secim == '1':
            fifo_algoritması(referans_dizi, cerceve_sayisi)
        elif secim == '2':
            lru_algoritması(referans_dizi, cerceve_sayisi)
        elif secim == '3':
            optimal_algoritması(referans_dizi, cerceve_sayisi)
        elif secim == '4':
            lfu_algoritması(referans_dizi, cerceve_sayisi)
        elif secim == '5': #karşılaştırma tablosu tabloyu yazdırmadan önce hepsini çalıştırıyor hepsine tek tek bakabiliyoruz
            sonuclar = {}
            sonuclar["FİFO"]=fifo_algoritması(referans_dizi, cerceve_sayisi)
            sonuclar["LRU"]=lru_algoritması(referans_dizi, cerceve_sayisi)
            sonuclar["OPTİMAL"]=optimal_algoritması(referans_dizi, cerceve_sayisi)
            sonuclar["LFU"]=lfu_algoritması(referans_dizi, cerceve_sayisi)
            
            karsilastirma_tablosu(sonuclar)
        else: #eğer kullanıcı seçimlerle uyuşmayan bir şey girerse hata vermesi için 
            print("geçersiz bir seçim yaptınız tekrar deneyiniz")
            
if __name__ == "__main__":
    main()
        
    