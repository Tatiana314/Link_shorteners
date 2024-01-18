from random import choices
from flask import flash, redirect, render_template, url_for

from . import app
from .constants import LEN_SHORT, ORIGINAL_LINK_VIEW, SHORT_LINK_SIMBOLS
from .forms import URLMapForm
from .models import URLMap

LINK_CREATED = 'Ваша новая ссылка готова'


def get_unique_short_id():
    short = ''.join(choices(SHORT_LINK_SIMBOLS, k=LEN_SHORT))
    while URLMap.query.filter_by(short=short).count():
        short = ''.join(choices(SHORT_LINK_SIMBOLS, k=LEN_SHORT))
    return short


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        if not form.custom_id.data:
            form.custom_id.data = get_unique_short_id()
        flash(LINK_CREATED)
        return render_template(
            'index.html',
            form=form,
            url_short=url_for(
                ORIGINAL_LINK_VIEW,
                short=URLMap.save_link(
                    original=form.original_link.data,
                    short=form.custom_id.data
                ).short, _external=True
            ))
    return render_template('index.html', form=form)


@app.route('/<string:short>')
def original_link_view(short):
    return redirect(URLMap.query.filter_by(short=short).first_or_404().original)
