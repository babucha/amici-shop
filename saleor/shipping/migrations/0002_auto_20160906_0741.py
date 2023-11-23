# Generated by Django 1.10.1 on 2016-09-06 12:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("shipping", "0001_initial")]

    operations = [
        migrations.AlterModelManagers(name="shippingmethodcountry", managers=[]),
        migrations.AlterField(
            model_name="shippingmethod",
            name="description",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="shippingmethodcountry",
            name="country_code",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "Any country"),
                    ("PN", "Pitcairn"),
                    ("KW", "Kuwait"),
                    ("MZ", "Mozambique"),
                    ("US", "United States of America"),
                    ("TC", "Turks and Caicos Islands"),
                    ("PM", "Saint Pierre and Miquelon"),
                    ("AZ", "Azerbaijan"),
                    ("DK", "Denmark"),
                    ("MX", "Mexico"),
                    ("SG", "Singapore"),
                    ("GS", "South Georgia and the South Sandwich Islands"),
                    ("CZ", "Czech Republic"),
                    ("NP", "Nepal"),
                    ("TT", "Trinidad and Tobago"),
                    ("FO", "Faroe Islands"),
                    ("BR", "Brazil"),
                    ("AM", "Armenia"),
                    ("IS", "Iceland"),
                    ("CA", "Canada"),
                    ("CW", "Curaçao"),
                    ("ZA", "South Africa"),
                    ("ER", "Eritrea"),
                    ("LV", "Latvia"),
                    ("HT", "Haiti"),
                    ("GT", "Guatemala"),
                    ("KY", "Cayman Islands"),
                    ("SC", "Seychelles"),
                    ("MK", "Macedonia (the former Yugoslav Republic of)"),
                    ("CK", "Cook Islands"),
                    ("MU", "Mauritius"),
                    ("DM", "Dominica"),
                    ("IM", "Isle of Man"),
                    ("UA", "Ukraine"),
                    ("RS", "Serbia"),
                    ("PH", "Philippines"),
                    ("IE", "Ireland"),
                    ("NR", "Nauru"),
                    ("BM", "Bermuda"),
                    ("IQ", "Iraq"),
                    ("MW", "Malawi"),
                    ("AL", "Albania"),
                    ("EC", "Ecuador"),
                    ("MV", "Maldives"),
                    ("BA", "Bosnia and Herzegovina"),
                    ("GA", "Gabon"),
                    ("CD", "Congo (the Democratic Republic of the)"),
                    ("MP", "Northern Mariana Islands"),
                    ("ES", "Spain"),
                    ("IT", "Italy"),
                    ("BV", "Bouvet Island"),
                    ("SX", "Sint Maarten (Dutch part)"),
                    ("GU", "Guam"),
                    ("GM", "Gambia"),
                    ("SR", "Suriname"),
                    ("BB", "Barbados"),
                    ("VI", "Virgin Islands (U.S.)"),
                    ("AU", "Australia"),
                    ("BJ", "Benin"),
                    ("BW", "Botswana"),
                    ("PF", "French Polynesia"),
                    ("GN", "Guinea"),
                    ("BQ", "Bonaire, Sint Eustatius and Saba"),
                    ("MF", "Saint Martin (French part)"),
                    ("CH", "Switzerland"),
                    ("FI", "Finland"),
                    ("PS", "Palestine, State of"),
                    ("IR", "Iran (Islamic Republic of)"),
                    ("TW", "Taiwan (Province of China)"),
                    ("ML", "Mali"),
                    ("BY", "Belarus"),
                    ("EG", "Egypt"),
                    ("NU", "Niue"),
                    ("RU", "Russian Federation"),
                    ("NF", "Norfolk Island"),
                    ("MS", "Montserrat"),
                    ("TM", "Turkmenistan"),
                    ("FJ", "Fiji"),
                    ("HR", "Croatia"),
                    ("IN", "India"),
                    ("MR", "Mauritania"),
                    ("PG", "Papua New Guinea"),
                    ("MQ", "Martinique"),
                    ("BE", "Belgium"),
                    ("AG", "Antigua and Barbuda"),
                    ("ID", "Indonesia"),
                    ("CL", "Chile"),
                    ("DO", "Dominican Republic"),
                    ("IO", "British Indian Ocean Territory"),
                    ("DE", "Germany"),
                    ("PT", "Portugal"),
                    ("SS", "South Sudan"),
                    ("KH", "Cambodia"),
                    ("AF", "Afghanistan"),
                    ("TV", "Tuvalu"),
                    ("CF", "Central African Republic"),
                    ("HN", "Honduras"),
                    ("BN", "Brunei Darussalam"),
                    ("KZ", "Kazakhstan"),
                    ("JE", "Jersey"),
                    ("KI", "Kiribati"),
                    ("JM", "Jamaica"),
                    ("KM", "Comoros"),
                    ("GE", "Georgia"),
                    ("KP", "Korea (the Democratic People's Republic of)"),
                    ("GL", "Greenland"),
                    ("UG", "Uganda"),
                    ("MT", "Malta"),
                    ("CC", "Cocos (Keeling) Islands"),
                    ("CI", "Côte d'Ivoire"),
                    ("GR", "Greece"),
                    ("VC", "Saint Vincent and the Grenadines"),
                    ("NA", "Namibia"),
                    ("LY", "Libya"),
                    ("GP", "Guadeloupe"),
                    ("BD", "Bangladesh"),
                    ("NI", "Nicaragua"),
                    ("PK", "Pakistan"),
                    ("TD", "Chad"),
                    ("MH", "Marshall Islands"),
                    ("TJ", "Tajikistan"),
                    ("TH", "Thailand"),
                    ("LB", "Lebanon"),
                    ("NC", "New Caledonia"),
                    ("GI", "Gibraltar"),
                    ("CM", "Cameroon"),
                    ("DZ", "Algeria"),
                    ("ST", "Sao Tome and Principe"),
                    ("KR", "Korea (the Republic of)"),
                    ("CX", "Christmas Island"),
                    ("MO", "Macao"),
                    ("SD", "Sudan"),
                    ("CY", "Cyprus"),
                    ("TL", "Timor-Leste"),
                    ("NO", "Norway"),
                    ("KN", "Saint Kitts and Nevis"),
                    ("LA", "Lao People's Democratic Republic"),
                    ("GQ", "Equatorial Guinea"),
                    ("NE", "Niger"),
                    ("AE", "United Arab Emirates"),
                    ("BT", "Bhutan"),
                    ("HM", "Heard Island and McDonald Islands"),
                    ("SO", "Somalia"),
                    ("UY", "Uruguay"),
                    ("LC", "Saint Lucia"),
                    ("JP", "Japan"),
                    ("SJ", "Svalbard and Jan Mayen"),
                    ("GD", "Grenada"),
                    ("ME", "Montenegro"),
                    ("GB", "United Kingdom of Great Britain and Northern Ireland"),
                    ("TO", "Tonga"),
                    ("VA", "Holy See"),
                    ("IL", "Israel"),
                    ("HU", "Hungary"),
                    ("AD", "Andorra"),
                    ("SE", "Sweden"),
                    ("BZ", "Belize"),
                    ("AS", "American Samoa"),
                    ("PR", "Puerto Rico"),
                    ("BH", "Bahrain"),
                    ("CN", "China"),
                    ("LK", "Sri Lanka"),
                    ("PE", "Peru"),
                    ("BG", "Bulgaria"),
                    ("AW", "Aruba"),
                    ("AQ", "Antarctica"),
                    ("GY", "Guyana"),
                    ("TG", "Togo"),
                    ("OM", "Oman"),
                    ("CG", "Congo"),
                    ("TR", "Turkey"),
                    ("EE", "Estonia"),
                    ("MA", "Morocco"),
                    ("BL", "Saint Barthélemy"),
                    ("SK", "Slovakia"),
                    ("TF", "French Southern Territories"),
                    ("AT", "Austria"),
                    ("GG", "Guernsey"),
                    ("LU", "Luxembourg"),
                    ("SM", "San Marino"),
                    ("ET", "Ethiopia"),
                    ("HK", "Hong Kong"),
                    ("UM", "United States Minor Outlying Islands"),
                    ("LT", "Lithuania"),
                    ("WF", "Wallis and Futuna"),
                    ("VE", "Venezuela (Bolivarian Republic of)"),
                    ("FK", "Falkland Islands  [Malvinas]"),
                    ("QA", "Qatar"),
                    ("AO", "Angola"),
                    ("MG", "Madagascar"),
                    ("CV", "Cabo Verde"),
                    ("SA", "Saudi Arabia"),
                    ("SH", "Saint Helena, Ascension and Tristan da Cunha"),
                    ("EH", "Western Sahara"),
                    ("RW", "Rwanda"),
                    ("WS", "Samoa"),
                    ("BS", "Bahamas"),
                    ("SL", "Sierra Leone"),
                    ("LS", "Lesotho"),
                    ("ZM", "Zambia"),
                    ("BI", "Burundi"),
                    ("ZW", "Zimbabwe"),
                    ("LI", "Liechtenstein"),
                    ("FM", "Micronesia (Federated States of)"),
                    ("GH", "Ghana"),
                    ("CU", "Cuba"),
                    ("RE", "Réunion"),
                    ("MY", "Malaysia"),
                    ("GF", "French Guiana"),
                    ("KG", "Kyrgyzstan"),
                    ("FR", "France"),
                    ("PY", "Paraguay"),
                    ("JO", "Jordan"),
                    ("LR", "Liberia"),
                    ("PA", "Panama"),
                    ("RO", "Romania"),
                    ("YE", "Yemen"),
                    ("TK", "Tokelau"),
                    ("SI", "Slovenia"),
                    ("AI", "Anguilla"),
                    ("BF", "Burkina Faso"),
                    ("MM", "Myanmar"),
                    ("KE", "Kenya"),
                    ("VU", "Vanuatu"),
                    ("BO", "Bolivia (Plurinational State of)"),
                    ("PL", "Poland"),
                    ("NL", "Netherlands"),
                    ("VN", "Viet Nam"),
                    ("SV", "El Salvador"),
                    ("SN", "Senegal"),
                    ("TN", "Tunisia"),
                    ("PW", "Palau"),
                    ("GW", "Guinea-Bissau"),
                    ("UZ", "Uzbekistan"),
                    ("CR", "Costa Rica"),
                    ("SB", "Solomon Islands"),
                    ("SZ", "Swaziland"),
                    ("MD", "Moldova (the Republic of)"),
                    ("YT", "Mayotte"),
                    ("DJ", "Djibouti"),
                    ("SY", "Syrian Arab Republic"),
                    ("MN", "Mongolia"),
                    ("NZ", "New Zealand"),
                    ("AX", "Åland Islands"),
                    ("TZ", "Tanzania, United Republic of"),
                    ("MC", "Monaco"),
                    ("VG", "Virgin Islands (British)"),
                    ("AR", "Argentina"),
                    ("CO", "Colombia"),
                    ("NG", "Nigeria"),
                ],
                default="",
                max_length=2,
            ),
        ),
    ]
