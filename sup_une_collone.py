def fonction():
	with open("kolle2.md", "w") as fichier2:
		with open("kolles.txt", "r") as fichier:
			lignes = fichier.readlines()
			cpt2 = 0
			cpt_fin_doc = 0
			print(len(lignes))
			for ligne in lignes:
				cpt_fin_doc += 1
				if cpt_fin_doc == 3:
					fichier2.write(ligne)
					continue
				#if cpt_fin_doc == 36: break  
				cpt2 += 1
				cpt = 0
				ligne_edit = ""
				for char in ligne:

					if char == "|": cpt += 1

					if cpt == 2:
						continue
					else:
						ligne_edit += char
				#print(ligne_edit) 
				fichier2.write(ligne_edit)


def copier():
	with open("kolle2.md", "r") as fichier2:
		with open("kolles.txt", "w") as fichier:
			for i in fichier2.readlines():
				fichier.write(i)


def main(nb):
	for i in range(nb):
		fonction()
		copier()


