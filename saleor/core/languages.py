"""List of all languages supported in Saleor.

Generated with Babel:

from babel import Locale
from babel.localedata import locale_identifiers

EXCLUDE = [
    "ar_001",
    "en_US_POSIX",
    "en_001",
    "en_150",
    "eo_001",
    "es_419",
    "ia_001",
    "prg_001",
    "vo_001",
    "yi_001",
]

languages = []

for lid in sorted(locale_identifiers()):
    if lid not in EXCLUDE:
        languages.append((lid.replace("_", "-"), Locale.parse(lid).english_name))
"""


LANGUAGES = [

    ("cs", "Czech"),
    ("de", "German"),
    ("en", "English"),
    ("es", "Spanish"),
    ("fr", "French"),
    ("he", "Hebrew"),
    ("hu", "Hungarian"),
    ("hy", "Armenian"),
    ("it", "Italian"),
    ("ka", "Georgian"),
    ("kk", "Kazakh"),
    ("ky", "Kyrgyz"),
    ("lt", "Lithuanian"),
    ("lv", "Latvian"),
    ("pl", "Polish"),
    ("pt", "Portuguese"),
    ("ru", "Russian"),
    ("sk", "Slovak"),
    ("sl", "Slovenian"),
    ("tr", "Turkish"),
    ("tt", "Tatar"),
    ("uz", "Uzbek"),
]
