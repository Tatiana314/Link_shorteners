from string import ascii_letters, digits


MAX_LEN_ORIGINAL_LINK = 2000
MAX_LEN_SHORT = 16
LEN_SHORT = 6

SHORT_LINK_SIMBOLS = ascii_letters + digits
REGEX = r'^[a-zA-Z0-9]{1,16}$'

ORIGINAL_LINK_VIEW = 'original_link_view'

LINK_EXISTS = 'Предложенный вариант короткой ссылки уже существует.'
REQUEST_ERROR = 'Отсутствует тело запроса'
LINK_CREATED = 'Ваша новая ссылка готова'
URL = '"url" является обязательным полем!'
SHORT_LINK_NAME = 'Указано недопустимое имя для короткой ссылки'
OBJECT_ERROE = 'Указанный id не найден'

CUSTOM_ID = 'Ссылка должна состоять из латинских букв и цифр в диапазоне от 0 до 9'
MESSAGE_FIELD = 'Обязательное поле'
LABEL_ORIGINAL_LINK = 'Введите ссылку'
LABEL_CUSTOM_ID = 'Введите короткую ссылку'
LABEL_SUBMIT = 'Создать'
