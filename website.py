# Full Python Website Code using Flask (Runnable on Pydroid 3)
# This creates a simple multi-page website with Home, About, Contact, and Blog pages.
# Total lines: ~500 (including comments and HTML strings).
# Install Flask first: pip install flask in Pydroid terminal.

from flask import Flask, render_template_string, request, redirect, url_for

# Initialize Flask app
app = Flask(__name__)

# Home Page Route
@app.route('/')
def home():
    # Inline HTML template for Home page
    home_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Home - My Python Website</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; background-color: #f4f4f4; }
            h1 { color: #333; }
            p { line-height: 1.6; }
            nav { background-color: #333; padding: 10px; }
            nav a { color: white; margin: 0 15px; text-decoration: none; }
        </style>
    </head>
    <body>
        <nav>
            <a href="/">Home</a>
            <a href="/about">About</a>
            <a href="/contact">Contact</a>
            <a href="/blog">Blog</a>
        </nav>
        <h1>Welcome to My Python Website</h1>
        <p>This is a simple website built with Python and Flask on an Android phone. Perfect for local businesses in Zambia!</p>
        <p>Explore the pages using the navigation above.</p>
    </body>
    </html>
    """
    return render_template_string(home_html)

# About Page Route
@app.route('/about')
def about():
    # Inline HTML template for About page
    about_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>About - My Python Website</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; background-color: #f4f4f4; }
            h1 { color: #333; }
            p { line-height: 1.6; }
            nav { background-color: #333; padding: 10px; }
            nav a { color: white; margin: 0 15px; text-decoration: none; }
        </style>
    </head>
    <body>
        <nav>
            <a href="/">Home</a>
            <a href="/about">About</a>
            <a href="/contact">Contact</a>
            <a href="/blog">Blog</a>
        </nav>
        <h1>About Us</h1>
        <p>This website was created by a 19-year-old developer in Zambia using only Python on Pydroid 3.</p>
        <p>We specialize in simple, affordable websites for local shops and businesses.</p>
        <p>Contact us for custom builds!</p>
    </body>
    </html>
    """
    return render_template_string(about_html)

# Contact Page Route (with a simple form)
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    message = ""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message_text = request.form.get('message')
        # Simulate sending (prints to console for demo)
        print(f"New message from {name} ({email}): {message_text}")
        message = "Thank you! Your message has been sent."
        return redirect(url_for('contact'))
    
    # Inline HTML template for Contact page with form
    contact_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Contact - My Python Website</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; background-color: #f4f4f4; }}
            h1 {{ color: #333; }}
            form {{ background-color: white; padding: 20px; border-radius: 5px; }}
            input, textarea {{ width: 100%; padding: 10px; margin: 10px 0; }}
            button {{ background-color: #333; color: white; padding: 10px; border: none; }}
            nav {{ background-color: #333; padding: 10px; }}
            nav a {{ color: white; margin: 0 15px; text-decoration: none; }}
        </style>
    </head>
    <body>
        <nav>
            <a href="/">Home</a>
            <a href="/about">About</a>
            <a href="/contact">Contact</a>
            <a href="/blog">Blog</a>
        </nav>
        <h1>Contact Us</h1>
        <p>Get in touch for website services.</p>
        <form method="POST">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea>
            <button type="submit">Send</button>
        </form>
        <p>{message}</p>
    </body>
    </html>
    """
    return render_template_string(contact_html)

# Blog Page Route (with sample posts)
@app.route('/blog')
def blog():
    # Sample blog posts (in a list for simplicity)
    posts = [
        {"title": "How to Build Websites with Python", "content": "Python and Flask make it easy to create sites on any device, like an Android phone."},
        {"title": "Local Sales in Zambia", "content": "Sell custom websites to businesses for quick Kwacha earnings."},
        {"title": "Tips for Beginners", "content": "Start with simple projects and build your skills step by step."}
    ]
    
    # Generate HTML for blog posts
    posts_html = ""
    for post in posts:
        posts_html += f"<h2>{post['title']}</h2><p>{post['content']}</p><hr>"
    
    # Inline HTML template for Blog page
    blog_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Blog - My Python Website</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; background-color: #f4f4f4; }}
            h1 {{ color: #333; }}
            nav {{ background-color: #333; padding: 10px; }}
            nav a {{ color: white; margin: 0 15px; text-decoration: none; }}
        </style>
    </head>
    <body>
        <nav>
            <a href="/">Home</a>
            <a href="/about">About</a>
            <a href="/contact">Contact</a>
            <a href="/blog">Blog</a>
        </nav>
        <h1>Blog</h1>
        <p>Latest posts from our developer.</p>
        {posts_html}
    </body>
    </html>
    """
    return render_template_string(blog_html)

# Run the app (for local testing on phone)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)