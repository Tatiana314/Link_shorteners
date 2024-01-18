from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, ValidationError
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp

from .models import URLMap

from .constants import LINK_EXISTS, MAX_LEN_SHORT, SHORT_LINK_SIMBOLS

CUSTOM_ID = 'Ссылка должна состоять из латинских букв и цифр в диапазоне от 0 до 9'
REGULAR_EXPR = f'^[{SHORT_LINK_SIMBOLS}]+$'
MESSAGE_FIELD = 'Обязательное поле'
LABEL_ORIGINAL_LINK = 'Введите ссылку'
LABEL_CUSTOM_ID = 'Введите короткую ссылку'
LABEL_SUBMIT = 'Создать'


class URLMapForm(FlaskForm):
    original_link = URLField(
        LABEL_ORIGINAL_LINK,
        validators=[
            DataRequired(message=MESSAGE_FIELD),
            URL(),
            Length(max=2000)]
    )
    custom_id = StringField(
        LABEL_CUSTOM_ID,
        validators=[
            Regexp(REGULAR_EXPR, message=CUSTOM_ID),
            Length(max=MAX_LEN_SHORT),
            Optional()
        ])
    submit = SubmitField(LABEL_SUBMIT)

    def validate_custom_id(self, field):
        if URLMap.query.filter_by(short=field.data).count():
            raise ValidationError(LINK_EXISTS)
