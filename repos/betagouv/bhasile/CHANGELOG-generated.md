## Changelog : bhasile (30 derniers jours, au 17 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la refonte et l'amélioration du module de transformation des structures d'hébergement. Les utilisateurs bénéficieront de nouveaux formulaires, d'une navigation plus fluide et d'une meilleure gestion des informations liées aux transformations. Des améliorations ont également été apportées aux statistiques, à l'interface utilisateur et à la gestion des documents.

### Évolutions fonctionnelles
- Ajout de la possibilité de créer des structures à partir de formulaires de transformation ([#1371](https://github.com/betagouv/bhasile/issues/1371)).
- Amélioration de l'affichage des champs DNA et FINESS lors de la création de structures à partir de transformations.
- Ajout de la validation de la date de création, désormais obligatoire ([#1373](https://github.com/betagouv/bhasile/issues/1373)).
- Correction de l'affichage des documents lors de la création de structures ([#1372](https://github.com/betagouv/bhasile/issues/1372)).
- Ajout de liens de retour sur les formulaires de transformation ([#1368](https://github.com/betagouv/bhasile/issues/1368)).
- Affichage de la carte de la structure même en phase de création ([#1367](https://github.com/betagouv/bhasile/issues/1367)).
- Ajout de structures finalisées pour les tests ([#1369](https://github.com/betagouv/bhasile/issues/1369)).
- Possibilité de naviguer dans les formulaires de transformation sans les compléter ([#1352](https://github.com/betagouv/bhasile/issues/1352)).
- Ajout d'une extension spécifique pour les actes administratifs HUDA CADA ([#1345](https://github.com/betagouv/bhasile/issues/1345)).
- Possibilité d'ajouter des avenants aux transformations ([#1330](https://github.com/betagouv/bhasile/issues/1330)).
- Ajout d'un affichage spécifique pour les DNA et FINESS dans les formulaires de transformation ([#1342](https://github.com/betagouv/bhasile/issues/1342)).
- Validation des formulaires de structureTransformation ([#1348](https://github.com/betagouv/bhasile/issues/1348)).
- Ajout de statistiques sur les types de places ([#1361](https://github.com/betagouv/bhasile/issues/1361)).
- Ajout d'un indicateur d'impact ([#1360](https://github.com/betagouv/bhasile/issues/1360)).
- Ajout d'un bloc d'activité avec des informations sur les actions des utilisateurs ([#1262](https://github.com/betagouv/bhasile/issues/1262)).
- Ajout d'un CTA pour accéder aux statistiques ([#1326](https://github.com/betagouv/bhasile/issues/1326)).
- Amélioration de l'affichage des filiales ([#1317](https://github.com/betagouv/bhasile/issues/1317)).
- Ajout de contacts pour les opérateurs ([#1286](https://github.com/betagouv/bhasile/issues/1286)).
- Ajout du logo des opérateurs ([#1275](https://github.com/betagouv/bhasile/issues/1275)).

### Évolutions techniques
- Refonte de la gestion des transformations, incluant la création de nouvelles routes et la migration des données ([#1258](https://github.com/betagouv/bhasile/issues/1258)).
- Amélioration de la performance en mettant en cache les données de `.next/cache` et en optimisant le déploiement sur Scalingo ([#1303](https://github.com/betagouv/bhasile/issues/1303)).
- Refactoring du repository de transformation ([#1370](https://github.com/betagouv/bhasile/issues/1370)).
- Ajout de tests E2E pour les nouvelles fonctionnalités ([#1325](https://github.com/betagouv/bhasile/issues/1325)).
- Migration des fichiers de migration obsolètes liés aux transformations.
- Utilisation de `getStructureDefaultValues` côté serveur pour améliorer la performance.
- Correction de bugs liés à la validation des adresses et à la navigation dans les formulaires.
- Amélioration de l'accessibilité (a11y) de l'application ([#1308](https://github.com/betagouv/bhasile/issues/1308)).

### Autres changements
- Ajout de documentation pour Dependabot ([#1322](https://github.com/betagouv/bhasile/issues/1322)).
- Ajout de types de documentation ([#1305](https://github.com/betagouv/bhasile/issues/1305)).
- Nettoyage du code et suppression de code mort.
- Correction de problèmes de style et d'affichage.
- Mise à jour de certaines dépendances (Hono, tmp, esbuild, etc.).
