# [Secilen-Repo-Ismi]

Bu depo, Kısıt Sağlama Problemlerini (Constraint Satisfaction Problems - CSP) çözmek için **MAC (Maintaining Arc Consistency)** algoritmasının Python ile uygulanmasını içerir. MAC, **AC3 (Arc Consistency Algorithm 3)** kullanarak arama sırasında yay tutarlılığını sürdüren bir Geriye İzleme (Backtracking) arama tekniğidir.

Uygulama, klasik **Avustralya Harita Boyama** problemi üzerinde gösterilmiştir.

## Genel Bakış

Kısıt Sağlama Problemleri, yapay zeka ve yöneylem araştırması gibi alanlarda önemli bir yer tutar. Bu projede, bir CSP'yi verimli bir şekilde çözmek için kullanılan yaygın teknikler uygulanmıştır:

*   **Geriye İzleme (Backtracking):** Sistematik olarak çözüm arayan temel arama algoritması.
*   **AC3:** Arama uzayını budamak için kullanılan bir yay tutarlılığı algoritması. Domainlerden, hiçbir çözümde yer alamayacak değerleri kaldırır.
*   **MAC:** Backtracking'in her adımında AC3'ü çağırarak tutarlılığı aktif olarak sürdüren ve böylece arama verimliliğini artıran gelişmiş bir arama algoritması.
*   **MRV (Minimum Remaining Values) Heuristiği:** Bir sonraki atanacak değişkeni seçmek için kullanılır (domaini en küçük olanı seçer).

## Nasıl Çalışır?

Kod temel olarak şu adımları izler:

1.  **Problem Tanımlama:** CSP; değişkenler (`Variable` sınıfı), her değişkenin alabileceği değerler (domain) ve değişkenler arasındaki kısıtlar (`Constraint` sınıfı) ile tanımlanır. `ConstraintProblem` sınıfı tüm problemi yönetir.
2.  **Başlangıç AC3 (Opsiyonel):** Arama başlamadan önce, başlangıç domainlerini küçültmek ve bariz tutarsızlıkları tespit etmek için tüm problem üzerinde AC3 çalıştırılır.
3.  **MAC Araması:**
    *   Özyinelemeli bir geriye izleme fonksiyonu (`mac_recursive`) çalışır.
    *   Her adımda, MRV heuristiği kullanılarak atanmamış bir değişken seçilir.
    *   Seçilen değişkenin domainindeki değerler sırayla denenir.
    *   Bir değer atandıktan **hemen sonra**, `ac3` fonksiyonu çağrılarak bu atamanın diğer değişkenlerin domainleri üzerindeki etkileri yayılır (yay tutarlılığı sürdürülür). `ac3` bu adımda sadece ilgili yayları kontrol ederek başlar.
    *   Eğer `ac3` bir değişkenin domaininin boşaldığını tespit ederse (tutarsızlık), o değer denemesi başarısız olur ve geri izleme (backtracking) yapılır.
    *   Geri izleme sırasında, `ac3`'ün yaptığı domain değişiklikleri `restore_domains` fonksiyonu ile geri alınır.
    *   Tüm değişkenlere tutarlı bir değer atandığında çözüm bulunur.

## Başlarken

### Gereksinimler

*   Python 3.x

### Çalıştırma

Depoyu klonladıktan veya kodu indirdikten sonra, tek dosya (`mac_solver.py` veya verdiğiniz isim) doğrudan çalıştırılabilir:

```bash
python mac_solver.py
