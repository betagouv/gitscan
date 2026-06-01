## Changelog : portail (30 derniers jours, au 2 mai 2026)

### Résumé
Cette mise à jour corrige un problème de non-déterminisme dans les tests du multiplexage H2, assurant ainsi une meilleure fiabilité des tests et, par conséquent, une plus grande stabilité du proxy.

### Évolutions techniques
- Correction d'un test non déterministe dans le multiplexage H2 en utilisant un client tiny rust. [#1](https://github.com/cloud-gouv/portail/commit/d04beda)
