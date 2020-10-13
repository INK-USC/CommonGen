import json


def generate_json(split):
    source_path = "../../dataset/final_data/commongen/commongen." + split + ".src_alpha.txt"
    target_path = "../../dataset/final_data/commongen/commongen." + split + ".tgt.txt"
    out_path = "commongen." + split + ".json"

    with open(source_path) as source, open(target_path) as target, open(out_path, "w") as output:
        source_lines = source.readlines()
        target_lines = target.readlines()

        assert len(source_lines) == len(target_lines)

        for i in range(len(source_lines)):
            source_line = source_lines[i].strip()
            target_line = target_lines[i].strip()

            out = {"src": source_line, "tgt": target_line}
            json.dump(out, output)

            if i != len(source_lines) - 1:
                output.write("\n")


generate_json("train")
generate_json("test")
generate_json("dev")