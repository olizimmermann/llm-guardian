import joblib
import numpy as np
from transformers import AutoTokenizer, AutoModel
import torch
from typing import Dict, Any

class PromptClassifier:
    def __init__(self):
        self.tokenizer = None
        self.bert_model = None
        self.classifier = None
        self.load_models()
    
    def clean_up_text(self, text):
        text = str(text)
        text = text.replace('\n', ' ')
        text = text.replace('\t', ' ')
        text = text.replace('\r', ' ')
        # remove whitespaces
        text = text.strip()
        # remove multiple whitespaces
        text = ' '.join(text.split())
        text = text.lower()
        return text
    
    def load_models(self):
        """Load BERT and trained classifier models"""
        try:
            # Load BERT model for embeddings
            self.tokenizer = AutoTokenizer.from_pretrained('bert-base-multilingual-uncased')
            self.bert_model = AutoModel.from_pretrained('bert-base-multilingual-uncased')
            
            # Load trained classifier
            self.classifier = joblib.load('data/models/random_forest_model_bert_smote_1000n.joblib')
            
            print("Models loaded successfully")
        except Exception as e:
            print(f"Error loading models: {e}")
            raise
    
    def generate_embeddings(self, text: str) -> np.ndarray:
        """Generate BERT embeddings for input text"""
        inputs = self.tokenizer(
            text, 
            padding=True, 
            truncation=True, 
            max_length=512,
            return_tensors="pt" # same params as training
        )
        
        with torch.no_grad():
            outputs = self.bert_model(**inputs)
            # Use mean pooling of last hidden states
            embeddings = outputs.last_hidden_state.mean(dim=1)
        
        return embeddings.numpy()
    
    def classify(self, prompt: str) -> Dict[str, Any]:
        """Classify prompt as malicious or benign"""
        try:
            prompt = self.clean_up_text(prompt)
            # Generate embeddings
            embeddings = self.generate_embeddings(prompt)
            
            # Get prediction and probability
            prediction = self.classifier.predict(embeddings)[0]
            probability = self.classifier.predict_proba(embeddings)[0]
            
            # Calculate confidence (max probability)
            confidence = float(np.max(probability))
            
            return {
                "is_malicious": bool(prediction),
                "confidence": confidence,
                "probabilities": {
                    "benign": float(probability[0]),
                    "malicious": float(probability[1])
                }
            }
        except Exception as e:
            print(f"Classification error: {e}")
            raise
    
    def is_loaded(self) -> bool:
        """Check if models are loaded"""
        return all([
            self.tokenizer is not None,
            self.bert_model is not None,
            self.classifier is not None
        ])