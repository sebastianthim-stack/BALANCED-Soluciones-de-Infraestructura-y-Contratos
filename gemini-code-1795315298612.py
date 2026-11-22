with open("competitive_positioning_matrix.md", "r", encoding="utf-8") as f:
    md = f.read()

md = md.replace("Rioplatense Spanish", "Spanish")
md = md.replace("C1–C2 English", "English")
md = md.replace("C1/C2 English", "English")

with open("competitive_positioning_matrix.md", "w", encoding="utf-8") as f:
    f.write(md)

print("Updated competitive_positioning_matrix.md language phrasing cleanly.")