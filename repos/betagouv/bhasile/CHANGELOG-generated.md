## Changelog : bhasile (30 derniers jours, au 22 avril 2026)

### Résumé
Ce mois-ci, les évolutions de bhasile se concentrent sur l'amélioration de l'expérience utilisateur et de la gestion des données, notamment concernant les CPOM (Contrats de Préstation d'Offre de Maintien) et les structures multi-DNA (Demande d'Asile). Des corrections de bugs et des optimisations de performance ont également été apportées. L'ajout de nouvelles fonctionnalités comme la gestion des opérateurs et l'amélioration des pipelines CI/CD contribuent à une meilleure efficacité du système.

### Évolutions fonctionnelles
- Amélioration de l'affichage des documents financiers [#1181](https://github.com/betagouv/bhasile/issues/1181).
- Ajout d'un modal de confirmation lors de la fermeture d'un formulaire de modification [#1179](https://github.com/betagouv/bhasile/issues/1179).
- Modification du libellé dynamique pour la case à cocher DNA/FINESS [#1175](https://github.com/betagouv/bhasile/issues/1175).
- Réorganisation des colonnes du tableau CPOM [#1174](https://github.com/betagouv/bhasile/issues/1174).
- Ajout de champs de saisie manuelle pour l'adresse administrative [#1167](https://github.com/betagouv/bhasile/issues/1167).
- Limitation des entrées numériques à deux décimales [#1165](https://github.com/betagouv/bhasile/issues/1165).
- Possibilité de rendre les tableaux scrollables [#1164](https://github.com/betagouv/bhasile/issues/1164).
- Ajout d'une page dédiée à la gestion des opérateurs [#1159](https://github.com/betagouv/bhasile/issues/1159) et mise à jour de la page d'accès refusé [#1105](https://github.com/betagouv/bhasile/issues/1105).
- Ajout de la possibilité d'ajouter plusieurs adresses pour un collectif [#1160](https://github.com/betagouv/bhasile/issues/1160).
- Ajout d'une notion de prévisionnel/réalisé pour les indicateurs financiers [#1154](https://github.com/betagouv/bhasile/issues/1154).
- Ajout d'un sélecteur pour le code DNA au lieu d'un champ texte [#1144](https://github.com/betagouv/bhasile/issues/1144).
- Ajout de la recherche par code DNA [#1112](https://github.com/betagouv/bhasile/issues/1112).
- Suppression du panneau d'affectation subventionné [#1111](https://github.com/betagouv/bhasile/issues/1111).
- Ajout de filtres et d'options de tri pour les CPOM [#1095](https://github.com/betagouv/bhasile/issues/1095).
- Amélioration de l'affichage des notes [#1146](https://github.com/betagouv/bhasile/issues/1146).
- Ajout de la gestion des filiales [#1145](https://github.com/betagouv/bhasile/issues/1145).

### Évolutions techniques
- Correction de l'import du référentiel OFII [#1180](https://github.com/betagouv/bhasile/issues/1180).
- Ajout du type `StructureApiRead` [#1176](https://github.com/betagouv/bhasile/issues/1176).
- Amélioration des pipelines CI/CD (plusieurs commits : [#1172](https://github.com/betagouv/bhasile/issues/1172), [#1170](https://github.com/betagouv/bhasile/issues/1170), [#1169](https://github.com/betagouv/bhasile/issues/1169)).
- Déplacement de certains calculs CPOM côté serveur [#1156](https://github.com/betagouv/bhasile/issues/1156).
- Refactorisation du schéma Prisma [#1142](https://github.com/betagouv/bhasile/issues/1142).
- Ajout de la gestion des rôles et des permissions [#1050](https://github.com/betagouv/bhasile/issues/1050).
- Correction d'un problème de z-index entre le tableau et l'en-tête [#1171](https://github.com/betagouv/bhasile/issues/1171).
- Correction de bugs liés aux dates et à la gestion des données multi-DNA (plusieurs commits : [#1103](https://github.com/betagouv/bhasile/issues/1103), [#1100](https://github.com/betagouv/bhasile/issues/1100), [#1099](https://github.com/betagouv/bhasile/issues/1099)).
- Amélioration de la gestion des tests E2E pour les CPOM [#1158](https://github.com/betagouv/bhasile/issues/1158) et ajout de tests pour l'authentification Proconnect [#1131](https://github.com/betagouv/bhasile/issues/1131).

### Autres changements
- Suivi de l'utilisation de l'application [#1177](https://github.com/betagouv/bhasile/issues/1177).
- Correction de typos et améliorations de la documentation [#1163](https://github.com/betagouv/bhasile/issues/1163), [#1123](https://github.com/betagouv/bhasile/issues/1123).
- Correction de problèmes liés à la gestion des régions et des filiales [#1118](https://github.com/betagouv/bhasile/issues/1118), [#1117](https://github.com/betagouv/bhasile/issues/1117), [#1089](https://github.com/betagouv/bhasile/issues/1089).
- Nettoyage de code et suppression de packages inutiles [#1102](https://github.com/betagouv/bhasile/issues/1102).
- Améliorations de l'interface utilisateur et de l'accessibilité [#1108](https://github.com/betagouv/bhasile/issues/1108), [#1094](https://github.com/betagouv/bhasile/issues/1094).
