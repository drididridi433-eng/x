phrase=input("donner une phrase").strip().upper()
# strip supp les espaces au debut et a la fin de chaine
# split decoupe la chaine
print("caracteres (avec espaces):",len(phrase))
print("caracteres (sans esoaces):",len(phrase.replace(" ","")))
ch=phrase.split()
print("nombre de mots: ",len(ch))


