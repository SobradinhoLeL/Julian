from test import message_to_base3, convertir_en_adn, adn_to_base3, base3_to_message

class ADN:
    def __init__(self):
        pass

    def text_to_adn(self):
        return convertir_en_adn(message_to_base3(self))

    def adn_to_text(self):
        return base3_to_message(adn_to_base3(self))