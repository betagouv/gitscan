## Changelog : federation (30 derniers jours)

### Résumé
Ce mois-ci, les évolutions de Federation se sont concentrées sur l'amélioration de l'expérience utilisateur, notamment en ajoutant des boutons de contact pour faciliter l'assistance en cas d'erreur, et en améliorant la clarté des messages d'erreur. Des corrections de bugs ont également été apportées pour stabiliser l'application et améliorer sa fiabilité. Enfin, des optimisations techniques et des mises à jour de dépendances ont été réalisées pour maintenir la sécurité et la performance de la plateforme.

### Évolutions fonctionnelles
- Ajout d'un bouton de contact pour signaler les erreurs internes (Y50006) et contacter le support. (#807, #823)
- Amélioration des messages d'erreur liés à l'authentification OIDC. (#853)
- Ajout d'une alerte en cas d'utilisation de l'environnement de test. (#848)
- Ajout d'un bouton de contact sur les pages d'erreur 500 pour faciliter la demande d'assistance. (#829)

### Évolutions techniques
- Suppression d'un index TTL obsolète sur les utilisateurs, améliorant potentiellement les performances de la base de données. (#850, #977f009e)
- Correction d'un problème lié au renouvellement du token CSRF à chaque requête, optimisant ainsi les performances. (#831, #428a6323)
- Suppression d'une exception inutile (FcException) simplifiant le code. (#830, #1e2a7c6b)
- Mise à jour de plusieurs dépendances :
    - Axios (back et admin) : passage de la version 1.12.2/1.13.2 à la version 1.13.5. (#851, #852, #87a042d9, #66f87c6f)
    - actions/attest-build-provenance : passage de la version 3.1.0 à la version 3.2.0 (#833)
    - actions/checkout : passage de la version 6.0.1 à la version 6.0.2 (#834)
    - @eslint-community/eslint-plugin-eslint-comments (#836)
    - type-fest (back) : passage de la version 5.0.1 à la version 5.4.1 (#835)
    - body-parser (back) : passage de la version 2.2.1 à la version 2.2.2 (#838)
    - prettier (admin) : passage de la version 3.7.4 à la version 3.8.0 (#839)
    - ejs (admin) : passage de la version 3.1.10 à la version 4.0.1 (#837)
    - eslint-plugin-prettier (quality) : passage de la version 5.5.4 à la version 5.5.5 (#841)
    - lodash (back, admin, quality) : passage de la version 4.17.21 à la version 4.17.23 (#826, #827, #828)
    - diff (admin) : passage de la version 4.0.2 à la version 4.0.4 (#821)
    - lodash-es (back) : passage de la version 4.17.21 à la version 4.17.23 (#825)
    - type-fest (back) : passage de la version 4.41.0 à la version 5.0.1 (#855)
    - docker/login-action : passage de la version 3.6.0 à la version 3.7.0 (#845)

### Autres changements
- Amélioration des logs de débogage pour l'IdP/SP. (#822, #90c66d21)
- Simplification du hook de sauvegarde de l'administration. (#805, #793bde7c)
- Nouvelle mise en page avec une colonne pour l'interface utilisateur. (#802, #15995866)
- Rétrogradation d'une mise à jour de dépendance (@nestjs/core) qui causait des problèmes. (#819, #952f7307)
