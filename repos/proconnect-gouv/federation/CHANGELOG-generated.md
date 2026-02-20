## Changelog : federation (30 derniers jours)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur avec une nouvelle interface, des corrections de bugs et l'ajout de fonctionnalités d'aide et de support. Des optimisations techniques ont également été apportées pour améliorer la stabilité et la sécurité de la plateforme, notamment en simplifiant la gestion des erreurs et des tokens CSRF.

### Évolutions fonctionnelles
- Nouvelle interface utilisateur avec une mise en page à une colonne (#802, #829).
- Ajout d'un bouton de contact pour signaler des problèmes sur les pages d'erreur, incluant un lien vers le support pour les erreurs liées aux fournisseurs d'identité (#829, #807).
- Amélioration des messages d'erreur pour les problèmes liés à la configuration du mailto (#853).
- Correction d'un bug d'affichage du bouton de contact sur l'erreur Y50006 (#823).
- Modification de l'action principale pour l'erreur Y50006 (#820).

### Évolutions techniques
- Passage aux modules ESNext pour une meilleure organisation du code (#855).
- Suppression d'un index TTL obsolète dans MongoDB qui supprimait les données des utilisateurs après 3 ans (#850).
- Suppression de l'exception `FcException` inutile (#824).
- Suppression de la mise à jour inutile du token CSRF à chaque requête (#831).
- Simplification du hook de sauvegarde de l'administration (#805).
- Mise à jour des dépendances : `pg` (8.16.3 -> 8.18.0), `systeminformation` (5.30.5 -> 5.31.1), `axios` (1.12.2 -> 1.13.5), `lodash` (4.17.21 -> 4.17.23), `type-fest` (4.41.0 -> 5.0.1), `prettier` (3.3.3 -> 3.7.4), `diff` (4.0.2 -> 4.0.4), `docker/login-action` (3.6.0 -> 3.7.0), `otpauth` (9.4.1 -> 9.5.0), `@nestjs/common` (11.1.9 -> 11.1.13), `jquery` (3.7.1 -> 4.0.0), `actions/attest-build-provenance` (3.1.0 -> 3.2.0), `actions/checkout` (6.0.1 -> 6.0.2), `@isaacs/brace-expansion` et d'autres.
- Amélioration des logs de débogage pour les fournisseurs d'identité (IdP) et les points de terminaison (SP) (#853).

### Autres changements
- Ajout d'une alerte pour l'environnement de test (#848).
- Mise à jour de la configuration Ansible pour gérer correctement les variables booléennes (#849).
- Amélioration de la réactivité de la nouvelle interface utilisateur (#868).
