"""Named entity recognition (NER)."""

import importlib.machinery
import os

from cltk.tokenize.word import WordTokenizer
from nltk.tokenize.punkt import PunktLanguageVars

from cltkv1.data.fetch import FetchCorpus
from cltkv1.utils import CLTK_DATA_DIR

__author__ = ["Natasha Voake <natashavoake@gmail.com>"]

NER_DICT = {
    "grc": os.path.join(
        CLTK_DATA_DIR, "/greek/model/greek_models_cltk/ner/proper_names.txt"
    ),
    "lat": os.path.join(
        CLTK_DATA_DIR + "/lat/model/lat_models_cltk/ner/proper_names.txt"
    ),
}


class NamedEntityReplacer(object):
    def __init__(self):

        self.entities = self._load_necessary_data()

    def _load_necessary_data(self):
        rel_path = os.path.join(
            CLTK_DATA_DIR, "french", "text", "french_data_cltk", "named_entities_fr.py"
        )
        path = os.path.expanduser(rel_path)
        # logger.info('Loading entries. This may take a minute.')
        loader = importlib.machinery.SourceFileLoader("entities", path)
        module = loader.load_module()
        entities = module.entities
        return entities

    def tag_ner_fr(self, input_text, output_type=list):
        """tags named entities in a string and outputs a list of tuples in the following format:
        (name, "entity", kind_of_entity)"""

        entities = self.entities

        for entity in entities:
            (name, kind) = entity

        word_tokenizer = WordTokenizer("french")
        tokenized_text = word_tokenizer.tokenize(input_text)
        ner_tuple_list = []

        match = False
        for word in tokenized_text:
            for name, kind in entities:
                if word == name:
                    named_things = [(name, "entity", kind)]
                    ner_tuple_list.append(named_things)
                    match = True
                    break
            else:
                ner_tuple_list.append((word,))
        return ner_tuple_list


def _check_latest_data(lang):
    """Check for presence of proper names dir, clone if not."""

    assert lang in NER_DICT.keys(), "Invalid language. Choose from: {}".format(
        ", ".join(NER_DICT.keys())
    )

    ner_file_path = os.path.expanduser(NER_DICT[lang])

    if not os.path.isfile(ner_file_path):
        corpus_importer = FetchCorpus(lang)
        corpus_importer.import_corpus("{}_models_cltk".format(lang))


def tag_ner(lang, input_text, output_type=list):
    """Run NER for chosen language.

    >>> from cltkv1.ner.ner import tag_ner
    >>> from cltkv1.utils.example_texts import get_example_text
    >>> tag_ner(lang="lat", input_text=get_example_text(iso_code="lat"))
    """

    _check_latest_data(lang)

    assert lang in NER_DICT.keys(), "Invalid language. Choose from: {}".format(
        ", ".join(NER_DICT.keys())
    )
    types = [str, list]
    assert type(input_text) in types, "Input must be: {}.".format(", ".join(types))
    assert output_type in types, "Output must be a {}.".format(", ".join(types))

    if type(input_text) == str:
        punkt = PunktLanguageVars()
        tokens = punkt.word_tokenize(input_text)
        new_tokens = []
        for word in tokens:
            if word.endswith("."):
                new_tokens.append(word[:-1])
                new_tokens.append(".")
            else:
                new_tokens.append(word)
        input_text = new_tokens

    ner_file_path = os.path.expanduser(NER_DICT[lang])
    with open(ner_file_path) as file_open:
        ner_str = file_open.read()
    ner_list = ner_str.split("\n")

    ner_tuple_list = []
    for count, word_token in enumerate(input_text):
        match = False
        for ner_word in ner_list:
            # the replacer slows things down, but is necessary
            if word_token == ner_word:
                ner_tuple = (word_token, "Entity")
                ner_tuple_list.append(ner_tuple)
                match = True
                break
        if not match:
            ner_tuple_list.append((word_token,))

    if output_type is str:
        string = ""
        for tup in ner_tuple_list:
            start_space = " "
            final_space = ""
            # this is some mediocre string reconstitution
            # maybe not worth the effort
            if tup[0] in [",", ".", ";", ":", "?", "!"]:
                start_space = ""
            if len(tup) == 2:
                string += start_space + tup[0] + "/" + tup[1] + final_space
            else:
                string += start_space + tup[0] + final_space
        return string

    return ner_tuple_list
