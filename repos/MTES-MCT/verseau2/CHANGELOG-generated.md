## Changelog : verseau2 (30 derniers jours, au 03 juillet 2026)

### Résumé
Ce mois-ci, Verseau2 a bénéficié d'améliorations significatives concernant la gestion des fichiers (ZIP, FTP), la robustesse du traitement des données (débit, conformité) et l'expérience utilisateur (Sentry, tooltip, autocomplete). Des optimisations de performance et des corrections de bugs ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la gestion des fichiers ZIP pour les agences de l'eau [#128](https://github.com/MTES-MCT/verseau2/issues/128).
- Ajout de la gestion des connexions FTP avec mot de passe [#125](https://github.com/MTES-MCT/verseau2/issues/125).
- Ajout de la gestion des destinataires pour l'envoi de rapports [#127](https://github.com/MTES-MCT/verseau2/issues/127).
- Amélioration de l'interface utilisateur avec l'ajout d'un tooltip pour expliquer le champ hcnf [#117](https://github.com/MTES-MCT/verseau2/issues/117).
- Amélioration de l'autocomplete avec un filtre côté client et suppression du flickering [#100](https://github.com/MTES-MCT/verseau2/issues/100).
- Ajout d'un composant `FixedHeightTable` pour une meilleure gestion des tableaux [#116](https://github.com/MTES-MCT/verseau2/issues/116).
- Affichage du nombre total de mesures au-dessus du tableau [#113](https://github.com/MTES-MCT/verseau2/issues/113).
- Ajout d'un avis sur les indicateurs pour les réseaux mixtes/unitaires [#112](https://github.com/MTES-MCT/verseau2/issues/112).
- Implémentation du contrôle de débit A3 et A4 [#96](https://github.com/MTES-MCT/verseau2/issues/96).

### Évolutions techniques
- Intégration de Sentry pour la gestion des erreurs et le suivi des performances côté frontend [#122](https://github.com/MTES-MCT/verseau2/issues/122) et ajout de variables de configuration [#123](https://github.com/MTES-MCT/verseau2/issues/123).
- Amélioration des performances des tests backend [#118](https://github.com/MTES-MCT/verseau2/issues/118).
- Création et gestion d'une vue matérialisée `mv_steu_scl_itv` pour optimiser les requêtes [#115](https://github.com/MTES-MCT/verseau2/issues/115).
- Normalisation des clés d'agence pour la configuration SFTP [#129](https://github.com/MTES-MCT/verseau2/issues/129).
- Décodage de la clé privée SFTP en UTF-8 [#111](https://github.com/MTES-MCT/verseau2/issues/111).
- Ajout d'un script pour tester le téléversement massif de fichiers XML [#119](https://github.com/MTES-MCT/verseau2/issues/119).
- Ajout de la gestion des tables exclues pour `pg_restore` [#109](https://github.com/MTES-MCT/verseau2/issues/109).
- Correction du calcul du débit de référence en cascade [#105](https://github.com/MTES-MCT/verseau2/issues/105).

### Autres changements
- Correction du format du nom d'utilisateur dans le XML [#126](https://github.com/MTES-MCT/verseau2/issues/126).
- Ajustement de la vérification DBO5 par rapport à CMA N-1 [#107](https://github.com/MTES-MCT/verseau2/issues/107).
- Corrections des vérifications DCO et DBO5 pour A3 et A4 [#106](https://github.com/MTES-MCT/verseau2/issues/106).
- Suppression des logs de tests inutiles [#130](https://github.com/MTES-MCT/verseau2/issues/130).
- Mise à jour du fichier `AGENTS.md` [#129](https://github.com/MTES-MCT/verseau2/issues/129).
- Préservation des fins de ligne CRLF lors de l'ajout du tag NomContact [#114](https://github.com/MTES-MCT/verseau2/issues/114).
- Correction des scripts de test [#124](https://github.com/MTES-MCT/verseau2/issues/124).
