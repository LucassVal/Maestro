import os
import shutil

root_dir = r"."

def purge_ghosts(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            # If the folder name contains ':' or is named 'c:'
            if ":" in item or item.lower() == "c:":
                print(f"[PURGING GHOST] {item_path}")
                try:
                    shutil.rmtree(item_path)
                    print(f"[OK] Purged: {item}")
                except Exception as e:
                    print(f"[ERR] Failed to purge {item}: {e}")
            else:
                purge_ghosts(item_path)

print("--- [[GHOST PURGE]] STARTING ---")
purge_ghosts(root_dir)
print("--- [[GHOST PURGE]] FINISHED ---")
