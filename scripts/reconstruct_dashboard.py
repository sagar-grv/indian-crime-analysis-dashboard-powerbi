from pathlib import Path
import base64, hashlib, json, lzma, sys

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "artifact_manifest.json").read_text())
parts = sorted((root / "artifact_parts").glob("part-*.b64"))
expected = manifest["chunk_count"]

if len(parts) != expected:
    print(f"Waiting for all parts: found {len(parts)} of {expected}")
    sys.exit(0)

encoded = "".join(p.read_text().strip() for p in parts)
compressed = base64.b64decode(encoded, validate=True)
data = lzma.decompress(compressed)
sha = hashlib.sha256(data).hexdigest()

if sha != manifest["original_sha256"]:
    raise SystemExit(f"SHA-256 mismatch: {sha}")

out = root / manifest["output_path"]
out.parent.mkdir(parents=True, exist_ok=True)
out.write_bytes(data)
print(f"Reconstructed {out} ({len(data)} bytes, SHA-256 {sha})")
