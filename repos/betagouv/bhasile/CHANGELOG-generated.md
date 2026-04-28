## Changelog : bhasile (30 derniers jours, au 27 avril 2026)

### Résumé
Ce mois-ci, les évolutions de bhasile se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de la recherche et de la gestion des structures et des CPOM. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des améliorations de la sécurité et de la gestion des accès. L'ajout de nouvelles fonctionnalités comme la gestion des opérateurs et l'amélioration des filtres renforcent les capacités de l'outil.

### Évolutions fonctionnelles
- Ajout de la recherche d'opérateurs et d'une page dédiée à leur gestion [#1182](https://github.com/betagouv/bhasile/issues/1182) et [#1159](https://github.com/betagouv/bhasile/issues/1159).
- Possibilité de saisir manuellement l'adresse administrative d'une structure [#1167](https://github.com/betagouv/bhasile/issues/1167).
- Amélioration de la recherche de structures avec la possibilité de rechercher par code DNA [#1112](https://github.com/betagouv/bhasile/issues/1112).
- Ajout de filtres et d'options de tri pour les CPOM [#1095](https://github.com/betagouv/bhasile/issues/1095).
- Ajout d'un modal de confirmation lors de la suppression d'un formulaire de finalisation [#1197](https://github.com/betagouv/bhasile/issues/1197).
- Amélioration de l'affichage des documents financiers [#1181](https://github.com/betagouv/bhasile/issues/1181).
- Ajout d'indicateurs de prévisionnel/réalisé pour les indicateurs financiers [#1154](https://github.com/betagouv/bhasile/issues/1154).
- Amélioration de l'affichage des colonnes dans le tableau CPOM [#1174](https://github.com/betagouv/bhasile/issues/1174).
- Ajout de notes [#1146](https://github.com/betagouv/bhasile/issues/1146).
- Amélioration de la gestion des filiales [#1147](https://github.com/betagouv/bhasile/issues/1147) et [#1145](https://github.com/betagouv/bhasile/issues/1145).
- Ajout d'un sélecteur pour le code DNA au lieu d'un champ texte [#1144](https://github.com/betagouv/bhasile/issues/1144).

### Évolutions techniques
- Ajout de tests pour le dépôt de structures [#1202](https://github.com/betagouv/bhasile/issues/1202) et pour les tests de formulaire de finalisation [#1197](https://github.com/betagouv/bhasile/issues/1197).
- Refactorisation du code pour déplacer certaines logiques côté serveur (isSubventionee/isAutorisee) [#1188](https://github.com/betagouv/bhasile/issues/1188).
- Amélioration de la performance des pipelines CI/CD [#1172](https://github.com/betagouv/bhasile/issues/1172), [#1170](https://github.com/betagouv/bhasile/issues/1170) et [#1169](https://github.com/betagouv/bhasile/issues/1169).
- Séparation du schéma Prisma [#1142](https://github.com/betagouv/bhasile/issues/1142).
- Mise en place de rôles et permissions [#1050](https://github.com/betagouv/bhasile/issues/1050).
- Amélioration de la gestion des dates et des timezones [#1129](https://github.com/betagouv/bhasile/issues/1129).
- Correction de problèmes de z-index pour l'affichage des tables et des headers [#1171](https://github.com/betagouv/bhasile/issues/1171).
- Amélioration de la gestion des erreurs et des validations avec Zod.

### Autres changements
- Correction de bugs divers liés à l'affichage, aux filtres et à la gestion des données [#1195](https://github.com/betagouv/bhasile/issues/1195), [#1194](https://github.com/betagouv/bhasile/issues/1194), [#1193](https://github.com/betagouv/bhasile/issues/1193), [#1190](https://github.com/betagouv/bhasile/issues/1190), [#1186](https://github.com/betagouv/bhasile/issues/1186), [#1166](https://github.com/betagouv/bhasile/issues/1166), [#1165](https://github.com/betagouv/bhasile/issues/1165), [#1163](https://github.com/betagouv/bhasile/issues/1163), [#1162](https://github.com/betagouv/bhasile/issues/1162), [#1127](https://github.com/betagouv/bhasile/issues/1127), [#1126](https://github.com/betagouv/bhasile/issues/1126), [#1123](https://github.com/betagouv/bhasile/issues/1123), [#1122](https://github.com/betagouv/bhasile/issues/1122), [#1115](https://github.com/betagouv/bhasile/issues/1115), [#1114](https://github.com/betagouv/bhasile/issues/1114), [#1113](https://github.com/betagouv/bhasile/issues/1113), [#1111](https://github.com/betagouv/bhasile/issues/1111), [#1109](https://github.com/betagouv/bhasile/issues/1109), [#1107](https://github.com/betagouv/bhasile/issues/1107), [#1093](https://github.com/betagouv/bhasile/issues/1093), [#1092](https://github.com/betagouv/bhasile/issues/1092), [#1091](https://github.com/betagouv/bhasile/issues/1091), [#1089](https://github.com/betagouv/bhasile/issues/1089), [#1078](https://github.com/betagouv/bhasile/issues/1078), [#1073](https://github.com/betagouv/bhasile/issues/1073).
- Amélioration de l'accessibilité et du design [#1108](https://github.com/betagouv/bhasile/issues/1108).
- Mise à jour des dépendances.
