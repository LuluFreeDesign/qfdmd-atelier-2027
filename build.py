"""Construit index.html à partir de src/template.html, src/seed.json et du logo de la monnaie."""
import base64, json, pathlib
root = pathlib.Path(__file__).parent
seed = json.loads((root / "src/seed.json").read_text(encoding="utf-8"))
tpl = (root / "src/template.html").read_text(encoding="utf-8")
data = json.dumps(seed, ensure_ascii=False).replace("</", "<\\/")
coin = "data:image/png;base64," + base64.b64encode((root / "src/trimaniaque.png").read_bytes()).decode()
(root / "index.html").write_text(tpl.replace("__SEED__", data).replace("__COIN__", coin), encoding="utf-8")
print("index.html reconstruit")
