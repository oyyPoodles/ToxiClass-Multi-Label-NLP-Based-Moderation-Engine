from lime.lime_text import LimeTextExplainer
import numpy as np

class XAIExplainer:
    def __init__(self, target_classifier_fn):
        """
        target_classifier_fn should take a list of strings and return a 2D numpy array 
        where probabilities for (Non-Toxic, Toxic) are mapped.
        """
        # We focus explicitly on explaining the "toxic" threshold
        self.explainer = LimeTextExplainer(class_names=["Non-Toxic", "Toxic"])
        self.classifier_fn = target_classifier_fn
        
    def explain_instance(self, text: str, num_features: int = 5):
        try:
            # We request LIME to randomly perturb the text and pass it to our Transformer
            exp = self.explainer.explain_instance(
                text, 
                self.classifier_fn, 
                num_features=num_features
            )
            
            # Extract word-weight tuples
            # Positive weight -> indicates Toxicity
            # Negative weight -> indicates Non-Toxicity
            explanation_dict = {word: float(weight) for word, weight in exp.as_list()}
            return explanation_dict
            
        except Exception as e:
            # If the pipeline errors during LIME perturbation
            return {"error_generating_explanation": 0.0}
