## Changelog : potentiel (30 derniers jours, au 2026-04-16)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'importation et de la gestion des données, notamment depuis Data.gouv, ainsi que sur la correction de bugs et l'optimisation de l'interface utilisateur. Des améliorations ont également été apportées à la gestion des garanties financières et des documents, avec un focus sur la simplification et la correction de problèmes liés aux notifications et aux formulaires.

### Évolutions fonctionnelles
- **Garanties Financières :** Refonte des pages garanties financières pour une meilleure expérience utilisateur [#4175](https://github.com/MTES-MCT/potentiel/issues/4175).
- **Notifications :** Suppression des notifications inutiles pour les étapes de projet en cas de recours [#4179](https://github.com/MTES-MCT/potentiel/issues/4179). Correction d'un bug empêchant les co-contractants de recevoir les notifications hors de leur zone [#4178](https://github.com/MTES-MCT/potentiel/issues/4178).
- **Documents :** Amélioration de la gestion des documents, notamment l'importation de références de raccordement depuis Data.gouv [#4103](https://github.com/MTES-MCT/potentiel/issues/4103) et la gestion des fichiers GF récupérés sur Data.gouv [#4096](https://github.com/MTES-MCT/potentiel/issues/4096).
- **Attestation de conformité :** Modification de l'attestation de conformité [#4159](https://github.com/MTES-MCT/potentiel/issues/4159).
- **DREALS :** Possibilité pour les DREALS de copier l'identifiant du projet en production [#4151](https://github.com/MTES-MCT/potentiel/issues/4151).
- **Actionnariat :** Ajout d'un nouveau type d'actionnariat et importation depuis Data.gouv [#4090](https://github.com/MTES-MCT/potentiel/issues/4090).
- **Mails Garanties Financières :** Ajout de nouveaux mails pour les garanties financières [#4083](https://github.com/MTES-MCT/potentiel/issues/4083).

### Évolutions techniques
- **Cache GraphQL :** Implémentation d'un cache GraphQL pour améliorer les performances [#4177](https://github.com/MTES-MCT/potentiel/issues/4177).
- **Tests :** Implémentation des tests manquants pour les délais et recours [#4182](https://github.com/MTES-MCT/potentiel/issues/4182).
- **Refactoring :** Simplification de la modélisation des Autorisations d'Opérer (AO) [#4147](https://github.com/MTES-MCT/potentiel/issues/4147). Refactorisation du code pour uniformiser les fichiers dans les spécifications [#4141](https://github.com/MTES-MCT/potentiel/issues/4141).
- **Types :** Ajout et mise à jour des types pour les différents documents et champs (nature d'exploitation, actionnaire, dispositif de stockage, etc.).
- **CI/CD :** Désactivation de l'envoi d'emails en CI pour éviter des spams lors des tests [#4138](https://github.com/MTES-MCT/potentiel/issues/4138).
- **Suppression de code obsolète :** Suppression de scripts et de types inutilisés.
- **Mises à jour de dépendances :** Mises à jour de plusieurs dépendances (dompurify, picomatch, basic-ftp).

### Autres changements
- **Documentation :** Mise à jour des données de test [#4181](https://github.com/MTES-MCT/potentiel/issues/4181).
- **Configuration :** Ajout du dépôt dans la projection des Garanties Financières [#4156](https://github.com/MTES-MCT/potentiel/issues/4156).
- **Correction de bugs :** Correction de plusieurs bugs mineurs liés à l'importation de données, la modification de documents et l'affichage de l'interface utilisateur.
- **Amélioration de la gestion des erreurs :** Explicitation du type d'erreur pour l'affichage des messages d'erreur [#4133](https://github.com/MTES-MCT/potentiel/issues/4133).
- **Nettoyage de code :** Diverses corrections et simplifications du code.
