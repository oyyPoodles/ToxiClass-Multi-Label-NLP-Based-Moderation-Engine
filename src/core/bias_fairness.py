class BiasDetector:
    def __init__(self):
        # Specific identity terms that models often misclassify as toxic
        self.sensitive_terms = [
            "muslim", "christian", "hindu", "jew", "atheist",
            "black", "white", "asian", "hispanic",
            "gay", "straight", "lesbian", "trans", "queer",
            "woman", "man", "girl", "boy"
        ]
        
    def assess_fairness_risk(self, text: str, toxicity_score: float) -> bool:
        """
        Flags if a high toxicity score might be disproportionately influenced 
        by the presence of a marginalized identity term rather than actual toxic intent.
        """
        lower_text = text.lower()
        contains_sensitive = any(term in lower_text for term in self.sensitive_terms)
        
        # If toxic score is marginally high but sensitive term is present, 
        # it triggers a manual review or fairness warning to the admin dashboard.
        if contains_sensitive and 0.5 < toxicity_score < 0.8:
            return True
        return False
