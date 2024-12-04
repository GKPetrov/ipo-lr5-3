file=open("text.txt")
text=file.read()
print(f"число слов {len(text.split())}")
file.close()
