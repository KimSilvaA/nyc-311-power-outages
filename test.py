# test.py in project root
import sys
print("Python path:")
for p in sys.path:
    print(f"  {p}")

print("\nCurrent directory:", sys.path[0])

try:
    import src
    print("✓ src found")
    print("src location:", src.__file__)
except:
    print("✗ src NOT found")

try:
    from src.etl import fetch_utils
    print("✓ src.etl.fetch_utils found")
except Exception as e:
    print(f"✗ src.etl.fetch_utils failed: {e}")