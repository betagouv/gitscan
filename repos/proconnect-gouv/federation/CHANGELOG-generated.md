## Changelog : federation (30 derniers jours)

### Résumé
Ce changelog présente les évolutions récentes de la solution d'identification des professionnels. Les modifications incluent une refonte de l'interface utilisateur pour une meilleure expérience, des corrections de bugs pour améliorer la stabilité, et des optimisations techniques pour une meilleure performance et sécurité. Des alertes ont également été ajoutées pour l'environnement de test.

### Évolutions fonctionnelles
- Nouvelle interface utilisateur avec une disposition en une seule colonne (#802, #829).
- Ajout d'un bouton de contact pour signaler les erreurs internes (#829).
- Amélioration de la version responsive de la nouvelle interface (#786, #868).
- Messages d'erreur améliorés pour les liens "mailto" (#853).
- Ajout d'une alerte pour l'environnement de test (#848).

### Évolutions techniques
- Passage au module ESNext (#855).
- Suppression de l'index TTL MongoDB qui supprimait les sous-utilisateurs après 3 ans (#850).
- Correction d'un problème empêchant le core de planter en cas d'échec du proxy (#869).
- Correction des tests d'intégration (#832).
- Optimisation du renouvellement du token CSRF pour éviter des requêtes inutiles (#831).
- Mise à jour de plusieurs dépendances :
    - `axios` (versions 1.12.2 -> 1.13.5) (#851, #852)
    - `pg` (versions 8.16.3 -> 8.18.0) (#858)
    - `systeminformation` (versions 5.30.5 -> 5.31.1) (#869)
    - `docker/build-push-action` (version 6.18.0 -> 6.19.2) (#856)
    - `otpauth` (version 9.4.1 -> 9.5.0) (#857)
    - `@nestjs/common` (version 11.1.9 -> 11.1.13) (#861)
    - `jquery` (version 3.7.1 -> 4.0.0) (#863)
    - `docker/login-action` (version 3.6.0 -> 3.7.0) (#845)
    - Diverses autres mises à jour de dépendances mineures (#833, #834, #835, #836, #837, #838, #839, #841, #846)

### Autres changements
- Suppression du fichier manifest.webmanifest trompeur (#872).
- Correction de l'analyse des variables d'environnement booléennes dans Ansible (#849).
- Suppression d'une exception FranceConnect (#830).
