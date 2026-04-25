## Changelog : bhasile (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, les évolutions de bhasile se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de la recherche et de la gestion des structures et des CPOM (Contrat de Plan d'Accompagnement vers l'Autonomie). Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des améliorations de la sécurité et de la gestion des accès. L'importation des données OFII a été revue et améliorée.

### Évolutions fonctionnelles
- **Recherche et filtrage :**
    - Ajout de la recherche par code DNA. [#1112](https://github.com/betagouv/bhasile/issues/1112)
    - Amélioration du filtrage et de l'ordonnancement des CPOM. [#1095](https://github.com/betagouv/bhasile/issues/1095)
    - Ajout de la recherche d'opérateur. [#1182](https://github.com/betagouv/bhasile/issues/1182)
    - Correction du problème d'affichage du loader lors de la recherche. [#1195](https://github.com/betagouv/bhasile/issues/1195)
- **Gestion des structures :**
    - Possibilité de saisir manuellement l'adresse administrative. [#1167](https://github.com/betagouv/bhasile/issues/1167)
    - Amélioration de la gestion des adresses des collectifs (possibilité de saisir plusieurs adresses). [#1160](https://github.com/betagouv/bhasile/issues/1160)
    - Correction de l'accès aux pages CPOM. [#1126](https://github.com/betagouv/bhasile/issues/1126)
    - Correction de la recherche de structure. [#1127](https://github.com/betagouv/bhasile/issues/1127)
- **Gestion des CPOM :**
    - Ajout d'une notion de prévisionnel/réalisé pour les indicateurs financiers. [#1154](https://github.com/betagouv/bhasile/issues/1154)
    - Un seul tableau financier par type de structure. [#1130](https://github.com/betagouv/bhasile/issues/1130)
    - Amélioration de l'affichage des documents financiers. [#1181](https://github.com/betagouv/bhasile/issues/1181)
- **Gestion des utilisateurs et accès :**
    - Ajout de la gestion des rôles et des permissions. [#1050](https://github.com/betagouv/bhasile/issues/1050)
    - Amélioration de la gestion des accès refusés. [#1105](https://github.com/betagouv/bhasile/issues/1105)
- **Import OFII :**
    - Amélioration du script d'importation des données OFII pour les structures avec plusieurs DNA. [#1139](https://github.com/betagouv/bhasile/issues/1139), [#1093](https://github.com/betagouv/bhasile/issues/1093)
    - Correction des retours multi DNA pour les agents. [#1103](https://github.com/betagouv/bhasile/issues/1103)

### Évolutions techniques
- **Tests :**
    - Ajout de nouveaux types de tests. [#1178](https://github.com/betagouv/bhasile/issues/1178)
    - Ajout de tests E2E pour la finalisation du formulaire. [#1197](https://github.com/betagouv/bhasile/issues/1197)
    - Ajout de tests E2E pour les CPOM. [#1158](https://github.com/betagouv/bhasile/issues/1158)
    - Ajout de tests unitaires pour les utilitaires de date. [#1135](https://github.com/betagouv/bhasile/issues/1135)
- **Architecture et performance :**
    - Déplacement de la logique de détermination de `isSubventionee` et `isAutorisee` côté serveur. [#1188](https://github.com/betagouv/bhasile/issues/1188)
    - Optimisation de la pipeline CI/CD. [#1172](https://github.com/betagouv/bhasile/issues/1172), [#1170](https://github.com/betagouv/bhasile/issues/1170), [#1169](https://github.com/betagouv/bhasile/issues/1169)
    - Suppression de dépendances inutiles. [#1191](https://github.com/betagouv/bhasile/issues/1191)
    - Refactorisation du schéma Prisma. [#1142](https://github.com/betagouv/bhasile/issues/1142)
- **Divers :**
    - Mise à jour des dépendances. (Ignoré, mises à jour de routine)

### Autres changements
- Ajout d'un modal de confirmation lors de la modification d'un formulaire. [#1179](https://github.com/betagouv/bhasile/issues/1179)
- Ajout du suivi de l'utilisation de l'application. [#1177](https://github.com/betagouv/bhasile/issues/1177)
- Amélioration de la présentation des colonnes dans les tableaux. [#1174](https://github.com/betagouv/bhasile/issues/1174), [#1157](https://github.com/betagouv/bhasile/issues/1157)
- Correction de problèmes de z-index dans les tableaux. [#1171](https://github.com/betagouv/bhasile/issues/1171)
- Amélioration de l'accessibilité et du design. [#1108](https://github.com/betagouv/bhasile/issues/1108)
- Ajout de notes. [#1146](https://github.com/betagouv/bhasile/issues/1146)
- Normalisation des dates. [#1136](https://github.com/betagouv/bhasile/issues/1136)
- Suppression du champ `updatedAt` pour `UserAction`. [#1128](https://github.com/betagouv/bhasile/issues/1128)
- Ajout de filiales dans la base de données. [#1145](https://github.com/betagouv/bhasile/issues/1145)
- Ajout de seeders pour les utilisateurs autorisés. [#1078](https://github.com/betagouv/bhasile/issues/1078)
- Correction de typos et amélioration de la lisibilité du code.
