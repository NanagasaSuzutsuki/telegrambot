import numpy as np


def cosine(a,b):
    return np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b)+1e-8)


def rank_papers(state,papers):

    predict_vecs = state.get_predict_vectors()

    w_origin = 0.2
    w_div = 0.4

    for p in papers:

        sim = max(
            cosine(pred,p.embedding)
            for pred in predict_vecs
        )

        origin_sim = cosine(state.origin_vector,p.embedding)

        # ⭐ intent influence
        title = p.title.lower()

        intent_bonus = 0

        if state.depth_axis > 0:
            if "survey" in title or "review" in title:
                intent_bonus += 0.2

        if state.depth_axis < 0:
            if "analysis" in title or "theorem" in title:
                intent_bonus += 0.2

        explore = min(1.0,state.pull_streak*0.3)

        p._score = (
            sim
            + w_origin*origin_sim
            + intent_bonus
            + explore*(1-sim)
        )

    papers.sort(key=lambda x:x._score,reverse=True)

    selected=[]

    while papers and len(selected)<10:

        best=None
        best_score=-1e9

        for p in papers:

            redundancy=0

            if selected:
                redundancy=max(
                    cosine(p.embedding,s.embedding)
                    for s in selected
                )

            score=p._score-w_div*redundancy

            if score>best_score:
                best_score=score
                best=p

        selected.append(best)
        papers.remove(best)

    return selected
