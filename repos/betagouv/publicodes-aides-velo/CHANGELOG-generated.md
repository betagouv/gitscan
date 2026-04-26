## Changelog : publicodes-aides-velo (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, les mises à jour se concentrent sur la correction de données d'aides (dates de fin, liens, communes) et l'ajout de nouvelles aides locales. Des améliorations techniques ont également été apportées, notamment le remplacement de l'outil de formatage de code par Prettier et la mise à jour de certaines dépendances.

### Évolutions fonctionnelles
- Mise à jour des aides pour le Luxembourg et Monaco.
- Correction de la question relative au "revenu de référence" pour une meilleure clarté.
- Mise à jour des aides pour les communes de Gap, Saint-Alban-Leysse, Dunkerque et Oullins-Pierre-Bénite.
- Ajout de nouvelles aides pour les communautés de communes (CC) Vie et Boulogne, CCVO.
- Correction d'un doublon pour l'aide "cc loue-lison".
- Correction de liens cassés et de dates de fin d'aides dépassées.

### Évolutions techniques
- Remplacement de l'outil de formatage de code Dprint par Prettier pour une meilleure cohérence du code. [#492b479](https://github.com/betagouv/publicodes-aides-velo/commit/492b479)
- Mise à jour de la dépendance `@etalab/decoupage-administratif` vers la version 6. [#436a823](https://github.com/betagouv/publicodes-aides-velo/commit/436a823)
- Restauration de la logique de génération du fichier `communes.json`. [#38060ea](https://github.com/betagouv/publicodes-aides-velo/commit/38060ea)
- Amélioration du script de gestion des aides : tri par type de collectivité et date des aides obsolètes. [#acfae35](https://github.com/betagouv/publicodes-aides-velo/commit/acfae35)

### Autres changements
- Correction du workflow de publication (release). [#94837a6](https://github.com/betagouv/publicodes-aides-velo/commit/94837a6)
- Application du formatage Prettier aux fichiers Publicodes. [#6d5cfc4](https://github.com/betagouv/publicodes-aides-velo/commit/6d5cfc4)
- Ajout d'un nouveau workflow pour les pull requests de mise à jour des packages. [#7db9959](https://github.com/betagouv/publicodes-aides-velo/commit/7db9959)
