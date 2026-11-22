# Sayfa Değiştirme Algoritmaları Simülasyonu

İşletim Sistemleri dersi kapsamında geliştirilen bu proje, bellekteki sayfa değiştirme (page replacement) algoritmalarının performansını simüle etmekte ve karşılaştırmaktadır. 

### Proje Hakkında
Bu simülasyon, belirli bir referans dizisi üzerinden belleğe sayfa yükleme süreçlerini adım adım gösterir. Her bir algoritma için bellek durumu, sayfanın bellekte bulunma "Hit" (İsabet) ve bulunamama "Fault" (Hata) durumları anlık olarak hesaplanarak konsola yazdırılır. Amacı, farklı algoritmaların bellek yönetimindeki verimliliklerini istatistiksel olarak ortaya koymaktır.

### İncelenen Algoritmalar ve Analiz Sonuçları
Projede dört temel sayfa değiştirme algoritması aynı referans dizisiyle (toplam 13 referans, 3 çerçeve) test edilmiş ve karşılaştırmalı olarak şu sonuçlar elde edilmiştir:

* **OPTİMAL:** Gelecekte en uzun süre kullanılmayacak sayfanın çıkarıldığı, en yüksek performansı veren modeldir. 7 Page Fault (%53.85 hata oranı) ve 6 Page Hit (%46.15 isabet oranı) ile simülasyonu tamamlamıştır.
* **LFU (Least Frequently Used):** En az sıklıkta kullanılan sayfanın çıkarıldığı bu yöntemde 8 Page Fault (%61.54 hata oranı) ve 5 Page Hit (%38.46 isabet oranı) hesaplanmıştır.
* **LRU (Least Recently Used):** En uzun süredir referans edilmeyen sayfanın değiştirildiği algoritmada 9 Page Fault (%69.23 hata oranı) ve 4 Page Hit (%30.77 isabet oranı) elde edilmiştir.
* **FİFO (First-In-First-Out):** İlk giren sayfanın ilk çıkarıldığı ve bu testte en düşük performansı sergileyen modeldir. 10 Page Fault (%76.92 hata oranı) ve 3 Page Hit (%23.08 isabet oranı) gözlemlenmiştir.

### Öne Çıkan Özellikler
* Kullanıcının kendi belirlediği referans dizisi ve çerçeve (frame) sayısı ile dinamik test yapabilme.
* CLI (Komut Satırı Arayüzü) üzerinden interaktif bir menü ile istenilen algoritmayı seçme veya tümünü aynı anda çalıştırıp kıyaslama.
* Her referans adımında bellek dizisinin o anki durumunu (trace) detaylı şekilde izleyebilme.
* Algoritmaların analiz verilerini bir araya getiren dinamik karşılaştırma tablosu.

### Kullanılan Teknolojiler
* Python

### Kurulum ve Çalıştırma
1. Proje dosyasını bilgisayarınıza indirin.
2. Terminal veya komut satırını açarak dosyanın bulunduğu dizine gidin.
3. `python main.py` (veya dosyanızın adı neyse) komutunu çalıştırarak programı başlatın.
