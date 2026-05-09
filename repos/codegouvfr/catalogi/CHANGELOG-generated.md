## Changelog : catalogi (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'amélioration de la provenance des données, la robustesse de l'API et l'expérience utilisateur. Des optimisations ont été apportées pour gérer plus efficacement les données Wikidata et améliorer la performance de l'application, notamment en réduisant les erreurs liées aux requêtes. L'interface web a également été améliorée avec des options supplémentaires et une meilleure gestion de la configuration.

### Évolutions fonctionnelles
- Amélioration de l'affichage de la provenance des données dans l'interface web, avec une présentation comparative en tableau dans la modale DSFR.
- Ajout d'options pour les systèmes d'exploitation mobiles dans l'interface web. [#500](https://github.com/codegouvfr/catalogi/issues/500)
- Possibilité de configurer les sources via des fichiers.
- Gestion des modifications utilisateur unifiées comme une source de données, permettant de suivre la provenance des données.
- Affichage des URLs des images Wikidata directement depuis Special:FilePath.

### Évolutions techniques
- Optimisation de la récupération des données Wikidata et des URLs des logos pour améliorer la performance de l'API.
- Refactorisation du type `SoftwareData` et suppression des colonnes de contenu de la table `softwares`.
- Amélioration de la robustesse de la passerelle Wikidata et mise en cache des autocomplétions pour éviter les erreurs 429.
- Unification du traitement des modifications utilisateur en tant que source de données.
- Mise à jour de la configuration de Content Security Policy (CSP) pour autoriser les sources d'images HTTPS arbitraires et les workers Sentry.
- Amélioration de la gestion de la configuration via des fichiers.
- Correction d'un problème de type dans `gitbeaker`.

### Autres changements
- Amélioration de la documentation locale pour la configuration de CSP.
- Nettoyage des artefacts de provenance et de revue.
- Mise à jour de la version de l'application.
- Correction de tests et dépendances.
- Ajout de la gestion des changements de route SPA pour le tracking analytics.
