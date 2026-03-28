import json
import glob

def clean_notebook_paths():
    notebooks = glob.glob("*.ipynb")
    for nb in notebooks:
        try:
            with open(nb, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            modified = False
            for cell in data.get('cells', []):
                if cell.get('cell_type') == 'code':
                    new_source = []
                    for line in cell.get('source', []):
                        # Force override Google Colab path mappings to local workspace mappings
                        if "/content/drive" in line and "path" in line:
                            new_source.append("path='./dataset/'\n")
                            modified = True
                        elif "test_labels.csv" in line and "labels=" in line.replace(" ", ""):
                            # Edge cases in ExtraTrees that hardcode a path string directly in read_csv
                            if "/content/drive" in line:
                                new_source.append("labels=pd.read_csv('./dataset/test_labels.csv')\n")
                                modified = True
                            else:
                                new_source.append(line)
                        else:
                            new_source.append(line)
                    cell['source'] = new_source
            
            if modified:
                with open(nb, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2)
                print(f"Fixed paths in {nb}")
                
        except Exception as e:
            print(f"Failed to fix paths in {nb}: {e}")

if __name__ == "__main__":
    clean_notebook_paths()
