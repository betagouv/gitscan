## Changelog : verseau2 (30 derniers jours, au 10 juillet 2026)

### Résumé
Ce mois-ci, Verseau2 a bénéficié d'améliorations significatives concernant la gestion des transferts de fichiers, notamment pour les agences de l'eau, avec l'ajout de la gestion du FTP, SFTP et des fichiers ZIP. L'application a également été améliorée en termes de performance, de gestion des erreurs et d'expérience utilisateur, avec l'intégration de Sentry pour le suivi des erreurs et des améliorations de l'interface utilisateur.

### Évolutions fonctionnelles
- Ajout de la gestion des fichiers ZIP pour les agences de l'eau [#128](https://github.com/MTES-MCT/verseau2/issues/128).
- Ajout de la gestion des destinataires pour l'envoi de rapports [#127](https://github.com/MTES-MCT/verseau2/issues/127).
- Gestion des connexions FTP avec mot de passe pour les agences de l'eau [#125](https://github.com/MTES-MCT/verseau2/issues/125).
- Ajout d'un tooltip pour expliquer le champ hcnf [#117](https://github.com/MTES-MCT/verseau2/issues/117).
- Affichage du nombre total de mesures au-dessus du tableau [#113](https://github.com/MTES-MCT/verseau2/issues/113).
- Ajout d'un avis sur les indicateurs pour les réseaux mixtes/unitaires [#112](https://github.com/MTES-MCT/verseau2/issues/112).
- Ajout d'un composant FixedHeightTable pour une meilleure présentation des données [#116](https://github.com/MTES-MCT/verseau2/issues/116).
- Amélioration de l'autocomplétion et suppression du flickering dans le composant SelectAutocomplete [#100](https://github.com/MTES-MCT/verseau2/issues/100).

### Évolutions techniques
- Ajout d'un client FTP pour la gestion des agences de l'eau et refactorisation des transferts de fichiers pour SFTP [#134](https://github.com/MTES-MCT/verseau2/issues/134).
- Normalisation des clés d'agence pour la configuration SFTP [#129](https://github.com/MTES-MCT/verseau2/issues/129).
- Amélioration de la journalisation lors de l'envoi de fichiers SFTP.
- Amélioration des performances des tests backend [#118](https://github.com/MTES-MCT/verseau2/issues/118).
- Création et gestion d'une vue matérialisée `mv_steu_scl_itv` [#115](https://github.com/MTES-MCT/verseau2/issues/115).
- Intégration de Sentry pour la gestion des erreurs côté frontend [#122](https://github.com/MTES-MCT/verseau2/issues/122) et configuration des variables Sentry [#123](https://github.com/MTES-MCT/verseau2/issues/123).
- Suppression des logs de tests [#130](https://github.com/MTES-MCT/verseau2/issues/130).
- Amélioration de la gestion des logs dans le contrôleur Masa.

### Autres changements
- Mise à jour de la documentation des commandes et correction de la description des tests.
- Mise à jour de la documentation AGENTS.md.
- Correction du format du nom d'utilisateur dans le XML [#126](https://github.com/MTES-MCT/verseau2/issues/126).
- Correction des scripts de test pour une exécution correcte [#124](https://github.com/MTES-MCT/verseau2/issues/124).
- Préservation des fins de ligne CRLF lors de l'ajout du tag NomContact [#114](https://github.com/MTES-MCT/verseau2/issues/114).
- Amélioration de la gestion des tables exclues dans la fonction `parseExcludedTables`.
- Mise à jour de pg-boss et ajout du tableau de bord pg-boss.
- Correction de la configuration des tests.
