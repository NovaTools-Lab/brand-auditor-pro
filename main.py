import urllib.request
import ssl
import time

def audit_avanzato(url):
    print(f"\n--- 🛡️ BRAND AUDIT REPORT PER: {url} ---")
    start = time.time()
    
    # Assicuriamoci che l'URL inizi con http o https
    if not url.startswith('http'):
        url = 'https://' + url
    
    # 1. Controllo Sicurezza SSL (Il "Lucchetto")
    context = ssl.create_default_context()
    ssl_status = "⚠️ SCONOSCIUTO"
    try:
        # Tenta una connessione HTTPS sicura
        with urllib.request.urlopen(url, context=context) as response:
            ssl_status = "✅ SICURO (HTTPS Attivo)"
    except ssl.SSLError:
        ssl_status = "❌ NON SICURO (Errore SSL/TLS)"
    except Exception:
        ssl_status = "⚠️ Errore di connessione (Controlla l'URL)"

    # 2. Controllo Velocità e Stato
    try:
        risposta = urllib.request.urlopen(url)
        fine = time.time()
        tempo_caricamento = round(fine - start, 2)
        status_code = risposta.getcode()
        
        # 3. Output del Report
        print(f"\n[RISULTATI]")
        print(f"🔒 Sicurezza SSL: {ssl_status}")
        print(f"🌐 Stato Sito: Online (Codice {status_code})")
        print(f"⚡ Velocità Risposta: {tempo_caricamento} secondi")
        
        # Suggerimenti automatici basati sui dati
        print(f"\n[SUGGERIMENTI DI BUSINESS]")
        if "❌ NON SICURO" in ssl_status:
            print("👉 AZIONE PRIORITARIA: Il sito non è sicuro. Installare subito un certificato SSL per non perdere clienti.")
        if tempo_caricamento > 2.0:
            print("👉 Ottimizzazione: Il sito è lento (>2s). Ottimizzare immagini e caching per migliorare la conversione.")
        if "✅ SICURO" in ssl_status and tempo_caricamento <= 2.0:
            print("🎉 Ottimo lavoro! Le basi tecniche del brand sono solide.")

    except Exception as e:
        print(f"\n❌ Errore critico: Impossibile analizzare il sito ({e})")

# --- Avvio del Tool ---
print("Benvenuto in Brand Auditor Pro v0.2")
sito = input("Inserisci l'URL del sito da analizzare (es: google.com): ")
audit_avanzato(sito)
