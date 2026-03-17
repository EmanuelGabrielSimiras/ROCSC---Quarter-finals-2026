@app.route('/game', methods=['GET', 'POST'])
@login_required
def game():
    if request.method == 'POST':
        # aici se preia raspunsul meu
        user_answer = request.form.get('captcha_answer', type=int)
        captcha_id = session.get('captcha_id')
        # cauta solutia in memorie
        correct_answer = captcha_storage.get(captcha_id)
        
        # dupa prima incercare, solutia este stearsa
        if captcha_id in captcha_storage:
            del captcha_storage[captcha_id]
        session.pop('captcha_id', None)

        # bug-ul- daca ambele sunt none, verificarea trece
        if user_answer != correct_answer:
            flash("ERROR: Optical Sensors Misaligned.", "error")
            return redirect(url_for('game'))
