import subprocess

scripts = [
    "scripts/bronze.py",
    "scripts/silver.py",
    "scripts/schema_check.py",
    "scripts/data_quality.py",
    "scripts/scd_type2.py",
    "scripts/gold.py"
]

print("==========")
print("DATAFLOW INC MEDALLION PIPELINE")
print("==========")

for script in scripts:
    print(f"\nRunning {script}...\n")
    result = subprocess.run(["python", script])
    
    if result.returncode != 0:
        print(f"\nError while running {script}")
        break
else:
    print("\nPipeline Completed Successfully")
