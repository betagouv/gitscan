## Changelog : mobilic-api (30 derniers jours, au 9 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la performance de l'API et du tableau de bord administrateur, ainsi que sur des corrections de données et de comptage pour le tableau de bord. Des améliorations ont également été apportées à la gestion des alertes réglementaires et à la gestion des pauses longues.

### Évolutions fonctionnelles
- Le tableau de bord administrateur a été amélioré avec des indicateurs plus précis et alignés sur les retours utilisateurs [#705](https://github.com/MTES-MCT/mobilic-api/pull/705), [#703](https://github.com/MTES-MCT/mobilic-api/pull/703).
- Les alertes réglementaires mensuelles sont désormais divisées en alertes jour et nuit [#4b93228](https://github.com/MTES-MCT/mobilic-api/commit/4b93228).
- Un indicateur est maintenant présent sur le tableau de bord pour identifier les jours avec plusieurs employeurs [#8c81b4f](https://github.com/MTES-MCT/mobilic-api/commit/8c81b4f).
- Correction d'un bug qui empêchait le comptage correct des invitations sur le tableau de bord administrateur [#62da82f](https://github.com/MTES-MCT/mobilic-api/pull/705).
- Correction de la sémantique des compteurs du tableau de bord et gestion des fuseaux horaires [#d567ff6](https://github.com/MTES-MCT/mobilic-api/commit/d567ff6).
- Correction du calcul du dépassement de temps de travail avant la pause longue [#9dd5ace](https://github.com/MTES-MCT/mobilic-api/commit/9dd5ace).

### Évolutions techniques
- Amélioration des performances de l'API en augmentant le nombre de workers Gunicorn et en réduisant les timeouts [#713](https://github.com/MTES-MCT/mobilic-api/pull/713), [#711](https://github.com/MTES-MCT/mobilic-api/pull/711), [#aed848c](https://github.com/MTES-MCT/mobilic-api/commit/aed848c).
- La configuration du nombre de workers Gunicorn est désormais gérée via la variable d'environnement `WEB_CONCURRENCY` [#3739377](https://github.com/MTES-MCT/mobilic-api/commit/3739377).
- Suppression de code inutilisé concernant la gestion des pauses longues [#aa8a710](https://github.com/MTES-MCT/mobilic-api/commit/aa8a710).
- Amélioration des performances de la page d'accueil [#38721c2](https://github.com/MTES-MCT/mobilic-api/commit/38721c2).

### Autres changements
- Correction d'un problème lié au téléchargement des CGU et des données personnelles [#702](https://github.com/MTES-MCT/mobilic-api/pull/702).
- Ajout d'un indicateur `hasAnyMissionThisWeek` exposé sur le tableau de bord [#09c8ab3](https://github.com/MTES-MCT/mobilic-api/commit/09c8ab3).
