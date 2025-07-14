from flask import Flask, render_template_string, request

app = Flask(__name__)

# Data login sederhana (bisa kamu ganti)
akun = {
    "rahman": "12345"
}

# Halaman login (HTML ditulis langsung di Python)
halaman_login = '''
<!doctype html>
<title>Login STIKOM</title>
<h2>Login STIKOM Banyuwangi</h2>
<form method="POST">
  <input type="text" name="username" placeholder="Nama Pengguna"><br><br>
  <input type="password" name="password" placeholder="Password"><br><br>
  <button type="submit">Masuk</button>
</form>
<p>{{ pesan }}</p>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    pesan = ''
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']
        if user in akun and akun[user] == pwd:
            pesan = f'Selamat datang, {user}!'
        else:
            pesan = 'Username atau password salah!'
    return render_template_string(halaman_login, pesan=pesan)

if __name__ == '__main__':
    app.run(debug=True)
