import numpy as np


class ResearchState:

    def __init__(self, embedding):

        self.direction_vectors = [embedding.copy()]
        self.prev_vectors = [None]

        self.origin_vector = embedding.copy()

        self.depth_axis = 0.0

        self.pull_streak = 0
        self.history = []
        self.pool = []
        self.pool_index = 0
    def consume_batch(self, batch_size):

        start = self.pool_index
        end = start + batch_size

        batch = self.pool[start:end]

        self.pool_index = end

        return batch

    def _update_intent(self, title):

        t = title.lower()

        if any(k in t for k in ["survey", "review", "benchmark"]):
            self.depth_axis += 0.1

        if any(k in t for k in ["theorem", "proof", "analysis"]):
            self.depth_axis -= 0.1

        self.depth_axis = max(-1, min(1, self.depth_axis))

    def _closest_direction_index(self, emb):

        sims = [
            np.dot(v, emb) /
            (np.linalg.norm(v)*np.linalg.norm(emb)+1e-8)
            for v in self.direction_vectors
        ]

        return int(np.argmax(sims))

    def update_with_click(self, paper_embedding, title=""):

        idx = self._closest_direction_index(paper_embedding)

        current = self.direction_vectors[idx]
        self.prev_vectors[idx] = current.copy()

        self.direction_vectors[idx] = (
            0.85 * current + 0.15 * paper_embedding
        )

        sim = np.dot(current, paper_embedding) / (
            np.linalg.norm(current)
            * np.linalg.norm(paper_embedding) + 1e-8
        )

        if sim < 0.6 and len(self.direction_vectors) < 3:
            self.direction_vectors.append(paper_embedding.copy())
            self.prev_vectors.append(None)

        self._update_intent(title)

        self.pull_streak = 0
        self.history.append(paper_embedding)

    def update_with_pull(self):
        self.pull_streak += 1

    def get_predict_vectors(self):

        preds = []

        for v, prev in zip(self.direction_vectors, self.prev_vectors):

            if prev is None:
                preds.append(v)
                continue

            direction = v - prev

            beta = 0.5

            predict = v + beta * direction

            preds.append(
                predict/(np.linalg.norm(predict)+1e-8)
            )

        return preds
