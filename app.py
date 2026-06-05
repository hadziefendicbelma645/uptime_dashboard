from flask import Flask, render_template_string
import requests

app = Flask(__name__)

# Web stranice koje DevOps dashboard nadgleda
SITES = [
    "https://google.com", 
    "https://github.com", 
    "https://ova-stranica-sigurno-ne-postoji-12345.com"
]

def check_site_status(url):
    try:
        # Šaljem zahtjev stranici (najviše 3 sekunde)
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return "UP"
        else:
            return f"DOWN ({response.status_code})"
    except Exception:
        return "DOWN (Error)"

@app.route('/')
def home():
    # Provjeravam status za svaku stranicu sa liste
    results = {}
    for site in SITES:
        results[site] = check_site_status(site)
    
    # HTML i CSS izgled stranice 
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Dashboard</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 50px; background-color: #f4f6f9; color: #333; }
            h1 { color: #2c3e50; border-bottom: 2px solid #2c3e50; padding-bottom: 10px; }
            .site-container { margin-top: 20px; }
            .card { padding: 15px 20px; margin: 10px 0; border-radius: 6px; font-weight: bold; font-size: 18px; display: flex; justify-content: space-between; }
            .UP { background-color: #d4edda; color: #155724; border-left: 5px solid #28a745; }
            .DOWN { background-color: #f8d7da; color: #721c24; border-left: 5px solid #dc3545; }
        </style>
    </head>
    <body>
        <h1>📊 DevOps Uptime Monitor — Projekt 2</h1>
        <p>Trenutni status nadgledanih web servisa i eksternih linkova:</p>
        
        <div class="site-container">
            {% for site, status in results.items() %}
                <div class="card {{ 'UP' if 'UP' in status else 'DOWN' }}">
                    <span>🔗 {{ site }}</span>
                    <span>{{ status }}</span>
                </div>
            {% endfor %}
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template, results=results)

if __name__ == '__main__':
    # Pokretanje servera lokalno na portu 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
