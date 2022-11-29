base = int(input('demander le nombre de personne convier à la table'))
Bases = 4
quantitédefromage = 800
quantitédeau = 2
quantitédail = 2
quantitédepain = 400
grammedefrommage= quantitédefromage * base / Bases
litredeau= quantitédeau * base / Bases
grammedail= quantitédail * base / Bases
grammedepain= quantitédepain * base / Bases
print(f'pour faire une fondue fribourgeoise pour {base} il nous faut \n:  {grammedefrommage} gramme de fromage,\n {litredeau} de litre deau,\n {grammedail} de gousse dail \n et {grammedepain} gramme de pain')
