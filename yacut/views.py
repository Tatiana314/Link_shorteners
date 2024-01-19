from flask import abort, redirect, render_template, url_for

from . import app
from .constants import ORIGINAL_LINK_VIEW
from .forms import URLMapForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    url_map = URLMap.save(
        original=form.original_link.data,
        short=form.custom_id.data
    )
    return render_template(
        'index.html',
        form=form,
        url_short=url_for(
            ORIGINAL_LINK_VIEW,
            short=url_map.short,
            _external=True
        ))


@app.route('/<string:short>')
def original_link_view(short):
    url_map = URLMap.get_object(short=short)
    if url_map:
        return redirect(url_map.original)
    abort(404)
