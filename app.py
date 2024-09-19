import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv
import time

# Fungsi untuk mengirim email dengan HTML
def kirim_email_html(from_email, password, to_email, subject, html_message):
    # Setup MIME
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # Menambahkan isi pesan HTML
    msg.attach(MIMEText(html_message, 'html'))

    try:
        # Menghubungkan ke SMTP server Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print(f"Email berhasil dikirim ke {to_email}")
    except Exception as e:
        print(f"Gagal mengirim email ke {to_email}. Error: {str(e)}")

# Pengaturan akun email pengirim
email_pengirim = ""  # Ganti dengan email pengirim
password_pengirim = ""

# Membaca CSV yang berisi nama, email, email institusi, dan password
with open('data_murid1.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        name = row['name']
        email = row['email']  # Email pribadi
        email_il = row['email-il']  # Email institusi
        password_il = row['password']  # Password institusi
        mentor = row['personal']
        # HTML message dengan table email institusi dan password spesifik per murid
        html_message = f"""
     <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Selamat Datang di Infinite Learning!</title>
</head>

<body>
    <div style="display: flex; justify-content: center; flex-direction: column; align-items: center; margin: 10px;">
        <div
            style="width: 95%; border: 2px solid purple; padding: 1em; margin: 1em 0.5em 1em 0.5em; border-radius: 7px;">
            <span>
                <h2 style="text-align: center;">Selamat datang di Program Advanced Artificial Intelligence, {name}!🤩🔥
                </h2>
                <br>
                Hi {name}!
                <br>
                Dengan senang hati kami menyambut kamu sebagai bagian dari Warga Infinite Learning (WIL) 🐳
                <br>
                Berikut informasi terkait account email Infinite Learning kamu.
            </span>
            <table style="border: 1px solid black; border-collapse: collapse; margin: 12px 0px 12px 0px;">
                <tr>
                    <th
                        style="font-size: 12px; font-weight: bolder; border: 1px solid black; padding: 8px; text-align: left; background-color: #f2f2f2;">
                        E-mail Infinite Learning</th>
                    <td
                        style="font-size: 12px; font-weight: bolder; border: 1px solid black; padding: 8px; text-align: left;">
                        {email_il}</td>
                </tr>
                <tr>
                    <th
                        style="font-size: 12px; font-weight: bolder; border: 1px solid black; padding: 8px; text-align: left; background-color: #f2f2f2;">
                        Password</th>
                    <td
                        style="font-size: 12px; font-weight: bolder; border: 1px solid black; padding: 8px; text-align: left;">
                        {password_il}</td>
                </tr>
                <tr>
                    <th
                        style="font-size: 12px; font-weight: bolder; border: 1px solid black; padding: 8px; text-align: left; background-color: #f2f2f2;">
                        Mentor Personal</th>
                    <td
                        style="font-size: 12px; font-weight: bolder; border: 1px solid black; padding: 8px; text-align: left;">
                        {mentor}</td>
                </tr>
            </table>
            <div>
                <div style="background-color: aquamarine; padding: 7px; text-align: center; border-radius: 7px;">
                    Email ini akan dipakai untuk <strong>akun LMS Infinite Learning dan IBM Cloud</strong>, jangan
                    digunakan untuk mendaftar di IBM SkillsBuild, Cognitive Class AI dan lain-lain, silakan gunakan akun
                    pribadi untuk platform selain LMS dan IBM Cloud!
                </div>
                <br>
                Silahkan kamu ikuti panduan Link Notion di bawah ini untuk tata cara penggunaan email: <br>
                <a href="https://fortune-chard-9e3.notion.site/Akun-Email-Infinite-Learning-13375758b26149268b4c70f49037233a?pvs=4"
                    target="_blank">https://fortune-chard-9e3.notion.site/Akun-Email-Infinite-Learning-13375758b26149268b4c70f49037233a?pvs=4</a>
                <br>
                <br>
                Harap segera login di <a
                    href="https://webmail.infinitelearningstudent.id">https://webmail.infinitelearningstudent.id</a>
                menggunakan detail ini dan <strong>ubah kata sandi anda</strong> untuk keamanan yang lebih baik.
                <br>
                Jika Anda memiliki pertanyaan atau butuh bantuan, jangan ragu untuk menghubungi mentornya ya!
                <br>
                Selamat belajar dan sukses selalu!
                <br>
                <br>
                Salam hangat!
                <br>

                Mentor Advanced Artificial Intelligence
                <br>
                Infinite Learning
            </div>
        </div>
    </div>
</body>

</html>
        """
        
        # Subjek email
        subject = f"Informasi Akun Infinite Learning - {name}"
        
        # Kirim email ke masing-masing murid (email pribadi)
        kirim_email_html(email_pengirim, password_pengirim, email, subject, html_message)
        time.sleep(2)  # Jeda antar email

print("Semua email telah dikirim")
