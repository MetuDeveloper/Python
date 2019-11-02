from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt
from functools import wraps

#Kullanıcı Giriş Decorator'ı
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("Bu sayfayı görüntülemek için lütfen giriş yapınız...","danger")
            return redirect(url_for("login"))
    return decorated_function

app = Flask(__name__)
app.secret_key = "gizlianahtar"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "okanwebsitesi"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

#Kullanıcı Kayıt Formu
class RegisterForm(Form):
    name = StringField("İsim Soyisim: ",validators=[validators.length(min=4,max=25),validators.DataRequired("İsminizi girin...")])
    username = StringField("Kullanıcı Adı: ",validators=[validators.length(min=4,max=25),validators.DataRequired("Kullanıcı adı giriniz...")])
    email = StringField("Email Adresi: ",validators=[validators.email("Lütfen Geçerli Bir Email Adresi Giriniz..."),validators.data_required("Email adresinizi giriniz...")])
    password = PasswordField("Şifre: ",validators=[validators.DataRequired("Şifrenizi Giriniz..."),validators.Length(min=5,max=20,message="5-20 arası karakter kullanınız."),validators.EqualTo(fieldname = "confirm",message = "Parolanız uyuşmuyor...")])
    confirm = PasswordField("Şifreyi Tekrar Giriniz: ")

#Giriş Formu
class LoginForm(Form):
    username = StringField("Kullanıcı Adı: ")
    password = PasswordField("Şifre: ")

@app.route("/register", methods = ["GET","POST"])
def kayıtol():
    form = RegisterForm(request.form)

    if request.method == "POST" and form.validate():
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(form.password.data)

        cursor = mysql.connection.cursor()
        sorgu = "INSERT INTO users(name,username,email,password) VALUES(%s,%s,%s,%s)"
        cursor.execute(sorgu,(name,username,email,password))
        mysql.connection.commit()
        cursor.close()
        flash("Başarıyla kayıt oldunuz hayırlı olsun...","success")
        return redirect(url_for("/login.html"))
    else:
        return render_template("register.html",form = form)

@app.route("/")
def index():
    sözlük = [
        {"isim":"okan kandemir","meslek":"inşaat mühendisi","yaş":"26"},
        {"isim":"orhan kandemir","meslek":"emekli","yaş":"54"},
        {"isim":"buket kandemir","meslek":"öğrenci","yaş":"14"},
        {"isim":"hatice kandemir","meslek":"ev hanımı","yaş":"50"}
    ]
    return render_template("index.html",dict = sözlük )

@app.route("/about")
def about():
    return render_template("about.html")

#Giriş yapma fonksiyonu
@app.route("/login", methods = ["GET","POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST":
        username = form.username.data
        password_entered = form.password.data
        cursor = mysql.connection.cursor()
        sorgu = "Select * From users where username = %s"
        result = cursor.execute(sorgu,(username,))
        if result > 0:
            data = cursor.fetchone()
            realpassword = data["password"]
            if sha256_crypt.verify(password_entered,realpassword):
                flash("Başarıyla giriş yaptınız...","success")
                session["logged_in"] = True
                session["username"] = username

                return redirect(url_for("index"))
            else:
                flash("Hatalı şifre, tekrar deneyiniz...","danger")
                return redirect(url_for("login"))
        else:
            flash("Böyle bir kullanıcı bulunmuyor","danger")
            return redirect(url_for("login"))
        cursor.close()

    return render_template("login.html",form = form)

#Çıkış işlemi
@app.route("/logout")
def cikis():
    session.clear()
    flash("Çıkış işlemi başarıyla gerçekleştirildi...","success")
    return redirect(url_for("index"))

@app.route("/dashboard")
@login_required
def dashboard():
    cursor = mysql.connection.cursor()
    sorgu = "Select * From articles where author = %s"
    result = cursor.execute(sorgu,(session["username"],))
    if result > 0:
        articles = cursor.fetchall()
        return render_template("/dashboard.html",articles = articles)
    else:
        return render_template("dashboard.html")

#Makale Ekleme
@app.route("/addarticle",methods=["GET","POST"])
@login_required
def addarticle():
    form = ArticleForm(request.form)
    if request.method == "POST" and form.validate:
        title = form.title.data
        content = form.content.data
        cursor = mysql.connection.cursor()
        sorgu = "Insert into articles(title,author,content) VALUES(%s,%s,%s)"
        cursor.execute(sorgu,(title,session["username"],content))
        mysql.connection.commit()
        cursor.close()
        flash("Makale başarıyla kaydedildi...","success")
        return redirect(url_for("dashboard"))


    return render_template("addarticles.html",form = form)

#Makale oluşturma
class ArticleForm(Form):
    title = StringField("Makale Başlığı: ",validators=[validators.length(min=5,max=100),"Makale başlığı 5-100 karakter arasında olmalıdır..."])
    content = TextAreaField("Makale İçeriği: ",validators=[validators.length(min=10),"Makale içeriği en az 10 karakter olmalıdır..."])

#Makeleler Sayfası
@app.route("/articles")
def makaleler():
    cursor = mysql.connection.cursor()
    sorgu = "Select * From articles"
    result = cursor.execute(sorgu)
    if result >0:
        articles = cursor.fetchall()
        return render_template("/articles.html",articles = articles)
    else:
        return render_template("/articles.html")
    
#Makale Detay Sayfası
@app.route("/article/<string:id>")
def makale_detayı(id):
    cursor = mysql.connection.cursor()
    sorgu = "Select*From articles where id = %s"
    result = cursor.execute(sorgu,(id,))

    if result > 0:
        article = cursor.fetchone()
        return render_template("article.html",article = article)
    else:
        return render_template("/article.html")

#Makale Silme
@app.route("/delete/<string:id>")
@login_required
def delete(id):
    cursor = mysql.connection.cursor()
    sorgu = "Select * From articles where author = %s and id = %s"
    result = cursor.execute(sorgu,(session["username"],id))
    if result>0:
        sorgu2 = "Delete from articles where id = %s"
        cursor.execute(sorgu2,(id,))
        mysql.connection.commit()
        return redirect(url_for("dashboard"))
    else:
        flash("Böyle bir makale yok veya bu işleme yetkiniz yok...","danger")
        return redirect(url_for("index"))
    cursor.close()

#Makale Güncelleme
@app.route("/edit/<string:id>",methods=["GET","POST"])
@login_required
def makale_guncelle(id):
    if request.method == "GET":
        cursor = mysql.connection.cursor()
        sorgu = "Select * from articles where id = %s and author = %s"
        result = cursor.execute(sorgu,(id,session["username"]))
        if result == 0:
            flash("Böyle bir makale yok veya bu işleme yetkiniz yok","danger")
            return redirect(url_for("index"))
        else:
            article = cursor.fetchone()
            form = ArticleForm()
            form.title.data = article["title"]
            form.content.data = article["content"]
            return render_template("update.html",form = form)

    else:
        form = ArticleForm(request.form)
        newtitle= form.title.data
        newcontent = form.content.data
        sorgu2 = "Update articles Set title = %s,content = %s where id = %s"
        cursor = mysql.connection.cursor()
        cursor.execute(sorgu2,(newtitle,newcontent,id))
        mysql.connection.commit()
        flash("Makale başarıyla güncellendi","success")
        return redirect(url_for("dashboard"))

#Ara Yapma Kısmı
@app.route("/search",methods=["GET","POST"])
def search():
    if request.method =="GET":
        return redirect(url_for("index"))
    else:
        keyword = request.form.get("keyword")
        cursor = mysql.connection.cursor()
        sorgu ="Select * from articles where title like '%" + keyword +"%' "
        result = cursor.execute(sorgu)
        if result == 0:
            flash("Aranan kelime bulunamadı","warning")
            return redirect(url_for("makaleler"))
        else:
            articles = cursor.fetchall()
            return render_template("articles.html",articles = articles)






if __name__ == "__main__":
    app.run(debug=True)