with open("index.html", "r", encoding="utf-8") as f:
    code = f.read()

# Replace Spanish language references in index.html
code = code.replace("español rioplatense e inglés ejecutivo (C1–C2)", "Español e Inglés")
code = code.replace("Español e Inglés", "Español e Inglés")
code = code.replace("español e inglés", "Español e Inglés")

# Replace English language references in index.html
code = code.replace("paired with C1–C2 English and native Rioplatense Spanish", "paired with Spanish and English")
code = code.replace("Spanish & English", "Spanish & English")
code = code.replace("English and Spanish", "Spanish and English")

# Fix any accidental newline escaping in prefillContact
code = code.replace('\\n', '\n')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(code)

print("Updated index.html language phrasing cleanly.")