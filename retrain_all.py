import os
import subprocess
import glob
import time

def retrain_all_notebooks():
    notebooks = glob.glob("*.ipynb")
    print(f"Found {len(notebooks)} notebooks to retrain: {notebooks}")
    
    # Optional: Order them so smaller ones run first
    traditional = [n for n in notebooks if "LSTM" not in n]
    deep_learning = [n for n in notebooks if "LSTM" in n]
    ordered_notebooks = traditional + deep_learning
    
    for nb in ordered_notebooks:
        print(f"\n[{time.strftime('%X')}] Starting execution: {nb}")
        try:
            # Execute the notebook strictly in place
            result = subprocess.run(
                [
                    "jupyter", "nbconvert", 
                    "--to", "notebook", 
                    "--execute", 
                    "--inplace", 
                    "--ExecutePreprocessor.timeout=7200", # 2 hour timeout per notebook
                    nb
                ],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print(f"✅ Successfully retrained: {nb}")
            else:
                print(f"❌ Error in {nb}:")
                # Print the last few lines of the error
                print('\n'.join(result.stderr.split('\n')[-20:]))
                
        except FileNotFoundError:
            print("❌ Jupyter is not installed or not in PATH. Please install: pip install jupyter")
            break
        except Exception as e:
            print(f"❌ Failed to run {nb}: {e}")

if __name__ == "__main__":
    print("Initiating Master Retraining Protocol...")
    retrain_all_notebooks()
    print("Retraining sequence complete.")
