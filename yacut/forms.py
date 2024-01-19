from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, ValidationError
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp

from .constants import (CUSTOM_ID, LABEL_CUSTOM_ID, LABEL_ORIGINAL_LINK,
                        LABEL_SUBMIT, LINK_EXISTS, MAX_LEN_ORIGINAL_LINK,
                        MAX_LEN_SHORT, MESSAGE_FIELD, REGEX)
from .models import URLMap


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
        if URLMap.query.filter_by(short=field.data).count():
            raise ValidationError(LINK_EXISTS)
