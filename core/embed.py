# core/embed.py

from sentence_transformers import SentenceTransformer
import numpy as np

# 全局模型，只加载一次
_model = SentenceTransformer("all-MiniLM-L6-v2")


def embed(text: str) -> np.ndarray:

    vec = _model.encode(text)

    return np.array(vec)
