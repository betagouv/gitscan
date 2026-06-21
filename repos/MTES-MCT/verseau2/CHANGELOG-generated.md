## Changelog : verseau2 (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, Verseau2 a bénéficié d'améliorations significatives en termes de fonctionnalités et de performance. Les utilisateurs profiteront d'une meilleure expérience grâce à l'ajout de nouveaux indicateurs, de filtres, de visualisations graphiques et d'une gestion améliorée des erreurs. Des optimisations côté serveur et des corrections de bugs ont également été apportées pour une plus grande stabilité et fiabilité.

### Évolutions fonctionnelles
- Ajout de la gestion des erreurs avec Sentry pour une meilleure détection et résolution des problèmes [#122](https://github.com/MTES-MCT/verseau2/issues/122).
- Amélioration de l'expérience utilisateur avec l'ajout d'un filtre autocomplete et suppression du flickering dans la sélection [#100](https://github.com/MTES-MCT/verseau2/issues/100).
- Ajout d'un tooltip pour expliquer le champ hcnf [#117](https://github.com/MTES-MCT/verseau2/issues/117).
- Ajout d'un composant `FixedHeightTable` pour une meilleure présentation des données [#116](https://github.com/MTES-MCT/verseau2/issues/116).
- Affichage du nombre total de mesures au-dessus du tableau [#113](https://github.com/MTES-MCT/verseau2/issues/113).
- Ajout d'un avis sur les indicateurs pour les réseaux mixtes/unitaires [#112](https://github.com/MTES-MCT/verseau2/issues/112).
- Ajout d'une bannière d'information sur la conformité réglementaire [#104](https://github.com/MTES-MCT/verseau2/issues/104).
- Ajout de la classe `truncate-cell` pour tronquer le texte des indicateurs [#103](https://github.com/MTES-MCT/verseau2/issues/103).
- Formatage de la date de validation des critères [#102](https://github.com/MTES-MCT/verseau2/issues/102).
- Ajout de liens cliquables pour les indicateurs [#98](https://github.com/MTES-MCT/verseau2/issues/98).
- Ajout de la gestion des filtres pour tous les contrôles [#91](https://github.com/MTES-MCT/verseau2/issues/91).
- Ajout d'un graphique pour visualiser les mesures [#88](https://github.com/MTES-MCT/verseau2/issues/88).
- Ajout de la gestion des statuts MASA et mise à jour des entités [#92](https://github.com/MTES-MCT/verseau2/issues/92).
- Ajout de la gestion des agences de l'eau par SIRET [#90](https://github.com/MTES-MCT/verseau2/issues/90).
- Suppression des filtres avancés en mode STEU [#94](https://github.com/MTES-MCT/verseau2/issues/94).

### Évolutions techniques
- Amélioration des performances des tests backend [#118](https://github.com/MTES-MCT/verseau2/issues/118).
- Création et gestion d'une vue matérialisée `mv_steu_scl_itv` pour optimiser les requêtes [#115](https://github.com/MTES-MCT/verseau2/issues/115).
- Ajout d'un script pour tester le téléversement massif de fichiers XML [#119](https://github.com/MTES-MCT/verseau2/issues/119).
- Ajout de la gestion des tables exclues pour `pg_restore` [#109](https://github.com/MTES-MCT/verseau2/issues/109).
- Correction de la vérification DBO5 par rapport à CMA N-1 [#107](https://github.com/MTES-MCT/verseau2/issues/107).
- Correction des vérifications DCO et DBO5 pour A3 et A4 [#106](https://github.com/MTES-MCT/verseau2/issues/106).
- Implémentation du contrôle de débit A3/A4 [#96](https://github.com/MTES-MCT/verseau2/issues/96).
- Correction du calcul du débit de référence en cascade [#105](https://github.com/MTES-MCT/verseau2/issues/105).
- Suppression de cache inutile [#99](https://github.com/MTES-MCT/verseau2/issues/99).
- Amélioration de la lisibilité du code avec des blocs conditionnels [#97](https://github.com/MTES-MCT/verseau2/issues/97).
- Décodage de la clé privée SFTP en UTF-8 [#111](https://github.com/MTES-MCT/verseau2/issues/111).
- Renommage des méthodes de détail dans `MasaProvider` [#89](https://github.com/MTES-MCT/verseau2/issues/89).
- Revoir le calcul de 'Maximum entre PC95 et débit de référence' [#101](https://github.com/MTES-MCT/verseau2/issues/101).

### Autres changements
- Suppression de l'entrée `graphify-out` et ajout de `understand-anything` dans le fichier `.gitignore`.
- Ajout de la gestion des API MASA [#93](https://github.com/MTES-MCT/verseau2/issues/93).
- Préserver les fins de ligne CRLF lors de l'ajout du tag NomContact [#114](https://github.com/MTES-MCT/verseau2/issues/114).
