from core.rank import rank_papers


def generate_probes(state, input_text):

    probes = [input_text]
    probes.append(input_text + " survey")
    probes.append(input_text + " framework")

    return probes



def run_pipeline(state, fetch_manager, input_text):

    probes = generate_probes(state, input_text)

    candidates = fetch_manager.search_all(probes)

    ranked = rank_papers(state, candidates)

    return ranked[:10]


POOL_TARGET = 50
BATCH_SIZE = 10


def run_pipeline(state, fetch_manager, input_text):

    if len(state.pool) - state.pool_index < BATCH_SIZE:

        probes = generate_probes(state, input_text)

        candidates = fetch_manager.search_all(probes)

        ranked = rank_papers(state, candidates)

        state.pool.extend(ranked)

    return state.consume_batch(BATCH_SIZE)
