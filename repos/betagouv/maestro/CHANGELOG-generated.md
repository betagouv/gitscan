## Changelog : maestro (30 derniers jours, au 01/10/2026)

### Résumé
Ce mois-ci, la plateforme Maestro a connu une évolution majeure de son module de paramétrage, offrant une gestion beaucoup plus fine des plans, des sous-plans et des matrices. Les droits d'accès ont également été affinés pour mieux répondre aux besoins des différents profils d'utilisateurs (nationaux, régionaux, départementaux), tout en améliorant la fluidité de la programmation et du suivi des activités.

### Évolutions fonctionnelles

**Paramétrage et configuration**
- Gestion avancée des matrices au niveau des plans ([#1590](https://github.com/betagouv/maestro/issues/1590), [#1582](https://github.com/betagouv/maestro/issues/1582), [#1568](https://github.com/betagouv/maestro/issues/1568)).
- Possibilité de dupliquer des domaines, des plans ou des sous-plans ([#1550](https://github.com/betagouv/maestro/issues/1550)).
- Amélioration de la gestion des échantillons : configuration des analytes (possibilité de mettre plusieurs analytes par échantillon) et calcul automatique via le paramétrage ([#1524](https://github.com/betagouv/maestro/issues/1524), [#1513](https://github.com/betagouv/maestro/issues/1513), [#1484](https://github.com/betagouv/maestro/issues/1484)).
- Nouvelles options de gestion : modification des titres de plans ([#1583](https://github.com/betagouv/maestro/issues/1583)), ajout d'IT direct sur le plan ([#1541](https://github.com/betagouv/maestro/issues/1541)), notion de propriétaire ([#1453](https://github.com/betagouv/maestro/issues/1453)), gestion de l'état "Terminer" ([#1441](https://github.com/betagouv/maestro/issues/1441)) et notion de surcharge entre plan et sous-plans ([#1412](https://github.com/betagouv/maestro/issues/1412)).
- Suppression sécurisée des domaines, plans et sous-plans non terminés ([#1475](https://github.com/betagouv/maestro/issues/1475)).
- Flexibilité accrue sur les ressources (l'année est désormais optionnelle) et les descripteurs (ajout d'un type date) ([#1540](https://github.com/betagouv/maestro/issues/1540), [#1491](https://github.com/betagouv/maestro/issues/1491)).

**Programmation et suivi**
- Introduction d'une fonctionnalité de suivi des activités ([#1221](https://github.com/betagouv/maestro/issues/1221)).
- Ouverture des droits d'importation de la programmation aux coordinateurs régionaux et départementaux ([#1578](https://github.com/betagouv/maestro/issues/1578)).
- Améliorations de l'interface utilisateur : ajout d'un bouton de retour en haut de page ([#1539](https://github.com/betagouv/maestro/issues/1539)) et tri des sous-plans par numéro ([#1537](https://github.com/betagouv/maestro/issues/1537)).

**Gestion des accès et utilisateurs**
- Élargissement des droits des coordinateurs nationaux : accès en lecture seule au dictionnaire des descripteurs ([#1536](https://github.com/betagouv/maestro/issues/1536)) et visibilité de tous les domaines ([#1462](https://github.com/betagouv/maestro/issues/1462)).
- Meilleure visibilité des commentaires nationaux pour les coordinateurs régionaux ([#1452](https://github.com/betagouv/maestro/issues/1452)).
- Ajout de fonctionnalités dédiées au support utilisateur ([#1538](https://github.com/betagouv/maestro/issues/1538)).

**Divers**
- Migration de la messagerie de Mattermost vers Tchap ([#1430](https://github.com/betagouv/maestro/issues/1430)).
- Corrections de bugs : recherche d'entreprises ([#1473](https://github.com/betagouv/maestro/issues/1473)), émetteur des emails automatiques ([#1567](https://github.com/betagouv/maestro/issues/1567)) et modification de la localisation des prélèvements ([#1414](https://github.com/betagouv/maestro/issues/1414)).

### Évolutions techniques

**Architecture et Refactoring**
- Restructuration du module PPV en sous-plans ([#1512](https://github.com/betagouv/maestro/issues/1512)).
- Déplacement des matrices de prescription vers les sous-plans ([#1580](https://github.com/betagouv/maestro/issues/1580)).
- Nettoyage du code : suppression de la gestion du mode offline ([#1523](https://github.com/betagouv/maestro/issues/1523)) et du code mort dans la partie programmation ([#1522](https://github.com/betagouv/maestro/issues/1522)).
- Refactoring des étapes (stages) ([#1566](https://github.com/betagouv/maestro/issues/1566)).

**Base de données et Infrastructure**
- Optimisation de la table des prescriptions via l'ajout de contraintes et la suppression de colonnes obsolètes ([#1577](https://github.com/betagouv/maestro/issues/1577)).
- Correction de migrations de base de données.

**Qualité et Build**
- Corrections de types pour les routes et amélioration de la stabilité des tests ([#1589](https://github.com/betagouv/maestro/issues/1589)).

### Autres changements
- Passage du projet sous licence MIT ([#1489](https://github.com/betagouv/maestro/issues/1489)).
