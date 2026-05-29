## Changelog : portail (30 derniers jours, au 2 mai 2026)

### Résumé
Cette mise à jour corrige un problème de non-déterminisme dans les tests du multiplexage H2, assurant une plus grande fiabilité des tests et, par conséquent, une meilleure stabilité du proxy.

### Évolutions techniques
- Correction d'un test non déterministe dans le multiplexage H2 en utilisant un client tiny rust.  [#1](https://github.com/cloud-gouv/portail/commit/d04beda)
