from flask import flash, redirect, url_for, render_template

from idea4u.models import Idea
from idea4u.form import IdeaForm
from idea4u import app, db


# Application Routes

@app.route('/', methods=['GET', 'POST'])
def index():
    messages = Idea.query.order_by(Idea.timestamp.desc()).all()
    form = IdeaForm()
    if form.validate_on_submit():
        topic = form.topic.data
        idea = form.idea.data
        writer = form.writer.data
        msg = Idea(topic=topic, idea=idea, writer=writer)
        db.session.add(msg)
        db.session.commit()
        flash("你的好点子已经提交！")
        return redirect(url_for('index'))
    return render_template('index.html', form=form, messages=messages)



