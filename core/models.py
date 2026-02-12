# core/models.py

from dataclasses import dataclass
import numpy as np


@dataclass
class Paper:

    id: str            # ⭐ arxiv id
    title: str
    abstract: str
    source: str
    embedding: np.ndarray
    pdf_url: str       # ⭐ 下载链接
