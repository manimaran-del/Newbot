import subprocess

processes = [
    subprocess.Popen(["python3", "-m", "Toxic"]),
    subprocess.Popen(["python3", "rank.py"]),
    subprocess.Popen(["python3", "word.py"])
]

for p in processes:
    p.wait()
