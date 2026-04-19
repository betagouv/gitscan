## Changelog : bhasile (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, les évolutions de bhasile se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de la gestion des CPOM, des structures et des données financières. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des améliorations de la sécurité et de l'infrastructure. L'ajout de nouvelles fonctionnalités comme la gestion des opérateurs et la recherche avancée contribuent à rendre l'outil plus puissant et flexible.

### Évolutions fonctionnelles
- Possibilité de saisir manuellement l'adresse administrative. [#1167](https://github.com/betagouv/bhasile/issues/1167)
- Ajout d'une page dédiée à la gestion des opérateurs et de leur description. [#1168](https://github.com/betagouv/bhasile/issues/1168) et [#1159](https://github.com/betagouv/bhasile/issues/1159)
- Amélioration de la recherche et du filtrage des CPOM, avec ajout d'options de tri. [#1095](https://github.com/betagouv/bhasile/issues/1095)
- Ajout d'une notion de prévisionnel/réalisé pour les indicateurs financiers. [#1154](https://github.com/betagouv/bhasile/issues/1154)
- Possibilité d'ajouter plusieurs adresses pour un collectif. [#1160](https://github.com/betagouv/bhasile/issues/1160)
- Ajout d'un sélecteur pour le code DNA au lieu d'un champ texte. [#1144](https://github.com/betagouv/bhasile/issues/1144)
- Amélioration de la gestion des filiales avec ajout de données de base. [#1145](https://github.com/betagouv/bhasile/issues/1145), [#1147](https://github.com/betagouv/bhasile/issues/1147) et [#1078](https://github.com/betagouv/bhasile/issues/1078)
- Ajout de notes. [#1146](https://github.com/betagouv/bhasile/issues/1146)
- Ajout d'une recherche par code DNA. [#1112](https://github.com/betagouv/bhasile/issues/1112)
- Nouvelle formulation pour l'affectation. [#1083](https://github.com/betagouv/bhasile/issues/1083)
- Une seule politique de contact. [#1082](https://github.com/betagouv/bhasile/issues/1082)

### Évolutions techniques
- Amélioration des performances du pipeline CI/CD. [#1172](https://github.com/betagouv/bhasile/issues/1172), [#1170](https://github.com/betagouv/bhasile/issues/1170) et [#1169](https://github.com/betagouv/bhasile/issues/1169)
- Refactoring du schéma Prisma. [#1142](https://github.com/betagouv/bhasile/issues/1142)
- Mise à jour de plusieurs dépendances (Hono, Next.js, etc.).
- Amélioration de la gestion des dates et des types de données.
- Optimisation des tests E2E pour les CPOM. [#1158](https://github.com/betagouv/bhasile/issues/1158) et [#1131](https://github.com/betagouv/bhasile/issues/1131)
- Amélioration de la structure des tables financières pour chaque type de structure. [#1130](https://github.com/betagouv/bhasile/issues/1130)
- Mise en place de tests unitaires pour les utilitaires de date. [#1135](https://github.com/betagouv/bhasile/issues/1135)
- Suppression de champs inutiles et nettoyage du code.
- Mise à jour des tailles des conteneurs cron. [#1069](https://github.com/betagouv/bhasile/issues/1069)
- Ajout de scripts pour la gestion des buckets S3. [#1084](https://github.com/betagouv/bhasile/issues/1084)

### Autres changements
- Correction du problème de z-index des tableaux par rapport à l'en-tête. [#1171](https://github.com/betagouv/bhasile/issues/1171)
- Correction de typos dans les tables de budget. [#1163](https://github.com/betagouv/bhasile/issues/1163)
- Autorisation de valeurs nulles pour la description du DNA. [#1162](https://github.com/betagouv/bhasile/issues/1162)
- Limitation des entrées numériques à deux décimales. [#1165](https://github.com/betagouv/bhasile/issues/1165)
- Amélioration de l'accessibilité et du design de l'interface utilisateur. [#1108](https://github.com/betagouv/bhasile/issues/1108) et [#1094](https://github.com/betagouv/bhasile/issues/1094)
- Centrage des colonnes dans les tableaux. [#1157](https://github.com/betagouv/bhasile/issues/1157)
- Correction de problèmes liés aux retours multi-DNA. [#1103](https://github.com/betagouv/bhasile/issues/1103), [#1100](https://github.com/betagouv/bhasile/issues/1100) et [#1098](https://github.com/betagouv/bhasile/issues/1098)
- Correction de bugs dans les scripts de seed. [#1120](https://github.com/betagouv/bhasile/issues/1120), [#1119](https://github.com/betagouv/bhasile/issues/1119) et [#1073](https://github.com/betagouv/bhasile/issues/1073)
- Amélioration de la gestion des dates et des fuseaux horaires. [#1136](https://github.com/betagouv/bhasile/issues/1136) et [#1128](https://github.com/betagouv/bhasile/issues/1128)
- Ajout de rôles et de permissions. [#1050](https://github.com/betagouv/bhasile/issues/1050)
- Mise à jour des accès refusés. [#1105](https://github.com/betagouv/bhasile/issues/1105)
