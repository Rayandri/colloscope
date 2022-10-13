	
with open("kolle2.md","w") as fichier2:
	with open("kolles.txt","r") as fichier:
		lignes = fichier.readlines()
		cpt2 = 0
		for ligne in lignes:
			cpt2 +=1
			cpt = 0
			ligne_edit = ""
			for char in ligne:
				
				if char == "|": cpt +=1
				
				if cpt == 2: 
					continue
				else: 
					ligne_edit += char 
			print(ligne_edit) 
			fichier2.write(ligne_edit)
		
