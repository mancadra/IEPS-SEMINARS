import torch.nn.functional as F
import torch

def calculate_embedding(model, tokenizer, text):
    """
        Used for calculating embedddings for models SloBERTA crosloberta and text-embedding-ada-002
    """
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state
    attention_mask = inputs['attention_mask'].unsqueeze(-1)
    masked_embeddings = embeddings * attention_mask
    sum_embeddings = masked_embeddings.sum(dim=1)
    sum_mask = attention_mask.sum(dim=1)
    mean_pooled = sum_embeddings / sum_mask
    normalized = F.normalize(mean_pooled, p=2, dim=1)
    return normalized.squeeze().tolist()