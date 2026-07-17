## Changelog : mobilic (30 derniers jours, au 16 juillet 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'interface utilisateur, notamment la refonte de l'en-tête et du pied de page avec les composants DSFR, ainsi que des corrections de bugs et des optimisations de performance. Des fonctionnalités ont été ajoutées pour faciliter la gestion des missions et des activités, notamment pour les administrateurs.

### Évolutions fonctionnelles
- Refonte de l'en-tête et du pied de page avec les composants DSFR pour une meilleure cohérence visuelle et accessibilité [#891](https://github.com/MTES-MCT/mobilic/pull/891), [#902](https://github.com/MTES-MCT/mobilic/pull/902), [#900](https://github.com/MTES-MCT/mobilic/pull/900), [#869](https://github.com/MTES-MCT/mobilic/pull/869).
- Ajout de la possibilité d'annuler une mission en cours [#889](https://github.com/MTES-MCT/mobilic/pull/889).
- Amélioration de la vue des activités pour les administrateurs, avec notamment un format d'heure plus clair et des boutons d'édition conformes aux standards DSFR [#880](https://github.com/MTES-MCT/mobilic/pull/880), [#879](https://github.com/MTES-MCT/mobilic/pull/879), [#878](https://github.com/MTES-MCT/mobilic/pull/878).
- Ajout du logo Perff sur la page partenaires [#892](https://github.com/MTES-MCT/mobilic/pull/892).
- Modification du libellé pour le transport de marchandises lourdes [#881](https://github.com/MTES-MCT/mobilic/pull/881).
- Possibilité de modifier les jours de travail enregistrés [#859](https://github.com/MTES-MCT/mobilic/pull/859).

### Évolutions techniques
- Optimisation de la récupération des webinaires pour améliorer la performance [#894](https://github.com/MTES-MCT/mobilic/pull/894).
- Correction de problèmes de performance liés aux requêtes d'historique [#886](https://github.com/MTES-MCT/mobilic/pull/886).
- Refactoring de l'en-tête pour améliorer la lisibilité et la maintenabilité du code.
- Centralisation de la constante `DSFR_BRAND_TOP` pour une meilleure cohérence.
- Utilisation de `Number.parseInt` au lieu de `parseInt` pour éviter des erreurs potentielles.
- Amélioration de la gestion des filtres après validation d'une mission ou d'un congé [#893](https://github.com/MTES-MCT/mobilic/pull/893), [#883](https://github.com/MTES-MCT/mobilic/pull/883).
- Suppression de l'option FranceConnect pour l'inscription des employés [#890](https://github.com/MTES-MCT/mobilic/pull/890), [#870](https://github.com/MTES-MCT/mobilic/pull/870).

### Autres changements
- Correction de problèmes d'affichage et d'accessibilité dans l'en-tête.
- Correction de bugs mineurs et améliorations de la qualité du code (linting, suppression de code inutile).
- Amélioration de la gestion des erreurs Sentry pour réduire le bruit et se concentrer sur les problèmes réels [#891](https://github.com/MTES-MCT/mobilic/pull/891).
- Correction de l'affichage du champ kilométrage pour les employés sans valeur saisie [#895](https://github.com/MTES-MCT/mobilic/pull/895).
- Correction de problèmes de style et de mise en page sur différentes pages.
