import json

with open('report.jsonl') as src:
    ps = [json.loads(line) for line in src]

with open('PRESUMM.run', 'w') as out:
    for p in ps:
        for sentence_id, score in enumerate(p['pred_ids']):
            out.write(f"{p['opinion_id']}\tQ0\ts{sentence_id}\t0\t{score}\tPRESUMM\n")
