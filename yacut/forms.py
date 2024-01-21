from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, ValidationError
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp

from .constants import MAX_LEN_ORIGINAL_LINK, MAX_LEN_SHORT, REGEX
from .models import URLMap

CUSTOM_ID = (
    'Ссылка должна состоять из латинских'
    'букв и цифр в диапазоне от 0 до 9'
)
MESSAGE_FIELD = 'Обязательное поле'
LABEL_ORIGINAL_LINK = 'Введите ссылку'
LABEL_CUSTOM_ID = 'Введите короткую ссылку'
LABEL_SUBMIT = 'Создать'
LINK_EXISTS = 'Предложенный вариант короткой ссылки уже существует.'


class URLMapForm(FlaskForm):
    original_link = URLField(
        LABEL_ORIGINAL_LINK,
        validators=[
            DataRequired(message=MESSAGE_FIELD),
            URL(),
            Length(max=MAX_LEN_ORIGINAL_LINK)]
    )
    custom_id = StringField(
        LABEL_CUSTOM_ID,
        validators=[
            Regexp(REGEX, message=CUSTOM_ID),
            Length(max=MAX_LEN_SHORT),
            Optional()
        ])
    submit = SubmitField(LABEL_SUBMIT)

    def validate_custom_id(self, field):
        if URLMap.get(short=field.data):
            raise ValidationError(LINK_EXISTS)
