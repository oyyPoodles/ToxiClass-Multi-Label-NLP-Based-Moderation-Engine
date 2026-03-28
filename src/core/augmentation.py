import random

class DataAugmenter:
    """
    Simulates Advanced Data Engineering for NLP pipelines.
    Typically utilized prior to training, this class provides robust synonym replacement.
    """
    def __init__(self):
        self.synonyms = {
            "stupid": ["idiot", "dumb", "foolish", "brainless"],
            "hate": ["despise", "detest", "loathe", "abhor"],
            "kill": ["murder", "execute", "destroy", "eliminate"],
            "ugly": ["hideous", "unattractive", "gross", "repulsive"]
        }
        
    def synonym_replacement(self, text: str, n: int = 1) -> str:
        words = text.split()
        replaceable_words = [word for word in words if word.lower() in self.synonyms]
        
        if not replaceable_words:
            return text
            
        num_replacements = min(n, len(replaceable_words))
        words_to_replace = random.sample(replaceable_words, num_replacements)
        
        new_words = words.copy()
        for target in words_to_replace:
            synonym_list = self.synonyms[target.lower()]
            new_word = random.choice(synonym_list)
            # Match case roughly
            if target.isupper():
                new_word = new_word.upper()
            elif target.istitle():
                new_word = new_word.title()
                
            idx = new_words.index(target)
            new_words[idx] = new_word
            
        return " ".join(new_words)
        
    def simulate_back_translation(self, text: str) -> str:
        """
        Placeholder for back-translation via MarianMT or Google Translate API.
        e.g., English -> French -> English
        Introduces natural variance in phrasing without altering core semantic toxicity.
        """
        return text # returning identical temporarily
