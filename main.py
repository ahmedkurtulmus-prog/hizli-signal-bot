import requests

# --- TELEGRAM AYARLARI ---
TELEGRAM_TOKEN = "8950898533:AAEU-FsEvHt5qUIAzXMwa-hCBWZMTGcDI_Y"
CHAT_ID = "-1003795173448"  # Eksi (-) işaretli grup ID'si


def telegram_mesaj_gonder(mesaj):
  url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
  payload = {"chat_id": CHAT_ID, "text": mesaj, "parse_mode": "Markdown"}
  try:
    requests.post(url, json=payload)
  except Exception as e:
    print(f"Telegram mesaj hatası: {e}")


def hizli_tarama():
  print("Kaptan, engelsiz alternatif tarama başlatıldı...")
  try:
    # CoinGecko'nun hiçbir IP engeli olmayan, dünyaya açık halka açık API'si
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana,ripple&vs_currencies=usd&include_24hr_change=true"
    response = requests.get(url, timeout=10)
    data = response.json()

    # Gelen veriyi işleyip Telegram'a gönderelim
    coin_map = {
        "bitcoin": "BTC",
        "ethereum": "ETH",
        "solana": "SOL",
        "ripple": "XRP",
    }

    for key, coin_adi in coin_map.items():
      if key in data:
        fiyat = data[key]["usd"]
        degisim = round(data[key]["usd_24h_change"], 2)

        mesaj = (
            f"⚡ *ENGELSİZ HIZLI SİNYAL* ⚡\n\n"
            f"🪙 *Coin:* `{coin_adi}/USDT`\n"
            f"💰 *Fiyat (USD):* `$ {fiyat}`\n"
            f"📊 *24s Değişim:* `% {degisim}`\n\n"
            f"Kaptan, coğrafi engel delindi, mermiler yolda!"
        )
        telegram_mesaj_gonder(mesaj)

    print("Tüm alternatif test mesajları başarıyla gruba gönderildi!")

  except Exception as e:
    print(f"Hata detayı: {e}")


if __name__ == "__main__":
  hizli_tarama()
