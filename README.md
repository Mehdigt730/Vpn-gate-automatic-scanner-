# Vpn-gate-automatic-scanner-

# 🌐 VPN Gate Fast Server Fetcher

A powerful, user-friendly Python script to fetch, test, and save the fastest public OpenVPN servers from [VPN Gate](https://www.vpngate.net/).  
With a single command, get working `.ovpn` configs with latency checks — perfect for privacy enthusiasts, researchers, and travelers!

---

## 🚀 Features

- **Auto Fetch:** Instantly grabs the latest public OpenVPN servers from VPN Gate.
- **Smart Filtering:** Only lists servers with a working `.ovpn` config.
- **Latency Test:** Checks real TCP connectivity and sorts servers by real ping time.
- **Multi-Threaded:** Super-fast server scanning using concurrent threads.
- **Easy Export:** Saves working OpenVPN configs for instant use.
- **Cross-Platform:** Runs on Windows, macOS, Linux.
- **Auto Dependency Installer:** Installs required Python modules automatically.

---

## 📦 Requirements

- Python 3.6+
- `requests` (auto-installed if needed)
- Internet access

---

## ⚡️ Usage

```bash
git clone https://github.com/Mehdigt730/vpngate-fast-fetcher.git
cd vpngate-fast-fetcher
python3 "vpn gate.py"
```

### 🛠 How it works

1. Fetches the latest VPN Gate server list.
2. Extracts OpenVPN `.ovpn` configs.
3. Lets you choose how many servers to test (or test all).
4. Checks which are reachable and measures latency.
5. Saves working configs into `vpngate_configs` folder.

### 🔑 Default VPN Credentials

- **Username:** `vpn`
- **Password:** `vpn`

---

## ⚠️ Disclaimer

- **For educational and research purposes only.**
- Use VPNs responsibly and comply with your country’s laws.

---

## 🤝 Credits

- Powered by [VPN Gate](https://www.vpngate.net/) project.

---

# 🌐 اسکریپت دریافت سریع سرورهای VPN Gate

یک اسکریپت پایتون ساده و قدرتمند برای دریافت، تست و ذخیره سریع‌ترین سرورهای عمومی OpenVPN از [VPN Gate](https://www.vpngate.net/).  
فایل‌های کانفیگ `.ovpn` را با تست تاخیر واقعی و فقط با یک دستور دریافت کنید — مناسب علاقه‌مندان حریم خصوصی، محققان و مسافران!

---

## 🚀 ویژگی‌ها

- **دریافت خودکار:** جدیدترین سرورهای عمومی OpenVPN را سریع دریافت کنید.
- **فیلتر هوشمند:** فقط سرورهایی را نمایش می‌دهد که فایل کانفیگ `.ovpn` دارند.
- **تست تاخیر:** سریع‌ترین سرورها را با بررسی اتصال و تاخیر واقعی پیدا می‌کند.
- **چندریسمانی:** تست فوق‌سریع سرورها با چند رشته همزمان.
- **خروجی آسان:** فایل کانفیگ سرورهای سالم را برای استفاده سریع ذخیره می‌کند.
- **سازگار با همه سیستم‌عامل‌ها:** ویندوز، مک و لینوکس.
- **نصب خودکار پیش‌نیازها:** ماژول‌های لازم را خودکار نصب می‌کند.

---

## 📦 پیش‌نیازها

- پایتون ۳.۶ یا بالاتر
- ماژول `requests` (در صورت نیاز خودکار نصب می‌شود)
- اتصال اینترنت

---

## ⚡️ روش اجرا

```bash
git clone https://github.com/Mehdigt730/vpngate-fast-fetcher.git
cd vpngate-fast-fetcher
python3 "vpn gate.py"
```

### 🛠 این اسکریپت چه می‌کند؟

1. جدیدترین لیست سرورهای VPN Gate را دریافت می‌کند.
2. کانفیگ‌های OpenVPN را استخراج می‌کند.
3. تعداد سرورهای مورد نظر برای تست را انتخاب می‌کنید (یا همه را تست کنید).
4. اتصال و تاخیر سرورها را بررسی می‌کند.
5. کانفیگ سرورهای سالم را داخل پوشه `vpngate_configs` ذخیره می‌کند.

### 🔑 اطلاعات ورود پیش‌فرض VPN

- **نام کاربری:** `vpn`
- **رمز عبور:** `vpn`

---

## ⚠️ هشدار

- **فقط برای اهداف آموزشی و تحقیقاتی.**
- مسئولیت استفاده بر عهده شماست و قوانین کشور خود را رعایت کنید.

---

## 🤝 با تشکر از

- پروژه [VPN Gate](https://www.vpngate.net/)

version beta 
