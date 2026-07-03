## Changelog : verseau2 (30 derniers jours, au 02 juillet 2026)

### Résumé
Ce mois-ci, les évolutions de Verseau2 se concentrent sur l'amélioration de la gestion des fichiers (notamment ZIP et FTP), l'ajout de fonctionnalités de surveillance et d'alerte (Sentry, indicateurs de conformité), ainsi que des optimisations de performance et des corrections de bugs pour une meilleure expérience utilisateur. Des améliorations ont également été apportées aux tests et à l'infrastructure.

### Évolutions fonctionnelles
- Ajout de la gestion des fichiers ZIP pour les agences de l'eau [#128](https://github.com/MTES-MCT/verseau2/issues/128).
- Ajout de la gestion des connexions FTP avec mot de passe [#125](https://github.com/MTES-MCT/verseau2/issues/125).
- Ajout de la gestion des destinataires pour l'envoi de rapports [#127](https://github.com/MTES-MCT/verseau2/issues/127).
- Ajout d'un tooltip pour expliquer le champ hcnf [#117](https://github.com/MTES-MCT/verseau2/issues/117).
- Ajout d'une bannière d'information sur la conformité réglementaire [#104](https://github.com/MTES-MCT/verseau2/issues/104).
- Affichage du nombre total de mesures au-dessus du tableau [#113](https://github.com/MTES-MCT/verseau2/issues/113).
- Ajout d'un avis sur les indicateurs pour les réseaux mixtes/unitaires [#112](https://github.com/MTES-MCT/verseau2/issues/112).
- Ajout de liens cliquables pour les indicateurs [#98](https://github.com/MTES-MCT/verseau2/issues/98).
- Suppression des filtres avancés en mode STEU [#94](https://github.com/MTES-MCT/verseau2/issues/94).
- Ajout d'un filtre autocomplete côté client et suppression du flickering SelectAutocomplete [#100](https://github.com/MTES-MCT/verseau2/issues/100).

### Évolutions techniques
- Intégration de Sentry pour la gestion des erreurs et le suivi des performances [#122](https://github.com/MTES-MCT/verseau2/issues/122) et [#123](https://github.com/MTES-MCT/verseau2/issues/123).
- Amélioration des performances des tests backend [#118](https://github.com/MTES-MCT/verseau2/issues/118).
- Création et gestion d'une vue matérialisée `mv_steu_scl_itv` pour optimiser les requêtes [#115](https://github.com/MTES-MCT/verseau2/issues/115).
- Ajout de la gestion des tables exclues pour `pg_restore` [#109](https://github.com/MTES-MCT/verseau2/issues/109).
- Refactoring du code backend pour améliorer la lisibilité avec des blocs conditionnels [#97](https://github.com/MTES-MCT/verseau2/issues/97).
- Normalisation des clés d'agence pour la configuration SFTP [#129](https://github.com/MTES-MCT/verseau2/issues/129).
- Décodage de la clé privée SFTP en UTF-8 [#111](https://github.com/MTES-MCT/verseau2/issues/111).
- Suppression de cache inutile [#99](https://github.com/MTES-MCT/verseau2/issues/99).

### Autres changements
- Correction du format du nom d'utilisateur dans le XML [#126](https://github.com/MTES-MCT/verseau2/issues/126).
- Correction des scripts de test pour une exécution correcte [#124](https://github.com/MTES-MCT/verseau2/issues/124).
- Correction des vérifications DCO et DBO5 pour A3 et A4 [#106](https://github.com/MTES-MCT/verseau2/issues/106).
- Ajustement de la vérification DBO5 par rapport à CMA N-1 [#107](https://github.com/MTES-MCT/verseau2/issues/107).
- Correction du calcul du débit de référence pour une cascade correcte [#105](https://github.com/MTES-MCT/verseau2/issues/105).
- Ajout d'un script pour tester le téléversement massif de fichiers XML [#119](https://github.com/MTES-MCT/verseau2/issues/119).
- Ajout de la classe `truncate-cell` pour le formatage du texte des indicateurs [#103](https://github.com/MTES-MCT/verseau2/issues/103).
- Formatage de la date de validation des critères [#102](https://github.com/MTES-MCT/verseau2/issues/102).
- Revoir le calcul de 'Maximum entre PC95 et débit de référence' [#101](https://github.com/MTES-MCT/verseau2/issues/101).
- Suppression de l'entrée `graphify-out` et ajout de `understand-anything` au `.gitignore` [#96](https://github.com/MTES-MCT/verseau2/issues/96).
- Ajout d'un composant `FixedHeightTable` pour une meilleure gestion des tableaux [#116](https://github.com/MTES-MCT/verseau2/issues/116).
- Préserver les fins de ligne CRLF lors de l'ajout du tag NomContact [#114](https://github.com/MTES-MCT/verseau2/issues/114).
