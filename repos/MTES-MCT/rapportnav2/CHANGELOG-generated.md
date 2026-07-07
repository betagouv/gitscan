## Changelog : rapportnav2 (30 derniers jours, au 06 juillet 2026)

### Résumé
Les dernières mises à jour de rapportnav2 se concentrent sur l'amélioration des performances, l'ajout de nouvelles fonctionnalités pour la gestion des missions (notamment l'intégration de données pays via API et la gestion des équipes de mission), et des corrections de bugs pour une meilleure expérience utilisateur. Des améliorations ont également été apportées à l'interface utilisateur, notamment pour les contrôles de navigation et les informations sur les actions.

### Évolutions fonctionnelles
- Intégration des données pays via une API : permet d'enrichir les informations relatives aux missions. [#1441](https://github.com/MTES-MCT/rapportnav2/pull/1441)
- Refonte de l'interface pour la gestion des équipes de mission (PAM).
- Amélioration de l'affichage des options dans les champs MultiRadio. [#1033](https://github.com/MTES-MCT/rapportnav2/issues/1033)
- Ajout de deux attributs à ActionFish.
- Refonte de l'affichage des contrôles de navigation (action control fish / nav).
- Ajout de la gestion des ressources et des agents.
- Ajout de la fonctionnalité "diving" pour les contrôles environnementaux.
- Ajout de la fonctionnalité "diving" pour les contrôles AEM.
- Amélioration de la gestion des informations sur les actions (entretien des moyens). [#1390](https://github.com/MTES-MCT/rapportnav2/issues/1390)
- Intégration d'un iframe Metabase pour l'affichage de tableaux de bord.

### Évolutions techniques
- Optimisation des performances :
    - Calcul du statut des actions en mémoire pour éviter des requêtes répétées à la base de données.
    - Utilisation de `@BatchSize` pour optimiser les requêtes liées aux infractions, aux contrôles, aux agents, aux rôles d'agents et aux modèles d'agents.
- Mise à jour de Spring Boot vers la version 4.1.0.
- Correction de problèmes de mapping de relations dans la base de données.
- Correction de problèmes de validation des données.
- Amélioration de la gestion des types de localisation (GPS).

### Autres changements
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Mise à jour des dépendances (undici).
- Amélioration des tests unitaires et d'intégration.
- Correction de problèmes de build et de test.
- Ajustements de la configuration du projet.
- Nettoyage du code.
- Mise à jour de la documentation.
