## Changelog : maestro (30 derniers jours, au 24 septembre 2026)

### Résumé
Ce mois-ci, Maestro a franchi une étape importante dans la finesse de sa configuration grâce à une refonte majeure du module de paramétrage (gestion des plans, des sous-plans et des échantillons). Les droits d'accès ont été affinés pour mieux répondre aux besoins des coordinateurs nationaux et régionaux, et l'outil de communication a migré vers Tchap.

### Évolutions fonctionnelles

**Paramétrage et gestion métier**
- Mise en place de la duplication pour les domaines, plans et sous-plans [#1550](https://github.com/betagouv/maestro/issues/1550).
- Amélioration de la gestion des échantillons : possibilité de configurer plusieurs analytes par échantillon [#1513](https://github.com/betagouv/maestro/issues/1513), paramétrage des analytes [#1476](https://github.com/betagouv/maestro/issues/1476) et calcul automatique des exemplaires via le paramétrage [#1524](https://github.com/betagouv/maestro/issues/1524).
- Introduction de nouveaux concepts de gestion : notion de propriétaire [#1453](https://github.com/betagouv/maestro/issues/1453), gestion de la surcharge entre plans et sous-plans [#1412](https://github.com/betagouv/maestro/issues/1412), et gestion de l'état "Terminer" [#1441](https://github.com/betagouv/maestro/issues/1441).
- Optimisation de l'organisation : paramétrage des sous-plans [#1399](https://github.com/betagouv/maestro/issues/1399), suppression facilitée des éléments non terminés [#1475](https://github.com/betagouv/maestro/issues/1475) et simplification de l'interface des domaines [#1387](https://github.com/betagouv/maestro/issues/1387).
- L'année devient optionnelle dans la gestion des ressources [#1540](https://github.com/betagouv/maestro/issues/1540).

**Utilisateurs et permissions**
- Élargissement des droits : les coordinateurs nationaux peuvent désormais voir tous les domaines [#1462](https://github.com/betagouv/maestro/issues/1462) et accéder en lecture seule au dictionnaire des descripteurs [#1536](https://github.com/betagouv/maestro/issues/1536).
- Amélioration de la visibilité : les coordinateurs régionaux peuvent désormais consulter les commentaires de la coordination nationale [#1452](https://github.com/betagouv/maestro/issues/1452).
- Corrections d'accès pour les prélèveurs [#1502](https://github.com/betagouv/maestro/issues/1502) et les coordinateurs nationaux [#1535](https://github.com/betagouv/maestro/issues/1535).
- Ajout de fonctionnalités dédiées au support utilisateur [#1538](https://github.com/betagouv/maestro/issues/1538).

**Programmation, prélèvements et alertes**
- Ajout d'un module de suivi de la programmation [#1221](https://github.com/betagouv/maestro/issues/1221).
- Amélioration du processus de prélèvement : modification de la localisation possible à l'étape 4 [#1414](https://github.com/betagouv/maestro/issues/1414) et correction de la suppression d'un prélèvement à envoyer [#1454](https://github.com/betagouv/maestro/issues/1454).
- Optimisation des alertes (corrections en PPV [#1474](https://github.com/betagouv/maestro/issues/1474)) et ajout de notifications via une boîte email institutionnelle [#1388](https://github.com/betagouv/maestro/issues/1388).

**Expérience utilisateur et autres**
- Migration de l'outil de communication de Mattermost vers Tchap [#1430](https://github.com/betagouv/maestro/issues/1430).
- Améliorations de l'interface : ajout d'un bouton "haut de page" [#1539](https://github.com/betagouv/maestro/issues/1539), tri des sous-plans par numéro [#1537](https://github.com/betagouv/maestro/issues/1537) et correction de la recherche des entreprises [#1473](https://github.com/betagouv/maestro/issues/1473).
- Correction des statistiques de prélèvements non conformes sur le tableau de bord [#1384](https://github.com/betagouv/maestro/issues/1384).

### Évolutions techniques

**Refactoring et maintenance**
- Nettoyage du code lié à la gestion du mode hors-ligne pour les prélèvements [#1523](https://github.com/betagouv/maestro/issues/1523) et suppression de code mort dans la programmation [#1522](https://github.com/betagouv/maestro/issues/1522).
- Correction des types de routes lors du processus de build.
- Amélioration de la robustesse du script de sauvegarde (backup) [#1386](https://github.com/betagouv/maestro/issues/1386).

### Autres changements
- Passage du projet sous licence MIT [#1489](https://github.com/betagouv/maestro/issues/1489).
