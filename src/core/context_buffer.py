from typing import List, Dict
import time

class ContextBuffer:
    def __init__(self, max_history: int = 5):
        self.max_history = max_history
        # In a real database this would be Redis/Memcached.
        # Structure: { "user_id": [{"text": str, "timestamp": float}] }
        self._history_store: Dict[str, List[Dict]] = {}
        
    def add_message(self, user_id: str, message: str) -> None:
        if user_id not in self._history_store:
            self._history_store[user_id] = []
            
        self._history_store[user_id].append({
            "text": message,
            "timestamp": time.time()
        })
        
        # Prune to max_history limits
        if len(self._history_store[user_id]) > self.max_history:
            self._history_store[user_id] = self._history_store[user_id][-self.max_history:]
            
    def get_context(self, user_id: str) -> str:
        """Returns the conversation history concatenated for context-aware modeling."""
        if user_id not in self._history_store:
            return ""
        
        messages = [entry["text"] for entry in self._history_store[user_id]]
        # Context delimiter separates messages so the Transformer can identify turn boundaries.
        return " [SEP] ".join(messages)

    def detect_sarcasm_pattern(self, current_msg: str, user_id: str) -> bool:
        """
        Heuristic check: if the user's previous message was highly positive 
        and the current message is a short dismissive token, flag potential sarcasm.
        """
        history = self._history_store.get(user_id, [])
        if not history:
            return False
            
        sarcasm_cues = ["yeah right", "sure", "great job", "whatever", "wow"]
        if any(cue in current_msg.lower() for cue in sarcasm_cues) and len(history) > 0:
            return True
            
        return False
