Distribution:
(array([0, 1]), array([268801,  81213]))
in percentage: (77.5, 22.5)

Cleaning and removing of duplicates:
```python
text = str(text)
text = text.replace('\n', ' ')
text = text.replace('\t', ' ')
text = text.replace('\r', ' ')
text = text.strip()
text = ' '.join(text.split())
text = text.lower()
```

## MiniLM
Embeddings shape: (437518, 384)

### LogisticRegression(random_state=42)
Accuracy: 0.7993
Precision: 0.6852
Recall: 0.2495
F1-Score: 0.3658

#### SMOTE
Accuracy: 0.7024
Precision: 0.4181
Recall: 0.7210
F1-Score: 0.5293

### XGBClassifier(random_state=42)
Accuracy: 0.8332
Precision: 0.7519
Recall: 0.4198
F1-Score: 0.5388

#### SMOTE
Accuracy: 0.7731
Precision: 0.5071
Recall: 0.7886
F1-Score: 0.6173

### RandomForestClassifier(random_state=42)
Accuracy: 0.8553
Precision: 0.8233
Recall: 0.4789
F1-Score: 0.6056

#### SMOTE
Accuracy: 0.8447
Precision: 0.6465
Recall: 0.7300
F1-Score: 0.6857

### Undersampled
Accuracy: 0.7917
Precision: 0.5324
Recall: 0.8394
F1-Score: 0.6516


------


## BERT
Embeddings shape: (437518, 768)

### LogisticRegression(random_state=42)
Accuracy: 0.8046
Precision: 0.6977
Recall: 0.2782
F1-Score: 0.3978

#### SMOTE
Accuracy: 0.7090
Precision: 0.4274
Recall: 0.7487
F1-Score: 0.5441

### XGBClassifier(random_state=42)
Accuracy: 0.8322
Precision: 0.7464
Recall: 0.4191
F1-Score: 0.5368

#### SMOTE
Accuracy: 0.7776
Precision: 0.5132
Recall: 0.8040
F1-Score: 0.6265

### RandomForestClassifier(random_state=42)
Accuracy: 0.8539
Precision: 0.8303
Recall: 0.4656
F1-Score: 0.5966

#### SMOTE
Accuracy: 0.8487
Precision: 0.6528
Recall: 0.7430
F1-Score: 0.6950

### SMOTE n_estimators=100, class_weight='balanced'
Accuracy: 0.8481
Precision: 0.6520
Recall: 0.7408
F1-Score: 0.6936

### SMOTE n_estimators=500, class_weight='balanced'
Accuracy: 0.8512
Precision: 0.6575
Recall: 0.7485
F1-Score: 0.7000

### SMOTE n_estimators=1000, class_weight='balanced'
Accuracy: 0.8510
Precision: 0.6566
Recall: 0.7499
F1-Score: 0.7002