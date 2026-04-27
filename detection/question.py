import re

def is_question(text: str) -> bool:
    text = text.lower().strip()
    if "?" in text:
        return True
        
    triggers = [r"\bwhat\b", r"\bhow\b", r"\bwhy\b", r"\btell\b", r"\bdescribe\b", r"\bexplain\b", r"\bcan you\b", r"\bcould you\b", r"\bwould you\b"]
    
    return any(re.search(t, text) for t in triggers)
