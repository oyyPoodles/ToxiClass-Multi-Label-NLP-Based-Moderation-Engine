import re

class TextPreprocessor:
    def __init__(self):
        # Basic slang dictionary for normalization
        self.slang_dict = {
            "u": "you",
            "r": "are",
            "idk": "I don't know",
            "lmao": "laughing my ass off",
            "wtf": "what the fuck",
            "stfu": "shut the fuck up",
            "fk": "fuck",
            "bch": "bitch",
            "kys": "kill yourself"
        }
    
    def reduce_noise(self, text: str) -> str:
        # Lowercase everything
        text = text.lower()
        # Remove URLs
        text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)
        # Remove mentions and hashtags
        text = re.sub(r'\@\w+|\#','', text)
        # Standardize multiple punctuations (e.g. !!!! -> !)
        text = re.sub(r'([!?.]){2,}', r'\1', text)
        return text.strip()

    def normalize_slang(self, text: str) -> str:
        words = text.split()
        normalized = [self.slang_dict.get(word, word) for word in words]
        return " ".join(normalized)
    
    def process(self, text: str) -> str:
        text = self.reduce_noise(text)
        text = self.normalize_slang(text)
        return text
