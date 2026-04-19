@app.route('/result3', methods=['GET', 'POST'])
def result3():
    res = None
    
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        phone = request.form.get('phone', '').strip()

        if len(name) > 2 and phone.startswith('+') and len(phone) >= 11:
            res = [name, phone]
        else:
            res = ["Ma'lumotlar noto'g'ri kiritildi"]

    return render_template('result3.html', res=res)
