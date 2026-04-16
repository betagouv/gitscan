## Changelog : bhasile (30 derniers jours, au 15 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la gestion des CPOM (Contrats de Préstation d'Objectifs et de Moyens), notamment avec une nouvelle interface et des fonctionnalités de filtrage et d'édition. Des améliorations ont également été apportées à la gestion des structures, des utilisateurs et des rôles, ainsi qu'à la correction de bugs et à l'optimisation de la base de données.

### Évolutions fonctionnelles
- Possibilité de saisir plusieurs adresses pour un collectif ([#1160](https://github.com/betagouv/bhasile/issues/1160)).
- Ajout d'une page pour gérer les opérateurs ([#1148](https://github.com/betagouv/bhasile/issues/1148)).
- Amélioration de l'accès refusé avec un message plus clair ([#1105](https://github.com/betagouv/bhasile/issues/1105)).
- Ajout d'un sélecteur pour le code DNA au lieu d'une saisie texte ([#1144](https://github.com/betagouv/bhasile/issues/1144)).
- Ajout de notes pour les structures ([#1146](https://github.com/betagouv/bhasile/issues/1146)).
- Ajout des filiales dans la base de données ([#1145](https://github.com/betagouv/bhasile/issues/1145)).
- Nouvelle table pour les finances CPOM, spécifique au type de structure ([#1130](https://github.com/betagouv/bhasile/issues/1130)).
- Ajout d'une notion de prévisionnel/réalisé pour les indicateurs financiers ([#1154](https://github.com/betagouv/bhasile/issues/1154)).
- Modification du titre des documents financiers ([#1155](https://github.com/betagouv/bhasile/issues/1155)).
- Ajout de la recherche par code DNA ([#1112](https://github.com/betagouv/bhasile/issues/1112)).
- Nouvelle affectation wording ([#1083](https://github.com/betagouv/bhasile/issues/1083)).
- Nouvelle politique d'un seul contact ([#1082](https://github.com/betagouv/bhasile/issues/1082)).
- Nouvelle page et formulaires de modification CPOM ([#1063](https://github.com/betagouv/bhasile/issues/1063)).
- Ajout d'une colonne structures à la table CPOM ([#1071](https://github.com/betagouv/bhasile/issues/1071)).
- Nouveau format pour les noms des CPOM ([#1070](https://github.com/betagouv/bhasile/issues/1070)).
- Ajout de rôles et permissions ([#1050](https://github.com/betagouv/bhasile/issues/1050)).
- Amélioration du design et de l'accessibilité ([#1108](https://github.com/betagouv/bhasile/issues/1108)).

### Évolutions techniques
- Centrage des colonnes dans les tableaux.
- Refactoring du schéma Prisma ([#1142](https://github.com/betagouv/bhasile/issues/1142)).
- Suppression de champs inutiles dans UserAction.
- Amélioration de la gestion des dates (format 00:00:00).
- Ajout de tests E2E pour la modification des CPOM ([#1158](https://github.com/betagouv/bhasile/issues/1158)).
- Ajout de tests unitaires pour date.util ([#1135](https://github.com/betagouv/bhasile/issues/1135)).
- Optimisation des scripts de seed.
- Mise à jour de plusieurs dépendances (Next.js, fast-xml-parser, etc.).

### Autres changements
- Ajout de notes pour les structures.
- Correction de bugs liés aux dates et aux filtres.
- Amélioration des scripts de migration et de remplissage de la base de données.
- Nettoyage du code et suppression de packages inutiles.
- Ajout de scripts pour gérer les buckets S3.
- Correction de typos et amélioration de la lisibilité du code.
- Ajout d'un bouton de suppression.
- Amélioration des vues.
- Normalisation des dates.
- Ajout de code FINESS.
- Suppression de la colonne "subventionné" dans l'affectation.
