## Changelog : rapportnav2 (30 derniers jours, au 7 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives à l'interface de gestion des équipages de mission (PAM), ainsi que des corrections de bugs et des optimisations de performance, notamment concernant l'affichage et la manipulation des données liées aux contrôles et infractions. De plus, l'application intègre désormais la gestion des pays via une API externe et des améliorations ont été apportées au formulaire et à la sauvegarde des données.

### Évolutions fonctionnelles
- Refonte de l'interface utilisateur pour la gestion des équipages de mission (PAM).
- Intégration de données de pays via une API externe, permettant d'enrichir les informations disponibles.
- Amélioration de l'affichage et de la gestion des contrôles et infractions, avec l'implémentation d'un système d'onglets pour une meilleure organisation.
- Ajout de deux nouveaux attributs à ActionFish.
- Amélioration de la gestion des informations générales et des cibles pour éviter les doublons.

### Évolutions techniques
- Optimisation des performances lors du calcul du statut des actions, en utilisant les données en mémoire plutôt que de requêter la base de données à chaque fois.
- Amélioration des performances des requêtes liées aux infractions et aux contrôles grâce à l'utilisation de `@BatchSize`.
- Mise à jour de Spring Boot en version 4.1.0.
- Correction de bugs liés à la sauvegarde des données et à la gestion des relations en base de données.

### Autres changements
- Correction de problèmes de validation des règles.
- Mise à jour des dépendances (undici).
- Corrections mineures et ajustements de l'interface utilisateur.
- Ajout d'un environnement pour les actions de patch dans les stubs.
- Audit de sécurité npm.
