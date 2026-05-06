## Changelog : find (30 derniers jours, au 5 mai 2026)

### Résumé
Ce mois-ci, le projet find a subi une phase importante de nettoyage et de simplification. Plusieurs fonctionnalités expérimentales, comme la recherche par embedding et l'application d'évaluation, ont été supprimées pour se concentrer sur les fonctionnalités principales et améliorer la stabilité. Des mises à jour de dépendances ont également été effectuées, incluant des correctifs de sécurité importants.

### Évolutions fonctionnelles
- Correction du type de valeur dans la recherche [#68](https://github.com/suitenumerique/find/issues/68).

### Évolutions techniques
- Suppression du code mort identifié par l'outil Vulture.
- Suppression de la recherche par embedding et du système BM25, maintenant uniquement BM25 est utilisé.
- Suppression de l'application d'évaluation.
- Suppression du service Dockerize non utilisé.
- Suppression des dépendances inutilisées `url-normalize` et déplacement de `factory_boy` vers les dépendances de développement.
- Mise à jour de Redis vers la version 6.
- Mise à jour de Django vers la version 6 [#112](https://github.com/suitenumerique/find/issues/112).
- Autorisation des constantes en majuscules dans les paramètres Django pour Pylint.
- Ajout de hooks pre-commit pour améliorer la qualité du code.

### Autres changements
- Correction de fautes de frappe dans la documentation.
- Plusieurs mises à jour de dépendances ont été appliquées, incluant des correctifs de sécurité pour Django, Requests, PyJWT, pytest, langchain-text-splitters et d'autres. Ces mises à jour sont gérées par Renovate Bot et ne sont pas listées individuellement ici.
- Séparation des PR de mise à jour des dépendances Python pour une meilleure gestion.
- Épinglage des dépendances pour une meilleure stabilité [#75](https://github.com/suitenumerique/find/issues/75).
