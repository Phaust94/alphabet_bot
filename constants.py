import string
import re

ALPHABET_UA = "а, б, в, г, ґ, д, е, є, ж, з, и, і, ї, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ь, ю, я".split(", ")
ALPHABET_RUNE = [
    "1399",
    "06DE",
    "058D",
    "07F6",
    "0B70",
    "0BF8",
    "0482",  # e
    "0F03",
    "0F17",
    "0F15",
    "0FC4",
    "1b68",     # i
    "109E",
    "0fcf",
    "1b7c",
    "19E7",
    "214f",     # m
    "19F7",
    "21d5",
    "213A",
    "2318",
    "0fbf",
    "0f13",
    "21dc",     # u
    "2328",
    "233E",
    "235D",
    "2361",
    "2306",
    "2305",
    "236D",
    "2355",
    "2563",
]

ALPHABET_RUNE = [chr(int(x, 16)) for x in ALPHABET_RUNE]

TRANSLATOR = str.maketrans("".join(ALPHABET_UA), "".join(ALPHABET_RUNE))

ZAPOVIT = """
Тарас Шевченко. "Заповіт"

Як умру, то поховайте

Мене на могилі

Серед степу широкого

На Вкраїні милій,

Щоб лани широкополі,

І Дніпро, і кручі

Було видно, було чути,

Як реве ревучий.

Як понесе з України

У синєє море

Кров ворожу... отойді я

І лани і гори —

Все покину, і полину

До самого Бога

Молитися... а до того

Я не знаю Бога.

Поховайте та вставайте,

Кайдани порвіте

І вражою злою кров’ю

Волю окропіте.

І мене в сем’ї великій,

В сем’ї вольній, новій,

Не забудьте пом’янути

Незлим тихим словом.""".lower()

ZAPOVIT_TRANSLATED = ZAPOVIT.translate(TRANSLATOR)

ABETKA_TRANSLATED = "тут ви можете дізнатись абетку. введіть літеру - і я перекладу її".translate(TRANSLATOR)

LONG_TRANSLATED = "це було б занадто легко. Тільки по 1 букві можна".lower().translate(TRANSLATOR)

ALLOWED_SYMBOLS = ALPHABET_UA + string.punctuation.split() + ALPHABET_RUNE + [" ", "’", "\n", "—"]
PAT = r"[^{}]".format("".join(ALLOWED_SYMBOLS))
BAD_SYMBOLS_REGEX = re.compile(PAT)

BAD_MESSAGE_TRANLATED = "тут щось незрозуміле".translate(TRANSLATOR)
ONLY_OUR_SYMBOLS_REGEX = re.compile(r"[{}]".format("".join(ALPHABET_RUNE)))

ERROR = "на жаль, сталась помилка".translate(TRANSLATOR)

EASTER_EGG_TEXT = "Яка відповідь на питання життя, Всесвіту і взагалі?".lower().translate(TRANSLATOR)
EASTER_EGG_CORRECT = "Вірно!!!".lower().translate(TRANSLATOR)
EASTER_EGG_INCORRECT = "Ви хіба \"Путівник Галактикою\" не дивились?".lower().translate(TRANSLATOR)
