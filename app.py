from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "secreat-key" # ganti yang lebih aman
UPLOAD_FOLDER =  "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# simpan data di memori 
data_list = []

@app.route("/", methods=["GET", "POST"])
def form_upload() :
    if request.method == "POST":
        nama_penyidik = request.form.get("nama_penyidik")
        nama_kanit = request.form.get("nama_penyidik")
        file = request.files.get("file")

        if not nama_penyidik or not nama_kanit or not file :
            flash("Semua field wajib diisi !", "danger")
            return redirect (url_for("form_upload"))
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save (file_path)

        data_list.append({
            "penyidik" : nama_penyidik,
            "kanit" : nama_kanit, 
            "file" : filename
        })

        flash("data berhasil disimpan!", "success")
        return redirect(url_for("form_upload"))
    return render_template ("form.html", data_list=data_list)

if __name__ == "__main__":
    app.run(debug=True)