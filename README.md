# cyberTools
CyberTools siber güvenlik araçları setidir. Bu proje, ağ testi, dosya analizi, brute force saldırıları, port tarama gibi temel siber güvenlik görevlerini kişisel kullanımı kolaylaştırmak için geliştirilmiştir. Her araç bağımsız bir modül olarak çalışır ve kullanımı oldukça basittir.

# 📁 Proje Yapısı
CyberTools
├── app.py                 # Ana uygulama dosyası
└── src
    ├── component          # Araçların bulunduğu modüller
    │   ├── file.py        # Dosya analizi modülü
    │   ├── firewall.py    # Güvenlik duvarı yönetimi modülü
    │   ├── gobuster.py    # Dizin keşfi için Gobuster modülü
    │   ├── hydra.py       # Brute force saldırıları için Hydra modülü
    │   ├── kriptoloji.py  # Kriptografik işlemler modülü
    │   ├── macchanger.py  # MAC adresi değiştirme modülü
    │   ├── nmap.py        # Port tarama için Nmap modülü
    └── wordlist           # wordlist dosyaları
    
# 🔧 Kurulum
sudo apt update
sudo apt install nmap gobuster hydra ufw figlet
git clone https://github.com/eysacakil/cyberTools.git
cd /CyberTools

# 🚀 Kullanım
Uygulamayı çalıştırmak için aşağıdaki komutu kullanın:
python3 app.py

# 📜 Araçlar ve Özellikler
Nmap:
Hedef ağda port taraması yapar. Çeşitli taramalar icin çeşitli seçenekler bulunur.
Gobuster:
Web dizinlerini ve dosyalarını keşfeder.
Macchanger:
MAC adresinizi değiştirir.
Binwalk:
Dosya analizinde kullanılır
Hydra:
Brute force saldırıları yapar.
Kriptoloji:
Metin şifreleme ve çözme işlemleri yapar.
Firewall:
UFW güvenlik duvarını yönetir.

# 💡 Notlar
Bu proje eğitim amaçlı geliştirilmiştir.
Yalnızca izinli sistemler üzerinde test yapınız. Ayrıca Anayasanın 243. 246. maddelerini gözden geçiriniz!
Araçların çalışması için gerekli yetkileri sağladığınızdan emin olun. (sudo)

