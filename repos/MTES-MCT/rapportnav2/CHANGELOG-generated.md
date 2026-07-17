## Changelog : rapportnav2 (30 derniers jours, au 2026-07-16)

### Résumé
Les dernières mises à jour de rapportnav2 améliorent significativement la gestion des missions, notamment au niveau de l'interface utilisateur pour les équipages et les contrôles "Fish". Des optimisations de performance ont été apportées pour accélérer le traitement des données, et la gestion des pays a été revue pour s'appuyer sur une source de données externe. Plusieurs corrections de bugs ont également été implémentées pour améliorer la stabilité et la fiabilité de l'application.

### Évolutions fonctionnelles
- Refonte de l'interface utilisateur pour la gestion des équipages de mission (PAM).
- Intégration d'une source de données externe pour la gestion des pays.
- Ajout de deux attributs à ActionFish pour une meilleure gestion des actions.
- Implémentation d'onglets pour les contrôles "Fish", améliorant l'organisation et l'accessibilité.
- Harmonisation de l'affichage des infractions.
- Amélioration de l'affichage des cibles (targets) pour Sati.
- Correction de l'ordre des options dans les radios multiples (MultiRadio) pour Fish [#1033](https://github.com/MTES-MCT/rapportnav2/issues/1033).

### Évolutions techniques
- Optimisation des performances en réduisant les requêtes à la base de données pour le calcul du statut des actions et en utilisant le batch processing pour les infractions et les contrôles.
- Mise à jour de Spring Boot vers la version 4.1.0.
- Correction de bugs liés à la suppression d'infractions sur les contrôles Fish [#1461](https://github.com/MTES-MCT/rapportnav2/issues/1461).
- Correction de bugs liés à la duplication d'informations générales et de cibles.
- Correction de problèmes de validation des règles.

### Autres changements
- Mise à jour des dépendances (npm audit).
- Préparation de la publication des versions v2.86.0, v2.86.1 et v2.86.2.
