## Changelog : sill-deploy (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'amélioration de la provenance des données, l'optimisation des performances de l'API et l'ajout de fonctionnalités de configuration. Des corrections ont également été apportées pour résoudre des problèmes de blocage de contenu par la politique de sécurité du contenu (CSP) et améliorer la robustesse de l'API face aux erreurs externes.

### Évolutions fonctionnelles
- Ajout d'une table de comparaison pour afficher la provenance des sources dans la modale DSFR.
- Possibilité de configurer l'application via des fichiers, permettant une gestion plus flexible de la configuration.
- Ajout d'options pour les systèmes d'exploitation mobiles manquants et amélioration de la sécurité des types pour les systèmes d'exploitation dans l'interface web.
- Amélioration du suivi des changements de route dans l'application web pour les outils d'analyse.

### Évolutions techniques
- Optimisation de la récupération et de l'affichage des logos Wikidata et des URL associées pour améliorer les performances de l'API.
- Refactorisation du type `SoftwareData` et suppression des colonnes de contenu de la table `softwares` pour simplifier la structure de la base de données.
- Amélioration de la gestion des erreurs et du cache pour l'API Wikidata afin d'éviter les erreurs 429 (limitation de débit).
- Unification des modifications utilisateur en tant que source de données et affichage de la provenance des données.
- Mise à jour de la politique de sécurité du contenu (CSP) pour autoriser les sources d'images HTTPS arbitraires et les workers Sentry.
- Modification de la gestion des fonctionnalités du gateway.
- Correction d'une incompatibilité de type GitBeaker.
- Ajout de workflows de déploiement SILL et de synchronisation avec le dépôt upstream.

### Autres changements
- Amélioration de la documentation locale pour la configuration de la CSP.
- Correction de tests et dépendances (voir [#500](https://github.com/codegouvfr/sill-deploy/issues/500)).
- Nettoyage de code et suppression d'artefacts de provenance et de revue.
- Plusieurs mises à jour de version (build bumps).
- Réorganisation des migrations.
