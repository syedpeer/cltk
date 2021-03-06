"""Converts legacy encodings into Unicode.

TODO: Rm regex dependency
TODO: Add tests
"""

# pylint: disable=anomalous-backslash-in-string

import regex

BETA_REPLACE_UPPER = [
    # Perseus-style head words
    # CAPS smooth
    (r"\*\)A", "Ἀ"),
    (r"\*\)E", "Ἐ"),
    (r"\*\)H", "Ἠ"),
    (r"\*\)I", "Ἰ"),
    (r"\*\)O", "Ὀ"),
    (r"\*\)W", "Ὠ"),
    # CAPS rough
    (r"\*\(A", "Ἁ"),
    (r"\*\(E", "Ἑ"),
    (r"\*\(H", "Ἡ"),
    (r"\*\(I", "Ἱ"),
    (r"\*\(O", "Ὁ"),
    (r"\*\(R", "Ῥ"),
    (r"\*\(U", "Ὑ"),
    (r"\*\(W", "Ὡ"),
    # CAPS circumflex
    (r"\*\)=A", "Ἆ"),
    (r"\*\)=H", "Ἦ"),
    (r"\*\)=I", "Ἶ"),
    (r"\*\)=W", "Ὦ"),
    (r"\*\(=A", "Ἇ"),
    (r"\*\(=H", "Ἧ"),
    (r"\*\(=I", "Ἷ"),
    (r"\*\(=U", "Ὗ"),
    (r"\*\(=W", "Ὧ"),
    # CAPS smooth grave
    (r"\*\)\\A", "Ἂ"),
    (r"\*\)\\E", "Ἒ"),
    (r"\*\)\\H", "Ἢ"),
    (r"\*\)\\I", "Ἲ"),
    (r"\*\)\\O", "Ὂ"),
    (r"\*\)\\W", "Ὢ"),
    # CAPS rough grave
    (r"\*\(\\A", "Ἃ"),
    (r"\*\(\\E", "Ἓ"),
    (r"\*\(\\H", "Ἣ"),
    (r"\*\(\\I", "Ἳ"),
    (r"\*\(\\O", "Ὃ"),
    (r"\*\(\\U", "Ὓ"),
    (r"\*\(\\W", "Ὣ"),
    # CAPS smooth acute
    (r"\*\)/A", "Ἄ"),
    (r"\*\)/E", "Ἔ"),
    (r"\*\)/H", "Ἤ"),
    (r"\*\)/I", "Ἴ"),
    (r"\*\)/O", "Ὄ"),
    (r"\*\)/W", "Ὤ"),
    # CAPS rough acute
    (r"\*\(/A", "Ἅ"),
    (r"\*\(/E", "Ἕ"),
    (r"\*\(/H", "Ἥ"),
    (r"\*\(/I", "Ἵ"),
    (r"\*\(/O", "Ὅ"),
    (r"\*\(/U", "Ὕ"),
    (r"\*\(/W", "Ὥ"),
    # TLG-style
    (r"\*A\'", "Ᾰ"),
    (r"\*I\'", "Ῐ"),
    (r"\*U\'", "Ῠ"),
    (r"\*A&", "Ᾱ"),
    (r"\*I&", "Ῑ"),
    (r"\*U&", "Ῡ"),
    (r"\*R\(", "Ῥ"),
    (r"\*A\)\|", "ᾈ"),
    (r"\*A\(\|", "ᾉ"),
    (r"\*A\)\\\|", "ᾊ"),
    (r"\*A\(\\\|", "ᾋ"),
    (r"\*A\)/\|", "ᾌ"),
    (r"\*A\(/\|", "ᾍ"),
    (r"\*A\)=\|", "ᾎ"),
    (r"\*A\(=\|", "ᾏ"),
    (r"\*H\)\|", "ᾘ"),
    (r"\*H\(\|", "ᾙ"),
    (r"\*H\)\\\|", "ᾚ"),
    (r"\*H\(\\\|", "ᾛ"),
    (r"\*H\)/\|", "ᾜ"),
    (r"\*H\(/\|", "ᾝ"),
    (r"\*H\)=\|", "ᾞ"),
    (r"\*H\(=\|", "ᾟ"),
    (r"\*\)\|", "ᾨ"),
    (r"\*\(\|", "ᾩ"),
    (r"\*\)\\\|", "ᾪ"),
    (r"\*\(\\\|", "ᾫ"),
    (r"\*\)/\|", "ᾬ"),
    (r"\*\(/\|", "ᾭ"),
    (r"\*\)=\|", "ᾮ"),
    (r"\*\(=\|", "ᾯ"),
    (r"\*A\)\\", "Ἂ"),
    (r"\*A\(\\", "Ἃ"),
    (r"\*E\)\\", "Ἒ"),
    (r"\*E\(\\", "Ἓ"),
    (r"\*H\)\\", "Ἢ"),
    (r"\*H\(\\", "Ἣ"),
    (r"\*I\)\\", "Ἲ"),
    (r"\*I\(\\", "Ἳ"),
    (r"\*O\)\\", "Ὂ"),
    (r"\*O\(\\", "Ὃ"),
    (r"\*U\(\\", "Ὓ"),
    (r"\*W\)\\", "Ὢ"),
    (r"\*W\(\\", "Ὣ"),
    (r"\*A\)/", "Ἄ"),
    (r"\*A\(/", "Ἅ"),
    (r"\*E\)/", "Ἔ"),
    (r"\*E\(/", "Ἕ"),
    (r"\*H\)/", "Ἤ"),
    (r"\*H\(/", "Ἥ"),
    (r"\*I\)/", "Ἴ"),
    (r"\*I\(/", "Ἵ"),
    (r"\*O\)/", "Ὄ"),
    (r"\*O\(/", "Ὅ"),
    (r"\*U\(/", "Ὕ"),
    (r"\*W\)/", "Ὤ"),
    (r"\*W\(/", "Ὥ"),
    (r"\*A\)=", "Ἆ"),
    (r"\*A\(=", "Ἇ"),
    (r"\*H\)=", "Ἦ"),
    (r"\*H\(=", "Ἧ"),
    (r"\*I\)=", "Ἶ"),
    (r"\*I\(=", "Ἷ"),
    (r"\*U\(=", "Ὗ"),
    (r"\*W\)=", "Ὦ"),
    (r"\*W\(=", "Ὧ"),
    (r"\*A=", "Ἆ"),
    (r"\*H=", "Ἦ"),
    (r"\*I=", "Ἶ"),
    (r"\*W=", "Ὦ"),
    (r"\*A\)", "Ἀ"),
    (r"\*A\(", "Ἁ"),
    (r"\*E\)", "Ἐ"),
    (r"\*E\(", "Ἑ"),
    (r"\*H\)", "Ἠ"),
    (r"\*H\(", "Ἡ"),
    (r"\*I\)", "Ἰ"),
    (r"\*I\(", "Ἱ"),
    (r"\*O\)", "Ὀ"),
    (r"\*O\(", "Ὁ"),
    (r"\*U\(", "Ὑ"),
    (r"\*W\)", "Ὠ"),
    (r"\*W\(", "Ὡ"),
    (r"\*A", "Α"),
    (r"\*B", "Β"),
    (r"\*C", "Ξ"),
    (r"\*D", "Δ"),
    (r"\*E", "Ε"),
    (r"\*F", "Φ"),
    (r"\*G", "Γ"),
    (r"\*H", "Η"),
    (r"\*I", "Ι"),
    (r"\*K", "Κ"),
    (r"\*L", "Λ"),
    (r"\*M", "Μ"),
    (r"\*N", "Ν"),
    (r"\*O", "Ο"),
    (r"\*P", "Π"),
    (r"\*Q", "Θ"),
    (r"\*R", "Ρ"),
    (r"\*S", "Σ"),
    (r"\*S3", "Σ"),
    (r"\*T", "Τ"),
    (r"\*U", "Υ"),
    (r"\*V", "Ϝ"),
    (r"\*W", "Ω"),
    (r"\*X", "Χ"),
    (r"\*Y", "Ψ"),
    (r"\*Z", "Ζ"),
]

BETA_REPLACE_LOWER = [
    (r"I\+", "ϊ"),
    (r"I\\\+", "ῒ"),
    (r"I/\+", "ΐ"),
    # Add a second entry for out-of-order betacode
    (r"I\+/", "ΐ"),
    (r"I=\+", "ῗ"),
    (r"U\+", "ϋ"),
    (r"U\\\+", "ῢ"),
    (r"U/\+", "ΰ"),
    (r"U=\+", "ῧ"),
    (r"A\'", "ᾰ"),
    (r"I\'", "ῐ"),
    (r"U\'", "ῠ"),
    (r"A&", "ᾱ"),
    (r"I&", "ῑ"),
    (r"U&", "ῡ"),
    (r"R\)", "ῤ"),
    (r"R\(", "ῥ"),
    (r"A\)\|", "ᾀ"),
    (r"A\(\|", "ᾁ"),
    (r"A\)\\\|", "ᾂ"),
    (r"A\(\\\|", "ᾃ"),
    (r"A\)/\|", "ᾄ"),
    (r"A\(/\|", "ᾅ"),
    (r"A\)=\|", "ᾆ"),
    (r"A\(=\|", "ᾇ"),
    (r"H\)\|", "ᾐ"),
    (r"H\(\|", "ᾑ"),
    (r"H\)\\\|", "ᾒ"),
    (r"H\(\\\|", "ᾓ"),
    (r"H\)/\|", "ᾔ"),
    (r"H\(/\|", "ᾕ"),
    (r"H\)=\|", "ᾖ"),
    (r"H\(=\|", "ᾗ"),
    (r"W\)\|", "ᾠ"),
    (r"W\(\|", "ᾡ"),
    (r"W\)\\\|", "ᾢ"),
    (r"W\(\\\|", "ᾣ"),
    (r"W\)/\|", "ᾤ"),
    (r"W\(/\|", "ᾥ"),
    (r"W\)=\|", "ᾦ"),
    (r"W\(=\|", "ᾧ"),
    (r"A\\\|", "ᾲ"),
    (r"A\|", "ᾳ"),
    (r"A/\|", "ᾴ"),
    (r"A=\|", "ᾷ"),
    (r"H\\\|", "ῂ"),
    (r"H\|", "ῃ"),
    (r"H/\|", "ῄ"),
    (r"H=\|", "ῇ"),
    (r"W\\\|", "ῲ"),
    (r"W\|", "ῳ"),
    (r"W/\|", "ῴ"),
    (r"W=\|", "ῷ"),
    (r"A\)\\", "ἂ"),
    (r"A\(\\", "ἃ"),
    (r"E\)\\", "ἒ"),
    (r"E\(\\", "ἓ"),
    (r"H\)\\", "ἢ"),
    (r"H\(\\", "ἣ"),
    (r"I\)\\", "ἲ"),
    (r"I\(\\", "ἳ"),
    (r"O\)\\", "ὂ"),
    (r"O\(\\", "ὃ"),
    (r"U\)\\", "ὒ"),
    (r"U\(\\", "ὓ"),
    (r"W\)\\", "ὢ"),
    (r"W\(\\", "ὣ"),
    (r"A\)/", "ἄ"),
    (r"A\(/", "ἅ"),
    (r"E\)/", "ἔ"),
    (r"E\(/", "ἕ"),
    (r"H\)/", "ἤ"),
    (r"H\(/", "ἥ"),
    (r"I\)/", "ἴ"),
    (r"I\(/", "ἵ"),
    (r"O\)/", "ὄ"),
    (r"O\(/", "ὅ"),
    (r"U\)/", "ὔ"),
    (r"U\(/", "ὕ"),
    (r"W\)/", "ὤ"),
    (r"W\(/", "ὥ"),
    (r"A\)=", "ἆ"),
    (r"A\(=", "ἇ"),
    (r"H\)=", "ἦ"),
    (r"H\(=", "ἧ"),
    (r"I\)=", "ἶ"),
    (r"I\(=", "ἷ"),
    (r"U\)=", "ὖ"),
    (r"U\(=", "ὗ"),
    (r"W\)=", "ὦ"),
    (r"W\(=", "ὧ"),
    (r"A=", "ᾶ"),
    (r"H=", "ῆ"),
    (r"I=", "ῖ"),
    (r"U=", "ῦ"),
    (r"W=", "ῶ"),
    (r"A\)", "ἀ"),
    (r"A\(", "ἁ"),
    (r"E\)", "ἐ"),
    (r"E\(", "ἑ"),
    (r"H\)", "ἠ"),
    (r"H\(", "ἡ"),
    (r"I\)", "ἰ"),
    (r"I\(", "ἱ"),
    (r"O\)", "ὀ"),
    (r"O\(", "ὁ"),
    (r"U\)", "ὐ"),
    (r"U\(", "ὑ"),
    (r"W\)", "ὠ"),
    (r"W\(", "ὡ"),
    (r"A\\", "ὰ"),
    (r"A/", "ά"),
    (r"E/", "έ"),
    (r"E\\", "ὲ"),
    (r"H/", "ή"),
    (r"H\\", "ὴ"),
    (r"I/", "ί"),
    (r"I\\", "ὶ"),
    (r"O/", "ό"),
    (r"O\\", "ὸ"),
    (r"U/", "ύ"),
    (r"U\\", "ὺ"),
    (r"W/", "ώ"),
    (r"W\\", "ὼ"),
    (r"A", "α"),
    (r"B", "β"),
    (r"C", "ξ"),
    (r"D", "δ"),
    (r"E", "ε"),
    (r"F", "φ"),
    (r"G", "γ"),
    (r"H", "η"),
    (r"I", "ι"),
    (r"K", "κ"),
    (r"L", "λ"),
    (r"M", "μ"),
    (r"N", "ν"),
    (r"O", "ο"),
    (r"P", "π"),
    (r"Q", "θ"),
    (r"R", "ρ"),
    # better handle final sigmas
    (r"S ", "ς "),
    (r"S$", "ς"),
    (r"S:", "ς:"),
    (r"S\.", "ς."),
    (r"S,", "ς,"),
    (r"S;", "ς;"),
    (r"S\'", "ς'"),
    (r"S-", "ς-"),
    (r"S_", "ς_"),
    #
    (r"S1", "σ"),
    (r"S2", "ς"),
    (r"S3", "c"),
    (r"S", "σ"),
    (r"T", "τ"),
    (r"U", "υ"),
    (r"V", "ϝ"),
    (r"W", "ω"),
    (r"X", "χ"),
    (r"Y", "ψ"),
    (r"Z", "ζ"),
    # punctuation here
    (r":", "·"),
    (r"\.", "."),
    (r",", ","),
    (r";", ";"),
    (r"\'", "’"),
    (r"-", "-"),
    (r"_", "—"),
]

# the third punctuation list wasn't working
BETA_REPLACE_PUNCT = [
    (r":", "·"),
    (r"\.", "."),
    (r",", ","),
    (r";", ";"),
    (r"\'", "’"),
    (r"-", "-"),
    (r"_", "—"),
]


class BetaCodeReplacer:
    """Replace Beta Code with Unicode.

    >>> from cltk.alphabet.grc.beta_to_unicode import BetaCodeReplacer
    >>> beta_code_replace = BetaCodeReplacer()
    >>> beta_code_str = "O(/PWS OU)=N MH\ TAU)TO\ "
    >>> beta_code_replace.replace_beta_code(beta_code_str)
    'ὅπως οὖν μὴ ταὐτὸ '
    >>> beta_code_str = "PROU+POTETAGME/NWN"
    >>> beta_code_replace.replace_beta_code(beta_code_str)
    'προϋποτεταγμένων'
    """

    def __init__(self, pattern1=None, pattern2=None, pattern3=None):
        if pattern1 is None:
            pattern1 = BETA_REPLACE_UPPER
        if pattern2 is None:
            pattern2 = BETA_REPLACE_LOWER
        if pattern3 is None:
            pattern3 = BETA_REPLACE_PUNCT
        self.pattern1 = [
            (regex.compile(beta_regex, flags=regex.VERSION1), repl)
            for (beta_regex, repl) in pattern1
        ]
        self.pattern2 = [
            (regex.compile(beta_regex, flags=regex.VERSION1), repl)
            for (beta_regex, repl) in pattern2
        ]
        self.pattern3 = [
            (regex.compile(beta_regex, flags=regex.VERSION1), repl)
            for (beta_regex, repl) in pattern3
        ]

    def replace_beta_code(self, text: str) -> str:
        """Replace method. Note: regex.subn() returns a tuple (new_string,
        number_of_subs_made).

        >>> from cltk.alphabet.grc.beta_to_unicode import BetaCodeReplacer
        >>> beta_code_replace = BetaCodeReplacer()
        >>> beta_code_str = r"*XALDAI+KH\\N"  # extra slash in ``\\N`` only here for doctest
        >>> beta_code_replace.replace_beta_code(beta_code_str)
        'Χαλδαϊκὴν'
        >>> beta_code_str = "proi+sxome/nwn"
        >>> beta_code_replace.replace_beta_code(beta_code_str)
        'προϊσχομένων'
        """

        text = text.upper().replace("-", "")
        for (pattern, repl) in self.pattern1:
            text = pattern.subn(repl, text)[0]
        for (pattern, repl) in self.pattern2:
            text = pattern.subn(repl, text)[0]
        # remove third run, if punct list not used
        for (pattern, repl) in self.pattern3:
            text = pattern.subn(repl, text)[0]
        return text
