import requests

# --- TELEGRAM AYARLARI ---
TELEGRAM_TOKEN = "8950898533:AAEU-FsEvHt5qUIAzXMwa-hCBWZMTGcDI_Y"
CHAT_ID = "853083506"


def telegram_mesaj_gonder(mesaj):
  url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
  payload = {"chat_id": CHAT_ID, "text": mesaj, "parse_mode": "Markdown"}
  try:
    requests.post(url, json=payload)
  except Exception as e:
    print(f"Telegram mesaj hatası: {e}")


def hizli_tarama():
  print("Kaptan, engelsiz saf API taraması başlatıldı...")
  try:
    # Doğrudan Binance Futures halka açık fiyat API adresi (IP engeline takılmaz)
    url = "https://fapi.binance.com/fapi/v1/ticker/24hr"
    response = requests.get(url, timeout=10)
    data = response.json()

    # İstediğimiz coinler
    hedef_coinler = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]

    for item in data:
      symbol = item["symbol"]
      if symbol in hedef_coinler:
        coin_adi = symbol.replace("USDT", "")
        fiyat = float(item["lastPrice"])
        degisim = float(item["priceChangePercent"])

        mesaj = (
            f"⚡ *SAF API TEST SİNYALİ* ⚡\n\n"
            f"🪙 *Coin:* `{coin_adi}/USDT`\n"
            f"💰 *Fiyat:* `{fiyat}`\n"
            f"📊 *24s Değişim:* `% {degisim}`\n\n"
            f"Kaptan, engel mangep kalmadı, hatlar tertemiz!"
        )
        telegram_mesaj_gonder(mesaj)

    print("Tüm saf API test mesajları başarıyla gönderildi!")

  except Exception as e:
    print(f"Hata detayı: {e}")


if __name__ == "__main__":
  hizli_tarama()
