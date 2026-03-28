from .preprocessing import TextPreprocessor
from .context_buffer import ContextBuffer
from .xai_explainer import XAIExplainer
from .bias_fairness import BiasDetector
from ..models.transformer import TransformerInference

import time

class HybridToxicityEngine:
    def __init__(self):
        self.preprocessor = TextPreprocessor()
        self.context_buffer = ContextBuffer()
        self.bias_detector = BiasDetector()
        
        self.transformer = TransformerInference()
        
        # Hardcoded rule-based Apriori triggers from the dataset mining
        self.apriori_rules = {
            "kill you": "threat",
            "i will kill": "threat",
            "die": "threat",
            "fucking bitch": "obscene",
            "piece of shit": "insult"
        }
        
    def rule_based_override(self, text: str):
        for rule, category in self.apriori_rules.items():
            if rule in text.lower():
                return category
        return None
        
    def analyze(self, text: str, user_id: str, history=None):
        start_ms = time.time()
        
        # 1. Context Logging
        self.context_buffer.add_message(user_id, text)
        context = self.context_buffer.get_context(user_id)
        
        # 2. Preprocessing
        clean_text = self.preprocessor.process(text)
        
        # 3. Sarcasm Check (Heuristic)
        is_sarcastic = self.context_buffer.detect_sarcasm_pattern(text, user_id)
        
        # 4. Rule-based Override (Apriori)
        rule_category = self.rule_based_override(clean_text)
        
        # 5. Transformer Inference (BERT / mBERT)
        preds = self.transformer.predict(clean_text, context)
        
        # 6. Apply Rules if present
        if rule_category:
            preds[rule_category] = 0.99
            
        # If sarcastic, reduce severity temporarily for safety review
        if is_sarcastic:
            preds = {k: v * 0.7 for k, v in preds.items()}
            
        max_category = max(preds, key=preds.get)
        max_score = preds[max_category]
        is_toxic = max_score > 0.6
        
        # 7. Fairness Analysis
        bias_flag = self.bias_detector.assess_fairness_risk(clean_text, max_score)
        
        # 8. Action routing
        if is_toxic and not bias_flag:
            action = "delete" if max_score > 0.85 else "flag_for_review"
        else:
            action = "allow"
            
        if bias_flag:
            action = "bias_review_required"
            
        process_time = (time.time() - start_ms) * 1000
        
        return {
            "is_toxic": is_toxic,
            "confidence": max_score,
            "categories": preds,
            "explainability": {}, # XAI computationally expensive, skipped unless explicitly requested
            "action": action
        }
