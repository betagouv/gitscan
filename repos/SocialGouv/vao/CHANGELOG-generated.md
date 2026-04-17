## Changelog : vao (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration du parcours de renouvellement d'agrément, avec des correctifs et des nouvelles fonctionnalités pour la gestion des activités, des représentants légaux et de la messagerie. Des améliorations ont également été apportées à l'interface administrateur (BO) pour la gestion des agréments et des utilisateurs, ainsi qu'à la gestion des données via le fusager.

### Évolutions fonctionnelles
- **Agrément :**
    - Ajout de la gestion des messages non lus pour les agréments côté DREETS [#1272](https://github.com/SocialGouv/vao/issues/1272).
    - Implémentation de la messagerie pour les agréments côté DREETS [#1271](https://github.com/SocialGouv/vao/issues/1271).
    - Ajout d'une action pour confirmer la complétude d'un agrément dans le BO [#1236](https://github.com/SocialGouv/vao/issues/1236).
    - Possibilité de changer le statut d'un agrément à "A_MODIFIER" dans le BO [#1227](https://github.com/SocialGouv/vao/issues/1227).
    - Ajout d'un bouton pour refuser un agrément dans le BO [#1245](https://github.com/SocialGouv/vao/issues/1245).
    - Ajout d'onglets pour les documents d'un agrément dans le BO [#1233](https://github.com/SocialGouv/vao/issues/1233).
- **Renouvellement d'agrément :**
    - Correction de plusieurs étapes du processus de renouvellement d'agrément (étape 1, 2, 3, 4) [#1265](https://github.com/SocialGouv/vao/issues/1265), [#1259](https://github.com/SocialGouv/vao/issues/1259), [#1266](https://github.com/SocialGouv/vao/issues/1266), [#1272](https://github.com/SocialGouv/vao/issues/1272).
    - Correction de bugs liés à la récupération des activités dans le cadre du renouvellement [#1265](https://github.com/SocialGouv/vao/issues/1265).
    - Correction de bugs liés aux représentants légaux dans le cadre du renouvellement [#1266](https://github.com/SocialGouv/vao/issues/1266).
- **Fusager :**
    - Ajout de la liste des JDMA au fusager [#1268](https://github.com/SocialGouv/vao/issues/1268).
    - Suppression du menu "renouvellement d'agrément" du fusager [#1269](https://github.com/SocialGouv/vao/issues/1269).
    - Correction d'un bug où le nombre de femmes était indéfini dans le fusager [#1270](https://github.com/SocialGouv/vao/issues/1270).
    - Ajout d'une action pour donner un avis dans le fusager [#1248](https://github.com/SocialGouv/vao/issues/1248).

### Évolutions techniques
- Refactorisation de code en TypeScript dans plusieurs parties du projet, notamment pour la gestion des représentants légaux et l'étape 2 du processus de renouvellement.
- Amélioration de la gestion des requêtes et des données dans le BO.
- Mise en place de fonctions de seed pour la suppression d'organismes dans la base de données PostgreSQL.

### Autres changements
- Mise à jour des pré-commits pour interdire l'utilisation de `console.log` dans le code.
- Nettoyage de code dans `shared-ui`.
- Amélioration des tests E2E pour la suppression d'utilisateurs et les personnes physiques [#1235](https://github.com/SocialGouv/vao/issues/1235), [#1244](https://github.com/SocialGouv/vao/issues/1244).
- Correction de bugs d'affichage de boutons dans le fusager [#1238](https://github.com/SocialGouv/vao/issues/1238).
- Correction d'un bug empêchant le blocage de l'étape suivante dans le fusager [#1237](https://github.com/SocialGouv/vao/issues/1237).
