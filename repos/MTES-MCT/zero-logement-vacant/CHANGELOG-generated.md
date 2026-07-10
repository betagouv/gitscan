## Changelog : zero-logement-vacant (30 derniers jours, au 08 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de la performance, notamment au niveau de la page d'analyse et de la gestion des données de référence. Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été apportées, notamment concernant les filtres, l'édition des propriétaires et la gestion des utilisateurs. Enfin, une migration technique vers de nouveaux outils de linting et de formatage de code a été réalisée.

### Évolutions fonctionnelles
- Amélioration de la page d'analyse : mise en cache des données pour une meilleure réactivité.
- Correction de l'affichage des filtres intercommunaux pour les DDT.
- Correction de l'affichage de l'année de vacance (remplacement de "inconsistancy2022" par "2023").
- Correction de la couleur des icônes de filtre pour respecter la charte graphique.
- Possibilité d'éditer les propriétaires dont l'adresse BAN a un score nul.
- Amélioration de la gestion des périmètres utilisateurs pour les structures multi-établissements.
- Ajout d'une liste des consommateurs LOVAC non enregistrés dans CEREMA.
- Ajout d'un contrôle plein écran à la carte des logements.
- Correction de l'affichage du champ "Date de naissance" des propriétaires (rendu optionnel).
- Correction de l'affichage de l'information "Pas d'information" pour le type de propriétaire.
- Amélioration de la gestion des filtres sur la page des logements.
- Ajout d'une fonctionnalité de déploiement en démonstration sur la production.
- Ajout de seeds pour la démonstration.

### Évolutions techniques
- Migration des outils de linting et de formatage de code vers `oxlint` et `oxfmt`.
- Refactorisation du code pour supprimer l'ancienne librairie de composants DSFR.
- Migration vers l'utilisation de "factories" pour la création de données de test et de démonstration.
- Mise en place d'un cache pour les données de référence (provenant de Metabase) afin d'améliorer les performances.
- Migration de la validation des données vers `validatorNext` pour une meilleure maintenabilité.
- Amélioration de la gestion des erreurs et des types dans le code.
- Utilisation de Terraform pour le déploiement du frontend.
- Mise à jour des dépendances.

### Autres changements
- Documentation : ajout de spécifications de conception pour les nouvelles fonctionnalités.
- Nettoyage du code et suppression de code obsolète.
- Amélioration des tests unitaires et d'intégration.
- Mise à jour de la configuration de l'environnement de développement.
- Correction de la configuration de l'image MapLibre.
- Ajout de scripts pour faciliter le backfill des données.
- Amélioration de la gestion des logs et du monitoring.
