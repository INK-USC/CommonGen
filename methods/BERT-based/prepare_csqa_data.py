import json


def generate_json(split):
    source_path = "../../evaluation/csqa/csqa." + split + ".qac.src"
    # target_path = "../../dataset/final_data/commongen/commongen." + split + ".tgt.txt"
    out_path = "csqa." + split + ".json"

    with open(source_path) as source, open(out_path, "w") as output:
        source_lines = source.readlines()

        for i in range(len(source_lines)):
            source_line = source_lines[i].strip()

            out = {"src": source_line, "tgt": ""}
            json.dump(out, output)

            if i != len(source_lines) - 1:
                output.write("\n")


generate_json("train")
generate_json("dev")