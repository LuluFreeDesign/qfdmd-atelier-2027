"""Construit index.html à partir de src/template.html et src/seed.json."""
import json, pathlib
root = pathlib.Path(__file__).parent
seed = json.loads((root / "src/seed.json").read_text(encoding="utf-8"))
tpl = (root / "src/template.html").read_text(encoding="utf-8")
data = json.dumps(seed, ensure_ascii=False).replace("</", "<\\/")
(root / "index.html").write_text(tpl.replace("__SEED__", data), encoding="utf-8")
print("index.html reconstruit")
