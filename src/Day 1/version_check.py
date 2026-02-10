import sys

print("Python Version Check")
print("---------------------")

print("Python Version:", sys.version)
print("Version Info :", sys.version_info)

if sys.version_info.major >= 3:
    print("✅ Python 3 is installed and ready to use.")
else:
    print("❌ Python 3 is not installed. Please upgrade.")
