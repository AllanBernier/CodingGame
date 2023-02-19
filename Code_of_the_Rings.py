# Le but du jeu est d'aider Blub à s'échapper de la forêt en lui envoyant une série d'instructions qui lui permettront d'épeler un phrase à l'aide de pierres magiques.

# Pour ce puzzle, il vous est demandé de générer une réponse d'une seule ligne. Votre rang prendra en compte votre pourcentage de réussite aux tests mais également la longueur de la ligne de réponse produite. Plus courte sera la réponse, meilleur sera votre rang.

# Votre programme reçoit en entrée une chaîne de caractères (la phrase magique que Blub doit épeler) et doit fournir en sortie une série d'instructions à destination de Blub.

# Ces instructions provoquent le déplacement de Blub et le font intéragir avec les différentes pierres.

# La forêt dans laquelle se trouve Blub obéit aux règles suivantes :
# La forêt est constituée de 30 zones distinctes.
# Blub peut se déplacer vers la gauche ou vers la droite et passer d'une zone à l'autre quand il reçoit un signe inférieur < ou supérieur >. Toutes les zones sont alignées et contiguës.
# La dernière zone est reliée à la première zone, les zones formant une boucle.
# Chaque zone contient une pierre magique sur laquelle est gravée une rune. Blub peut modifier la rune inscrite sur la pierre

# Les runes fonctionnent de la manière suivante :
# Chaque rune est représentée par une lettre de l'alphabet (A-Z) ou par un espace.
# Toutes les pierres sont initialement des runes espaces.
# Blub change la lettre d'une rune en augmentant ou diminuant la lettre quand il reçoit un signe plus + ou un signe moins -.
# La lettre après le Z est l'espace. La lettre après l'espace est le A. Les autres lettres suivent l'ordre alphabétique.
# Blub peut activer la rune se trouvant sur la pierre de la zone où il se trouve. L'activation d'une rune ajoute la lettre correspondante à la phrase qu'il épèle. Il effectue cette action quand il reçoit l'instruction point ..
# Une rune peut être activée plusieurs fois.
# Vous perdez si :
# À la fin des mouvements de Blub, la phrase écrite n'est pas la bonne.
# Blub fait plus de 4000 actions dans la forêt.
# Les instructions fournies à Blub sont incorrectes.
# Votre programme ne fournit pas d'instructions à Blub dans le temps imparti.

# Pour les CodinGamers experts, nous avons ajouté les boucles ! Vous pouvez passer cette partie tant que vous n'avez pas vraiment essayé le reste.

# Ces instructions supplémentaires sont également disponibles :
# [ : Si la rune courante est un espace, toutes les instructions jusqu'au ] correspondant sont ignorées, sinon l'exécution continue normalement.
# ] : Si la rune courante est un espace, l'exécution continue normalement, sinon les instructions à partir du [ précédent correspondant sont exécutées.
# Les boucles offrent la possibilité d'exécuter plus d'instructions tout en produisant une solution plus courte.

# Par exemple, AAAAAAAAAAAAAAAAAAAAAAAAAA (A x26) a pour solution +.......................... et aussi +>-[<.>-].

# Laissez-vous tenter par les boucles si vous en avez le courage !


s = input()
a = 1
u = ''
for c in range(len(s)):
    b=[1,ord(s[c])-63][s[c]!=' ']
    m=-[(a-b)%27,(a-b)%27-27][(a-b)%27>14]
    u+=['-'*-m,'+'*m][m>=0]+'.'
    a+=m%27
print(u)

