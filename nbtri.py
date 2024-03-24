import sys

# cette  application compte le nombres de (vrais) triangles tracés
# dans une figure donnée.
# Elle prend en compte le fichier:
#               graphe.txt
# qui contient des lignes de la forme ABCD pour signifier
# que les segment [AB] [AC] et [AD] sont tracés
# et éventuellement
#               alignement.txt
# qui contient des lignes de la forme ABCD pour signifier
# que A,B,C et D sont alignés.

segment = []


def lignes():
    """renvoie les lignes de graphe.txt"""
    try:
        with open("graphe.txt") as graphe:
            lignes = graphe.read().split()
            return lignes
    except:
        print("Le fichier graphe.txt est introuvable")
        sys.exit()


def les_alignements():
    """renvoie les lignes de alignement.txt"""
    try:
        with open("alignement.txt") as alignement:
            lignes = alignement.read().split()
            return lignes
    except:
        return []


def les_segments():
    """renvoie tous les segments -set- construits"""
    segments = []
    l = [x for x in lignes() if len(x) > 0]
    for ligne in l:
        if len(ligne) < 2:
            print("problème dans graphe.txt")
            sys.exit()
        else:
            for x in ligne[1:]:
                segments.append(set(ligne[0]).union(set(x)))
    return segments


def les_points(l):
    """renvoie tous les points apparraissant dans une liste de segments"""
    points = set()
    for x in l:
        for y in x:
            points.add(y)
    return points


l = les_segments()
l2 = ["[" + "".join(list(x)) + "]" for x in sorted(l)]
p = les_points(l)
a = les_alignements()
print(a)
print("Il y a {} points : {}".format(len(p), ",".join(sorted(p))))
print("et {} segments : {}".format(len(l), ",".join(l2)))

plats = set()
if len(a) != 0:
    print("Alignements :")
    for d in a:
        print(d)
        if len(set(d)) > 2:
            trois = [frozenset([x, y, z]) for x in set(d) for y in set(d) for z in set(d) if len(set([x, y, z])) == 3]
            for t in trois:
                plats.add(t)
##    for p in plats:
##        print(p)

# création de tous les ensemnbles de 3 points
triplets = [[x, y, z] for x in p for y in p for z in p]
trio = []
for t in triplets:
    tt = set(t)
    if len(tt) == 3:
        trio.append(tt)

triangles = []

for t in trio:
    tl = list(t)
    cotes = [set([tl[0], tl[1]]), set([tl[0], tl[2]]), set([tl[1], tl[2]])]
    if cotes[0] in l and cotes[1] in l and cotes[2] in l and t not in triangles:
        triangles.append(t)

# triangles contient la liste des ensembles de points formant triangles constructibles
# reste à supprimer les plats


resultats = [t for t in triangles if t not in plats]
print("Nombres de vrais triangles :", len(resultats))
for t in resultats:
    print("".join(sorted(list(t))), end=" ")