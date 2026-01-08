from flask import Flask, render_template_string, request, redirect, url_for, session
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = "mutendele_gregory_2026"

# --- DATABASE SETUP ---
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users 
        (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT, 
         is_paid INTEGER DEFAULT 0, quiz_score INTEGER DEFAULT 0, transaction_ref TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS info (id INTEGER PRIMARY KEY, announcement TEXT, ticker TEXT)''')
    cursor.execute('INSERT OR IGNORE INTO info (id, announcement, ticker) VALUES (1, "Welcome", "🚀 New Python Data Science module is now LIVE! | 🎓 Get your certificate today! | 💰 K5 for 5 Days!")')
    conn.commit(); conn.close()

init_db()

CSS_STYLE = """
    body { font-family: 'Segoe UI', sans-serif; margin: 0; background-color: #0a0a0a; color: #e0e0e0; overflow-x: hidden; }
    
    /* FEATURE 1: News Ticker */
    .ticker-wrap { width: 100%; overflow: hidden; background: #332b00; color: #ffeb3b; padding: 5px 0; font-size: 0.8em; font-weight: bold; }
    .ticker { display: inline-block; white-space: nowrap; animation: ticker 25s linear infinite; }
    @keyframes ticker { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }

    nav { background-color: #1a1a1a; padding: 15px; text-align: center; border-bottom: 2px solid #333; }
    nav a { color: #bb86fc; margin: 0 10px; text-decoration: none; font-weight: bold; font-size: 0.8em; }
    
    .container { padding: 15px; max-width: 600px; margin: auto; }
    
    /* BIG SIGNUP FONT */
    .big-font { font-size: 3.5em; color: #bb86fc; font-weight: 900; line-height: 1; margin-bottom: 20px; }
    
    .card { background: #1e1e1e; padding: 20px; border-radius: 15px; border: 1px solid #333; margin-bottom: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
    
    .btn { background: #03dac6; color: #000; padding: 15px; border: none; cursor: pointer; border-radius: 10px; width: 100%; font-weight: bold; font-size: 1.1em; transition: 0.3s; }
    .btn:hover { background: #bb86fc; }
    
    /* Floating WhatsApp Button */
    .whatsapp-float { position: fixed; bottom: 20px; right: 20px; background: #25d366; color: white; width: 50px; height: 50px; border-radius: 50%; text-align: center; line-height: 50px; font-size: 24px; box-shadow: 0 4px 10px rgba(0,0,0,0.3); text-decoration: none; }
    
    input { background: #2c2c2c; border: 1px solid #444; color: white; padding: 15px; width: 85%; border-radius: 10px; margin-bottom: 10px; font-size: 1.1em; }
"""

def get_header(title):
    conn = sqlite3.connect('users.db')
    ticker_text = conn.execute("SELECT ticker FROM info WHERE id=1").fetchone()[0]
    conn.close()
    
    # Feature 7: Auto-Greeter
    hour = datetime.now().hour
    greeting = "Good Morning" if hour < 12 else "Good Afternoon" if hour < 18 else "Good Evening"
    user_greet = f"{greeting}, {session['user']}!" if 'user' in session else "Welcome Student"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title><style>{CSS_STYLE}</style>
    </head>
    <body>
        <div class="ticker-wrap"><div class="ticker">{ticker_text}</div></div>
        <nav>
            <a href="/">HOME</a><a href="/courses">NOTES</a><a href="/community">RANK</a>
            {'<a href="/logout">LOGOUT</a>' if 'user' in session else '<a href="/login">LOGIN</a>'}
        </nav>
        <div class="container">
            <p style="color:#03dac6; font-size:0.8em; text-align:center;">{user_greet}</p>
    """

FOOTER = """
    </div>
    <a href="https://wa.me/260764140632" class="whatsapp-float">💬</a>
    <footer><p style="text-align:center; color:#555; font-size:0.6em; margin-top:50px;">© 2026 Mutendele Gregory Tembo</p></footer>
    </body></html>
"""

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        u, p = request.form['u'], request.form['p']
        conn = sqlite3.connect('users.db')
        try:
            conn.execute('INSERT INTO users (username, password) VALUES (?,?)', (u,p))
            conn.commit(); conn.close(); return redirect(url_for('login'))
        except: return "Name taken."
    return render_template_string(get_header("Join") + """
        <div style="text-align:center;">
            <div class="big-font">LEARN<br>FAST.</div>
            <p style="color:#777;">Engineering Hub Entrance</p>
            <form method="POST">
                <input name="u" placeholder="Your Name" required><br>
                <input name="p" type="password" placeholder="Choose Password" required><br>
                <button class="btn">START MY 5 DAYS (K5)</button>
            </form>
        </div>
    """ + FOOTER)

@app.route('/courses')
def courses():
    if 'user' not in session: return redirect(url_for('login'))
    # Logic to check payment and show PDF links + Audio Player
    return render_template_string(get_header("Lessons") + """
        <div class="card">
            <h3>Lesson 1: Logic Design</h3>
            <p style="color:#aaa;">Introduction to digital systems.</p>
            <button class="btn" style="background:#333; color:white; font-size:0.8em;">📖 View PDF Notes</button>
            <br><br>
            <p style="font-size:0.7em;">Listen to Audio Summary:</p>
            <audio controls style="width:100%;">
                <source src="lesson1.mp3" type="audio/mpeg">
            </audio>
        </div>
    """ + FOOTER)

@app.route('/')
def home():
    return render_template_string(get_header("Home") + """
        <div class="card" style="text-align:center; border: 2px solid #03dac6;">
            <h1 style="margin:0; color:#03dac6;">K5</h1>
            <p style="margin:0;">Full Access for 5 Days</p>
        </div>
        <a href="/signup" class="btn">CLICK TO JOIN NOW</a>
    """ + FOOTER)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        u, p = request.form['u'], request.form['p']
        conn = sqlite3.connect('users.db')
        if conn.execute('SELECT 1 FROM users WHERE username=? AND password=?', (u,p)).fetchone():
            session['user'] = u; conn.close(); return redirect(url_for('courses'))
        conn.close()
    return render_template_string(get_header("Login") + """
        <form method="POST" style="text-align:center;">
            <input name="u" placeholder="Name"><br>
            <input name="p" type="password" placeholder="Pass"><br>
            <button class="btn">LOGIN</button>
        </form>
    """ + FOOTER)

@app.route('/logout')
def logout(): session.clear(); return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)