from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp

CUSTOM_ID = 'Ссылка должна состоять из латинских букв и цифр в диапазоне от 0 до 9'
REGULAR_EXPR = '^[a-zA-Z0-9]+$'
MESSAGE_FIELD = 'Обязательное поле'


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Введите ссылку',
        validators=[DataRequired(message=MESSAGE_FIELD), URL()]
    )
    custom_id = StringField(
        'Введите короткую ссылку',
        validators=[
            Regexp(REGULAR_EXPR, message=CUSTOM_ID),
            Length(0, 16),
            Optional()
        ])
    submit = SubmitField('Создать')
