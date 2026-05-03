## Changelog : proconnect-identite (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des informations relatives aux établissements publics, des corrections de fuites mémoire et une maintenance générale des dépendances du projet. Une nouvelle fonctionnalité permet d'intégrer la tranche d'effectifs d'une unité légale dans l'index.

### Évolutions fonctionnelles
- Ajout de la prise en charge de la "tranche-effectifs-unite-legale" dans l'index, permettant une meilleure identification des établissements. [#1898](https://github.com/proconnect-gouv/proconnect-identite/pull/1898)
- Mise à jour de la logique pour déterminer si un établissement est "petit" (isSmallEtablissementPublic). [#1890](https://github.com/proconnect-gouv/proconnect-identite/pull/1890)

### Évolutions techniques
- Correction d'une fuite mémoire dans la gestion des requêtes HTTP, en revenant à l'utilisation d'Axios. [#1905](https://github.com/proconnect-gouv/proconnect-identite/pull/1905), [#1896](https://github.com/proconnect-gouv/proconnect-identite/pull/1896)
- Remplacement initialement tenté de Axios par Fetch a été annulé en raison de problèmes de fuite mémoire.
- Les dépendances "peer" du package identité sont maintenant optionnelles, ce qui offre plus de flexibilité aux intégrateurs. [#1906](https://github.com/proconnect-gouv/proconnect-identite/pull/1906)
- Ajout de routes de ping pour permettre aux services externes de vérifier la disponibilité de l'application. [#1900](https://github.com/proconnect-gouv/proconnect-identite/pull/1900)

### Autres changements
- Mise à jour de plusieurs dépendances : `nodemailer`, `hono`, `drizzle-orm`, `vite`, `sentry`, `dotenvx`, `follow-redirects`.
- Ajout de "changesets" pour faciliter la gestion des versions et la génération du changelog. [#1902](https://github.com/proconnect-gouv/proconnect-identite/pull/1902), [#1901](https://github.com/proconnect-gouv/proconnect-identite/pull/1901), [#1897](https://github.com/proconnect-gouv/proconnect-identite/pull/1897), [#1892](https://github.com/proconnect-gouv/proconnect-identite/pull/1892)
