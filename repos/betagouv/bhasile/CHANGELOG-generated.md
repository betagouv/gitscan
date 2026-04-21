## Changelog : bhasile (30 derniers jours, au 20 avril 2026)

### Résumé
Ce mois-ci, les évolutions de bhasile se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de la gestion des CPOM (Contrat de Préstation d'Hébergement et d'Accompagnement Social), des structures et des données financières. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des améliorations de la sécurité et de l'infrastructure.

### Évolutions fonctionnelles
- Possibilité de saisir manuellement l'adresse administrative. [#1167](https://github.com/betagouv/bhasile/issues/1167)
- Ajout de la possibilité de modifier la description d'un opérateur. [#1168](https://github.com/betagouv/bhasile/issues/1168)
- Amélioration de la gestion des filiales avec ajout de données de test. [#1147](https://github.com/betagouv/bhasile/issues/1147)
- Ajout d'une notion de prévisionnel/réalisé pour les indicateurs financiers. [#1154](https://github.com/betagouv/bhasile/issues/1154)
- Possibilité d'ajouter plusieurs adresses pour un collectif. [#1160](https://github.com/betagouv/bhasile/issues/1160)
- Ajout d'un code de recherche ADN. [#1112](https://github.com/betagouv/bhasile/issues/1112)
- Amélioration de la gestion des retours multi-ADN pour les agents, CPOM et l'ajout de structures. [#1103](https://github.com/betagouv/bhasile/issues/1103), [#1100](https://github.com/betagouv/bhasile/issues/1100), [#1098](https://github.com/betagouv/bhasile/issues/1098)
- Ajout d'une page dédiée aux opérateurs. [#1148](https://github.com/betagouv/bhasile/issues/1148) et [#1159](https://github.com/betagouv/bhasile/issues/1159)
- Amélioration de la recherche et du filtrage des CPOM. [#1095](https://github.com/betagouv/bhasile/issues/1095)
- Ajout de la possibilité de modifier les CPOM. [#1130](https://github.com/betagouv/bhasile/issues/1130)
- Amélioration de l'affichage des colonnes dans les tableaux (centrage). [#1157](https://github.com/betagouv/bhasile/issues/1157)
- Ajout de notes. [#1146](https://github.com/betagouv/bhasile/issues/1146)

### Évolutions techniques
- Amélioration de la performance du pipeline. [#1172](https://github.com/betagouv/bhasile/issues/1172), [#1170](https://github.com/betagouv/bhasile/issues/1170), [#1169](https://github.com/betagouv/bhasile/issues/1169)
- Refactoring du schéma Prisma. [#1142](https://github.com/betagouv/bhasile/issues/1142)
- Mise à jour de plusieurs dépendances (Hono, Next.js, etc.).
- Amélioration de la gestion des dates (formatage, tests). [#1135](https://github.com/betagouv/bhasile/issues/1135) et [#1129](https://github.com/betagouv/bhasile/issues/1129)
- Ajout de tests E2E pour la modification des CPOM. [#1158](https://github.com/betagouv/bhasile/issues/1158)
- Amélioration de la gestion des accès et des permissions (rôles). [#1050](https://github.com/betagouv/bhasile/issues/1050) et [#1105](https://github.com/betagouv/bhasile/issues/1105)

### Autres changements
- Correction de bugs d'affichage (z-index, couleurs, typographie). [#1171](https://github.com/betagouv/bhasile/issues/1171), [#1166](https://github.com/betagouv/bhasile/issues/1166), [#1165](https://github.com/betagouv/bhasile/issues/1165), [#1163](https://github.com/betagouv/bhasile/issues/1163), [#1115](https://github.com/betagouv/bhasile/issues/1115)
- Correction de bugs liés à la gestion des données (ADN, périmètre, filiales). [#1162](https://github.com/betagouv/bhasile/issues/1162), [#1126](https://github.com/betagouv/bhasile/issues/1126), [#1127](https://github.com/betagouv/bhasile/issues/1127), [#1117](https://github.com/betagouv/bhasile/issues/1117)
- Amélioration de la documentation et des messages d'erreur.
- Nettoyage du code et suppression de dépendances inutiles.
- Correction de problèmes liés aux seeders (données de test). [#1120](https://github.com/betagouv/bhasile/issues/1120), [#1119](https://github.com/betagouv/bhasile/issues/1119), [#1118](https://github.com/betagouv/bhasile/issues/1118), [#1113](https://github.com/betagouv/bhasile/issues/1113)
- Ajout de scripts pour la gestion des buckets S3 et des accès. [#1143](https://github.com/betagouv/bhasile/issues/1143) et [#1142](https://github.com/betagouv/bhasile/issues/1142)
