from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Mahasiswa

app = Flask(__name__)

# ==========================
# Konfigurasi
# ==========================
app.config["SECRET_KEY"] = "pbofinal123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# ==========================
# Inisialisasi Database
# ==========================
db.init_app(app)

# ==========================
# Login Manager
# ==========================
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ==========================
# HOME / DASHBOARD
# ==========================
@app.route("/")
@login_required
def home():

    jumlah_mahasiswa = Mahasiswa.query.count()

    return render_template(
        "dashboard.html",
        user=current_user,
        jumlah_mahasiswa=jumlah_mahasiswa
    )


# ==========================
# REGISTER
# ==========================
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]
        konfirmasi_password = request.form["konfirmasi_password"]

        # Validasi Password
        if password != konfirmasi_password:
            flash("Konfirmasi password tidak sama!", "danger")
            return redirect(url_for("register"))

        # Cek Username
        user = User.query.filter_by(username=username).first()

        if user:
            flash("Username sudah digunakan!", "danger")
            return redirect(url_for("register"))

        password_hash = generate_password_hash(password)

        new_user = User(
            username=username,
            password=password_hash
        )

        db.session.add(new_user)
        db.session.commit()

        flash("Registrasi berhasil. Silakan login.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


# ==========================
# LOGIN
# ==========================
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):

            login_user(user)

            flash("Login berhasil.", "success")
            return redirect(url_for("home"))

        flash("Username atau Password salah!", "danger")
        return redirect(url_for("login"))

    return render_template("login.html")


# ==========================
# LOGOUT
# ==========================
@app.route("/logout")
@login_required
def logout():

    logout_user()

    flash("Anda berhasil logout.", "info")

    return redirect(url_for("login"))


# ==========================
# DATA MAHASASISWA
# ==========================
@app.route("/mahasiswa")
@login_required
def mahasiswa():

    keyword = request.args.get("keyword")

    if keyword:
        data = Mahasiswa.query.filter(
            Mahasiswa.nama.contains(keyword) |
            Mahasiswa.nim.contains(keyword) |
            Mahasiswa.jurusan.contains(keyword)
        ).all()
    else:
        data = Mahasiswa.query.all()

    return render_template(
        "mahasiswa.html",
        mahasiswa=data,
        keyword=keyword
    )


# ==========================
# TAMBAH MAHASISWA
# ==========================
@app.route("/tambah", methods=["GET", "POST"])
@login_required
def tambah():

    if request.method == "POST":

        nama = request.form["nama"]
        nim = request.form["nim"]
        jurusan = request.form["jurusan"]

        # Validasi
        if not nama or not nim or not jurusan:
            flash("Semua field wajib diisi!", "danger")
            return redirect(url_for("tambah"))

        # Cek NIM
        cek = Mahasiswa.query.filter_by(nim=nim).first()

        if cek:
            flash("NIM sudah digunakan!", "danger")
            return redirect(url_for("tambah"))

        data = Mahasiswa(
            nama=nama,
            nim=nim,
            jurusan=jurusan
        )

        db.session.add(data)
        db.session.commit()

        flash("Data mahasiswa berhasil ditambahkan.", "success")

        return redirect(url_for("mahasiswa"))

    return render_template("tambah.html")


# ==========================
# EDIT MAHASISWA
# ==========================
@app.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit(id):

    mahasiswa = Mahasiswa.query.get_or_404(id)

    if request.method == "POST":

        nama = request.form["nama"]
        nim = request.form["nim"]
        jurusan = request.form["jurusan"]

        # Cek NIM selain data yang sedang diedit
        cek = Mahasiswa.query.filter(
            Mahasiswa.nim == nim,
            Mahasiswa.id != id
        ).first()

        if cek:
            flash("NIM sudah digunakan mahasiswa lain!", "danger")
            return redirect(url_for("edit", id=id))

        mahasiswa.nama = nama
        mahasiswa.nim = nim
        mahasiswa.jurusan = jurusan

        db.session.commit()

        flash("Data mahasiswa berhasil diubah.", "success")

        return redirect(url_for("mahasiswa"))

    return render_template(
        "edit.html",
        mahasiswa=mahasiswa
    )


# ==========================
# HAPUS MAHASISWA
# ==========================
@app.route("/hapus/<int:id>")
@login_required
def hapus(id):

    mahasiswa = Mahasiswa.query.get_or_404(id)

    db.session.delete(mahasiswa)
    db.session.commit()

    flash("Data mahasiswa berhasil dihapus.", "success")

    return redirect(url_for("mahasiswa"))


# ==========================
# Membuat Database
# ==========================
with app.app_context():
    db.create_all()


# ==========================
# Menjalankan Aplikasi
# ==========================
if __name__ == "__main__":
    app.run(debug=True)