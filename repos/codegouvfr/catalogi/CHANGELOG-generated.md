## Changelog : catalogi (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'enrichissement des données des logiciels, notamment via Wikidata, et sur l'amélioration de la provenance des informations affichées. Des optimisations de performance ont également été apportées à l'API, et la configuration de l'application a été revue.

### Évolutions fonctionnelles
- Amélioration de l'affichage de la provenance des données dans la modale DSFR, avec une présentation sous forme de tableau comparatif [#500](https://github.com/codegouvfr/catalogi/issues/500).
- Ajout d'options pour les systèmes d'exploitation mobiles dans l'interface web.
- Possibilité de configurer les sources de données via des fichiers.
- Amélioration de la gestion des sources d'informations utilisateur.

### Évolutions techniques
- Optimisation de la récupération et de l'affichage des logos et des données Wikidata, réduisant les risques de limitation de débit (429 errors).
- Refactorisation du type `SoftwareData` dans l'API pour simplifier la structure des données.
- Unification de la gestion des modifications utilisateur en tant que source de données.
- Amélioration de la gestion de la configuration des fonctionnalités via le gateway.
- Mise à jour de la gestion des URL d'images Wikidata pour utiliser `Special:FilePath`.
- Amélioration de la robustesse de la communication avec le gateway Wikidata.
- Correction d'un problème de typage dans les dépendances de test.
- Mise à jour de la gestion du Content Security Policy (CSP) pour l'environnement de développement.

### Autres changements
- Nettoyage des artefacts de provenance et de revue.
- Mise à jour des tests Wikidata pour tenir compte des changements récents.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Mises à jour de version (build bumps).
