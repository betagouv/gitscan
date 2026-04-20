## Changelog : proconnect-identite (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la stabilité et de la performance du service, avec notamment la correction d'une fuite mémoire et l'optimisation de la gestion des dépendances. Des améliorations ont également été apportées à l'indexation des données et à la gestion des erreurs. Enfin, des mises à jour de dépendances ont été effectuées pour assurer la sécurité et la compatibilité du système.

### Évolutions fonctionnelles
- Ajout de routes de ping pour les services externes, permettant de vérifier la disponibilité du service. [#1900](https://github.com/proconnect-gouv/proconnect-identite/pull/1900)
- Mise à jour de la logique de détermination si un établissement public est de petite taille. [#1890](https://github.com/proconnect-gouv/proconnect-identite/pull/1890)
- Ajout du champ "tranche-effectifs-unite-legale" à l'index, corrigeant une omission précédente. [#1899](https://github.com/proconnect-gouv/proconnect-identite/pull/1899)
- Ajout d'un formateur pour le champ "tranche effectifs unite legale". [#1897](https://github.com/proconnect-gouv/proconnect-identite/pull/1897)
- Amélioration de la gestion des erreurs "trop de requêtes" en déplaçant le code dans un fichier spécifique. [#1838](https://github.com/proconnect-gouv/proconnect-identite/pull/1838)

### Évolutions techniques
- Correction d'une fuite mémoire dans la gestion des requêtes HTTP en revenant à l'utilisation d'Axios. [#1905](https://github.com/proconnect-gouv/proconnect-identite/pull/1905)
- Remplacement de l'importation de `fetch` par Axios. [#1879](https://github.com/proconnect-gouv/proconnect-identite/pull/1879)
- Mise à jour de la base image Node.js vers la version 24-slim. [#1863](https://github.com/proconnect-gouv/proconnect-identite/pull/1863)
- Les dépendances peer sont maintenant optionnelles dans le package identité. [#1906](https://github.com/proconnect-gouv/proconnect-identite/pull/1906)
- Ajout de changements pour la publication de versions (changesets). [#1901](https://github.com/proconnect-gouv/proconnect-identite/pull/1901), [#1902](https://github.com/proconnect-gouv/proconnect-identite/pull/1902), [#1876](https://github.com/proconnect-gouv/proconnect-identite/pull/1876)

### Autres changements
- Suppression d'instructions `it.only` résiduelles dans les tests Cypress. [#1870](https://github.com/proconnect-gouv/proconnect-identite/pull/1870)
- Renommage et nettoyage du code. [#1872](https://github.com/proconnect-gouv/proconnect-identite/pull/1872)
- Diverses mises à jour de dépendances (Hono, follow-redirects, nodemailer, vite, cypress, dotenvx, brace-expansion, picomatch, etc.).
