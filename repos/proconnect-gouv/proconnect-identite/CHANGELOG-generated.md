## Changelog : proconnect-identite (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la stabilité et de la performance du service, notamment avec la correction d'une fuite mémoire et le retour à l'utilisation d'Axios pour les requêtes HTTP. Des mises à jour de dépendances ont également été effectuées pour maintenir la sécurité et la compatibilité du projet. Enfin, des informations sur la taille des établissements publics sont désormais incluses.

### Évolutions fonctionnelles
- Ajout d'informations sur la "tranche effectifs unité légale" dans l'index, améliorant la granularité des données disponibles. [#1898](https://github.com/proconnect-gouv/proconnect-identite/pull/1898)
- Mise à jour de la logique pour déterminer si un établissement est considéré comme "petit" (isSmallEtablissementPublic). [#1890](https://github.com/proconnect-gouv/proconnect-identite/pull/1890)
- Ajout de routes de ping pour permettre aux services externes de vérifier la disponibilité du service d'identité. [#1900](https://github.com/proconnect-gouv/proconnect-identite/pull/1900)

### Évolutions techniques
- Correction d'une fuite mémoire dans la gestion des requêtes HTTP, améliorant la stabilité du service. [#1904](https://github.com/proconnect-gouv/proconnect-identite/pull/1904)
- Retour à l'utilisation de la librairie Axios pour les requêtes HTTP, suite à des problèmes rencontrés avec `fetch`. [#1905](https://github.com/proconnect-gouv/proconnect-identite/pull/1905)
- Les dépendances de peer sont maintenant optionnelles dans le package identité, offrant plus de flexibilité aux intégrateurs. [#1906](https://github.com/proconnect-gouv/proconnect-identite/pull/1906)
- Mises à jour de plusieurs dépendances :
    - hono (4.12.12 -> 4.12.14)
    - @hono/node-server (1.19.11 -> 1.19.13)
    - vite (7.3.1 -> 7.3.2)
    - cypress-io/github-action (7.1.8 -> 7.1.9)
    - nodemailer (8.0.4 -> 8.0.5)
    - dotenvx (1.55.1 -> 1.61.0)
    - follow-redirects (1.15.11 -> 1.16.0)
    - axios (1.13.6 -> 1.15.0)

### Autres changements
- Ajout de changeset pour faciliter la gestion des versions et la publication des changements.
- Intégration de la publication automatique des versions via GitHub Actions.
- Amélioration de la documentation et de la configuration du projet.
