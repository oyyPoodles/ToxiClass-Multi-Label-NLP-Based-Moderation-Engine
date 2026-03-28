from transformers import pipeline
import logging

logger = logging.getLogger("ToxiShield")

class TransformerInference:
    def __init__(self):
        # We initialize zero-shot to simulate fine-tuned toxic multiclass outputs
        # In a real environment, you run model="your-name/finetuned-bert-toxicity"
        logger.info("Loading DistilBERT base pipeline...")
        self.english_pipeline = pipeline(
            "text-classification", 
            model="distilbert-base-uncased", 
            return_all_scores=True
        )
        
        logger.info("Loading mBERT/XLM-R multilingual pipeline...")
        self.multilingual_pipeline = pipeline(
            "text-classification", 
            model="xlm-roberta-base", 
            return_all_scores=True
        )

        self.labels = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]
        
    def is_multilingual(self, text: str) -> bool:
        """Primitive lang check: assume non-ascii indicates multilingual/hindi/tamil."""
        return not text.isascii()

    def predict(self, text: str, context: str = ""):
        # Construct context-aware input
        if context:
            full_input = context + " [SEP] " + text
        else:
            full_input = text
            
        # Choose model dynamically based on text layout (Multilingual or Native)
        pipe = self.multilingual_pipeline if self.is_multilingual(text) else self.english_pipeline
        
        # Note: Raw base models won't have the 6 labels configured without fine-tuning weights.
        # This wrapper simulates the extraction for the API deployment layer.
        try:
            raw_scores = pipe(full_input)[0] 
            
            # Map dummy output to actual classes since we're using raw un-finetuned bases strictly for architecture scaffold
            # This would map 1:1 on a fine-tuned Roberta model.
            mapped_probabilities = {
                label: float(raw_scores[i % len(raw_scores)]['score']) for i, label in enumerate(self.labels)
            }
            return mapped_probabilities
            
        except Exception as e:
            logger.error(f"Transformer Inference Error: {e}")
            return {label: 0.0 for label in self.labels}
