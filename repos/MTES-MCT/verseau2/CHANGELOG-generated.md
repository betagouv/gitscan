## Changelog : verseau2 (30 derniers jours, au 11 juin 2026)

### Résumé
Ce mois-ci, Verseau2 a bénéficié d'améliorations significatives en termes de fonctionnalités et de corrections, notamment autour de la gestion des données MASA, des indicateurs de conformité, et de l'export des données. Des optimisations ont également été apportées au backend pour améliorer la performance et la lisibilité du code. L'interface utilisateur a été enrichie avec de nouvelles visualisations et des informations contextuelles.

### Évolutions fonctionnelles
- Ajout de l'affichage du nombre total de mesures au-dessus du tableau des données [#113](https://github.com/MTES-MCT/verseau2/issues/113).
- Ajout d'un avis informatif pour les indicateurs concernant les réseaux mixtes/unitaires [#112](https://github.com/MTES-MCT/verseau2/issues/112).
- Implémentation du décodage de la clé privée SFTP en UTF-8 [#111](https://github.com/MTES-MCT/verseau2/issues/111).
- Ajout de la gestion des statuts MASA et mise à jour des entités associées [#92](https://github.com/MTES-MCT/verseau2/issues/92).
- Ajout de la gestion des agences de l'eau par SIRET [#90](https://github.com/MTES-MCT/verseau2/issues/90).
- Ajout d'un graphique pour visualiser les mesures [#88](https://github.com/MTES-MCT/verseau2/issues/88).
- Ajout de la gestion des filtres pour tous les contrôles [#91](https://github.com/MTES-MCT/verseau2/issues/91).
- Ajout d'une bannière d'information sur la conformité réglementaire [#104](https://github.com/MTES-MCT/verseau2/issues/104).
- Ajout de la classe `truncate-cell` pour tronquer le texte des indicateurs [#103](https://github.com/MTES-MCT/verseau2/issues/103).
- Formatage de la date de validation des critères [#102](https://github.com/MTES-MCT/verseau2/issues/102).
- Ajout de liens cliquables pour les indicateurs [#98](https://github.com/MTES-MCT/verseau2/issues/98).
- Ajout de l'export CSV pour les données [#82](https://github.com/MTES-MCT/verseau2/issues/82).
- Ajout de nouvelles colonnes au bilan [#72](https://github.com/MTES-MCT/verseau2/issues/72).
- Ajout de la gestion des dates de début et de fin pour les bilans et nouvel endpoint paramètres [#84](https://github.com/MTES-MCT/verseau2/issues/84).
- Suppression des filtres avancés en mode STEU [#94](https://github.com/MTES-MCT/verseau2/issues/94).
- Ajout d'un service d'authentification mock avec gestion [#85](https://github.com/MTES-MCT/verseau2/issues/85).

### Évolutions techniques
- Amélioration de la gestion des tables exclues pour `pg_restore` [#109](https://github.com/MTES-MCT/verseau2/issues/109).
- Ajustement de la vérification DBO5 par rapport à CMA N-1 [#107](https://github.com/MTES-MCT/verseau2/issues/107).
- Correction des vérifications DCO et DBO5 pour A3 et A4 [#106](https://github.com/MTES-MCT/verseau2/issues/106).
- Implémentation du contrôle de débit A3 A4 [#96](https://github.com/MTES-MCT/verseau2/issues/96).
- Correction du calcul du débit de référence en cascade [#105](https://github.com/MTES-MCT/verseau2/issues/105).
- Refactor du calcul de 'Maximum entre PC95 et débit de référence' [#101](https://github.com/MTES-MCT/verseau2/issues/101).
- Suppression de cache inutile [#99](https://github.com/MTES-MCT/verseau2/issues/99).
- Amélioration de la lisibilité du code avec des blocs conditionnels [#97](https://github.com/MTES-MCT/verseau2/issues/97).
- Renommage des méthodes de détail dans `MasaProvider`.
- Ajout de la gestion CORS pour les déploiements frontend/backend [#83](https://github.com/MTES-MCT/verseau2/issues/83).
- Correction d'une erreur lors du déploiement de `sync-pg` [#87](https://github.com/MTES-MCT/verseau2/issues/87).
- Correction d'une erreur `ERR_PNPM_ABORTED_REMOVE_MODULES_DIR_NO_TTY`.
- Mise à jour de la dépendance `axios` vers la version 1.16 [#66](https://github.com/MTES-MCT/verseau2/issues/66).

### Autres changements
- Suppression de l'entrée `graphify-out` et ajout de `understand-anything` dans le fichier `.gitignore`.
- Correction d'une erreur de restauration pg en local [#86](https://github.com/MTES-MCT/verseau2/issues/86).
- Ajout de la configuration du gestionnaire de paquets et des moteurs [#86](https://github.com/MTES-MCT/verseau2/issues/86).
