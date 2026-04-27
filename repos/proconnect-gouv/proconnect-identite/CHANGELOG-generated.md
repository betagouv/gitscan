## Changelog : proconnect-identite (30 derniers jours, au 21 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse et de la maintenance du code, avec notamment la correction d'une fuite de mémoire et l'optimisation des dépendances. De nouvelles informations sur les effectifs des unités légales sont désormais disponibles et des routes de ping ont été ajoutées pour faciliter la surveillance de l'application par des services externes.

### Évolutions fonctionnelles
- Ajout de la tranche d'effectifs de l'unité légale dans l'index, améliorant ainsi la gestion des informations relatives aux entreprises. [#1899](https://github.com/proconnect-gouv/proconnect-identite/pull/1899)
- Mise à jour de la logique pour déterminer si un établissement est considéré comme "petit", améliorant la précision de cette classification. [#1870](https://github.com/proconnect-gouv/proconnect-identite/pull/1870)
- Ajout de routes de ping pour permettre aux services externes de vérifier la disponibilité de l'application. [#1890](https://github.com/proconnect-gouv/proconnect-identite/pull/1890)

### Évolutions techniques
- Correction d'une fuite de mémoire dans la gestion des requêtes HTTP, améliorant la stabilité de l'application. [#1904](https://github.com/proconnect-gouv/proconnect-identite/pull/1904)
- Remplacement temporaire de Axios par Fetch pour corriger la fuite mémoire, puis retour à Axios. [#1905](https://github.com/proconnect-gouv/proconnect-identite/pull/1905) et [#1906](https://github.com/proconnect-gouv/proconnect-identite/pull/1906)
- Simplification de la gestion des dépendances en rendant les dépendances "peer" optionnelles. [#1896](https://github.com/proconnect-gouv/proconnect-identite/pull/1896)
- Mise à jour de plusieurs dépendances, notamment `hono`, `nodemailer`, `drizzle-orm`, `vite` et `cypress-io/github-action`, pour bénéficier des dernières corrections et améliorations.

### Autres changements
- Ajout de formatteur pour la tranche effectifs unité légale. [#1897](https://github.com/proconnect-gouv/proconnect-identite/pull/1897)
- Renommage et nettoyage du code pour améliorer la lisibilité et la maintenabilité. [#1895](https://github.com/proconnect-gouv/proconnect-identite/pull/1895)
- Intégration de changements de version automatique via `changesets`. [#1902](https://github.com/proconnect-gouv/proconnect-identite/pull/1902) et [#1900](https://github.com/proconnect-gouv/proconnect-identite/pull/1900)
