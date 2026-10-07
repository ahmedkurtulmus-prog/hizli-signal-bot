import requests

# --- TELEGRAM AYARLARI ---
TELEGRAM_TOKEN = "8950898533:AAEU-FsEvHt5qUIAzXMwa-hCBWZMTGcDI_Y"
CHAT_ID = "-1003795173448"


def telegram_mesaj_gonder(mesaj):
  url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
  payload = {"chat_id": CHAT_ID, "text": mesaj, "parse_mode": "Markdown"}
  try:
    requests.post(url, json=payload)
  except Exception as e:
    print(f"Telegram mesaj hatası: {e}")


def hizli_tarama():
  print("Kaptan, korumalı saf API taraması başlatıldı...")
  try:
    url = "https://fapi.binance.com/fapi/v1/ticker/24hr"
    response = requests.get(url, timeout=10)
    data = response.json()

    # Gelen verinin liste olup olmadığını kontrol ediyoruz
    if not isinstance(data, list):
      print(f"Beklenmeyen veri formatı: {data}")
      return

    hedef_coinler = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]

    for item in data:
      symbol = item.get("symbol")
      if symbol in hedef_coinler:
        coin_adi = symbol.replace("USDT", "")
        fiyat = float(item.get("lastPrice", 0))
        degisim = float(item.get("priceChangePercent", 0))

        mesaj = (
            f"⚡ *KORUMALI SAF API SİNYALİ* ⚡\n\n"
            f"🪙 *Coin:* `{coin_adi}/USDT`\n"
            f"💰 *Fiyat:* `{fiyat}`\n"
            f"📊 *24s Değişim:* `% {degisim}`\n\n"
            f"Kaptan, veriler tertemiz çekildi, sistem tam gaz!"
        )
        telegram_mesaj_gonder(mesaj)

    print("Tüm korumalı test mesajları başarıyla gönderildi!")

  except Exception as e:
    print(f"Hata detayı: {e}")


if __name__ == "__main__":
  hizli_tarama()
