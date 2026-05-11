## Changelog : proconnect-identite (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse et de la performance du service, avec notamment la correction d'une fuite mémoire et l'ajout de routes de ping pour une meilleure surveillance de la disponibilité. Des mises à jour de dépendances ont également été effectuées pour maintenir la sécurité et la stabilité de l'application. Enfin, des améliorations ont été apportées à la gestion des informations relatives aux effectifs des entités légales.

### Évolutions fonctionnelles
- Ajout de routes de ping pour permettre aux services externes de vérifier la disponibilité du service d'identité [#1893](https://github.com/proconnect-gouv/proconnect-identite/pull/1893).
- Intégration de la tranche d'effectifs de l'unité légale dans l'index, améliorant ainsi la présentation des informations [#1899](https://github.com/proconnect-gouv/proconnect-identite/pull/1899).
- Ajout d'un formateur pour la tranche d'effectifs de l'unité légale [#1897](https://github.com/proconnect-gouv/proconnect-identite/pull/1897).
- Mise à jour de la logique de détermination si un établissement est de petite taille [#1890](https://github.com/proconnect-gouv/proconnect-identite/pull/1890).

### Évolutions techniques
- Correction d'une fuite mémoire dans la gestion des requêtes HTTP en revenant à l'utilisation d'Axios [#1904](https://github.com/proconnect-gouv/proconnect-identite/pull/1904).
- Les dépendances de peer sont maintenant optionnelles dans le package identite, offrant une plus grande flexibilité d'intégration [#1906](https://github.com/proconnect-gouv/proconnect-identite/pull/1906).
- Mises à jour des dépendances :
    - `hono` (4.12.12 -> 4.12.14)
    - `@hono/node-server` (1.19.11 -> 1.19.13)
    - `nodemailer` (8.0.5)
    - `axios` (1.13.6 -> 1.15.0)
    - `vite` (7.3.2)
    - `@dotenvx/dotenvx` (1.55.1 -> 1.61.0)
    - `follow-redirects` (1.15.11 -> 1.16.0)
    - `cypress-io/github-action` (7.1.9)

### Autres changements
- Préparation et publication de nouvelles versions du package [#1902](https://github.com/proconnect-gouv/proconnect-identite/pull/1902), [#1898](https://github.com/proconnect-gouv/proconnect-identite/pull/1898), [#1900](https://github.com/proconnect-gouv/proconnect-identite/pull/1900), [#1901](https://github.com/proconnect-gouv/proconnect-identite/pull/1901), [#1905](https://github.com/proconnect-gouv/proconnect-identite/pull/1905).
- Ajout de changeset pour faciliter le versionnement et la publication des changements.
- Nettoyage et refactorisation du code.
