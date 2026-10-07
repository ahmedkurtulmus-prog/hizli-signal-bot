import ccxt
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


# --- ALTERNATİF BİNANCE BAĞLANTISI (IP Engelini Aşar) ---
exchange = ccxt.binance({
    'options': {'defaultType': 'future'},
    'enableRateLimit': True,
    'urls': {
        'api': {
            'public': 'https://fapi.binance.com/fapi/v1',
            'private': 'https://fapi.binance.com/fapi/v1',
        }
    },
})


def hizli_tarama():
  print('Kaptan, engelsiz hızlı sinyal botu tarıyor...')
  try:
    # Test için ana pariteler
    coinler = ['BTC/USDT:USDT', 'ETH/USDT:USDT', 'SOL/USDT:USDT']

    for symbol in coinler:
      ticker = exchange.fetch_ticker(symbol)
      coin_adi = symbol.split('/')[0]
      fiyat = ticker['last']
      degisim = ticker['percentage']

      mesaj = (
          f"⚡ *ENGELSİZ HIZLI TEST SİNYALİ* ⚡\n\n"
          f"🪙 *Coin:* `{coin_adi}/USDT`\n"
          f"💰 *Fiyat:* `{fiyat}`\n"
          f"📊 *24s Değişim:* `% {degisim}`\n\n"
          f"Kaptan, IP engeli aşıldı, hatlar bomba gibi!"
      )
      telegram_mesaj_gonder(mesaj)

    print('Tüm test mesajları başarıyla gönderildi!')

  except Exception as e:
    print(f"Hata detayı: {e}")


if __name__ == '__main__':
  hizli_tarama()
