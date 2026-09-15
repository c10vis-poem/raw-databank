import os, json

def build_manifest():
    manifest_path = "manifest.jsonl"
    doc_dir = "./vault" # The obsidian vault / repo folder
    
    with open(manifest_path, "w") as f:
        for root, dirs, files in os.walk(doc_dir):
            for file in files:
                if file.endswith((".md", ".jsonl", ".py", ".js")):
                    full_path = os.path.join(root, file)
                    # Create an agent-readable entry
                    with open(full_path, "r", errors="ignore") as doc:
                        first_line = doc.readline().strip()[:100]
                    
                    entry = {
                        "file": file,
                        "path": full_path,
                        "summary": first_line or "No header found."
                    }
                    f.write(json.dumps(entry) + "\n")
    print("Universal JSONL Manifest compiled successfully.")

if __name__ == "__main__":
    build_manifest()
