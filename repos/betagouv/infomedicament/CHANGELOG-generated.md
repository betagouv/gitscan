## Changelog : infomedicament (30 derniers jours, au 17 juin 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration significative de la recherche de médicaments, notamment en intégrant des synonymes et en affinant les résultats. Des améliorations ont également été apportées à l'affichage des informations sur les médicaments, en particulier pour les données pédiatriques et les notices. Enfin, des optimisations de performance ont été réalisées pour accélérer le chargement des pages et des données.

### Évolutions fonctionnelles
- **Recherche améliorée :** La recherche prend désormais en compte des synonymes pour les termes de recherche [#194](https://github.com/betagouv/infomedicament/pull/194).
- **Suggestions de recherche :** Des suggestions "Vouliez-vous dire" sont maintenant affichées pour les requêtes avec synonymes.
- **Affichage des spécialités :** Amélioration du classement et de l'autocomplétion des spécialités dans la recherche.
- **Informations pédiatriques :** Affichage plus précis des contre-indications pour les données pédiatriques.
- **Nouvelle page médicament :** Refonte de la page d'information d'un médicament [#222](https://github.com/betagouv/infomedicament/pull/222).
- **Date de dernière mise à jour :** Ajout d'une indication de la date de dernière mise à jour des données.
- **Notices :** Intégration d'une recherche sémantique dans les notices, utilisant un modèle de langage pour répondre aux questions et mettre en évidence les informations pertinentes.
- **Pages de listes :** Redirection des pages racines des listes vers la première lettre.
- **Cartes spécialités :** Affichage des indications sur les nouvelles cartes spécialités.

### Évolutions techniques
- **Performance :** Pré-rendu des 500 médicaments les plus consultés lors de la construction du site pour améliorer la vitesse de chargement.
- **Performance :** Déplacement de la récupération des données vers des composants serveur pour optimiser les performances.
- **Base de données :** Optimisation de la population de la table `specMetadataTable` pour éviter les erreurs de mémoire insuffisante.
- **Architecture :** Refactorisation du code pour utiliser Matomo en mode sans cookies et suppression du consentement banner.
- **Tests :** Ajout de tests unitaires et d'intégration pour la recherche et les nouvelles fonctionnalités.
- **Infrastructure :** Amélioration de la configuration pour les environnements de revue.

### Autres changements
- **Documentation :** Ajout de commentaires et de TODOs pour faciliter la maintenance et les futures améliorations.
- **Nettoyage du code :** Suppression de code obsolète (Hotjar) et simplification de certains composants.
- **Configuration :** Mise à jour de la configuration pour activer le mode JSX React.
- **Sitemap :** Ajout des nouvelles pages au sitemap.
