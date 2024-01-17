from random import choices
from flask import flash, redirect, render_template

from . import app, db
from .constants import LEN_SHORT, SHORT_LINK_SIMBOLS
from .forms import URLMapForm
from .models import URLMap

LINK_CREATED = 'Ваша новая ссылка готова'
LINK_EXISTS = 'Предложенный вариант короткой ссылки уже существует.'


def get_unique_short_id():
    return ''.join(choices(SHORT_LINK_SIMBOLS, k=LEN_SHORT))


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        if form.custom_id.data and URLMap.query.filter_by(short=form.custom_id.data).count():
            flash(LINK_EXISTS)
            return render_template('url_map.html', form=form)
        if not form.custom_id.data:
            form.custom_id.data = get_unique_short_id()
            while URLMap.query.filter_by(short=form.custom_id.data).count():
                form.custom_id.data = get_unique_short_id()
        db.session.add(
            URLMap(original=form.original_link.data, short=form.custom_id.data)
        )
        db.session.commit()
        flash(LINK_CREATED)
    return render_template('url_map.html', form=form)


@app.route('/<string:short>')
def original_link_view(short):
    return redirect(URLMap.query.filter_by(short=short).first_or_404().original)
