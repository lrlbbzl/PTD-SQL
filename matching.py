import json

def find_overlap_indices(a, b, shots):
    def overlap_count(tokens1, tokens2):
        return len(set(tokens1).intersection(set(tokens2)))
    overlap_scores = [overlap_count(sentence_tokens, b) for sentence_tokens in a]
    top_indices = sorted(range(len(overlap_scores)), key=lambda i: overlap_scores[i], reverse=True)[:shots]

    return top_indices

def auto_prompting(test_data, train_data, shots=4, type='count'):
    questions = [x['question'] for x in train_data]
    question_tokens = [xx.split(' ') for xx in questions]
    selected_idx = []
    for i, x in enumerate(test_data):
        temp = find_overlap_indices(question_tokens, x['question'].split(' '), shots)
        selected_idx.append(temp)
    matching_list = {
        test_data[i]['question'] : [train_data[idx]['question'] for idx in selected_idx[i]] for i in range(len(selected_idx))
    }
    return matching_list


# test_data, train_data = json.load(open('./data/test/complex/complex.json', 'r')), json.load(open('./data/train/complex/true_samples.json', 'r'))
# matching_list = auto_prompting(test_data, train_data)