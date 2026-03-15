## Changelog : bhasile (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à bhasile au cours des 30 derniers jours. Les mises à jour incluent des corrections de bugs, des améliorations de l'interface utilisateur, l'ajout de nouvelles fonctionnalités comme un journal d'audit, et des optimisations techniques pour une meilleure performance et sécurité. L'application a également été préparée pour l'année 2026 avec des ajustements des données et des typologies.

### Évolutions fonctionnelles
- Ajout d'un message d'alerte lors de l'ajout d'un avenant orphelin [#1062](https://github.com/betagouv/bhasile/issues/1062).
- Amélioration de la navigation : les filtres de structures sont conservés lors d'un retour en arrière avec le bouton "Retour" [#1049](https://github.com/betagouv/bhasile/issues/1049).
- Ajout d'un lien vers la fiche produit dans le pied de page [#1055](https://github.com/betagouv/bhasile/issues/1055).
- Correction d'une faute de frappe "reconductible" [#1060](https://github.com/betagouv/bhasile/issues/1060).
- Correction de l'affichage de l'année du CPOM dans les documents financiers [#1032](https://github.com/betagouv/bhasile/issues/1032).
- Ajout d'un journal d'audit pour suivre les actions des utilisateurs [#1018](https://github.com/betagouv/bhasile/issues/1018).
- Ajout de CGU, Mentions légales et politique de confidentialité [#1041](https://github.com/betagouv/bhasile/issues/1041).
- Ajout de restrictions sur les utilisateurs autorisés [#950](https://github.com/betagouv/bhasile/issues/950).
- Correction du bug où "Tout public" était systématiquement défini [#1020](https://github.com/betagouv/bhasile/issues/1020).
- Amélioration du bloc "Contrôle" [#1005](https://github.com/betagouv/bhasile/issues/1005).
- Ajout d'une adresse email de contact sur la page 403 (interdit) [#1009](https://github.com/betagouv/bhasile/issues/1009).
- Ajout de tests E2E pour le formulaire de modification [#1019](https://github.com/betagouv/bhasile/issues/1019).

### Évolutions techniques
- Augmentation du délai d'expiration des transactions Prisma [#1045](https://github.com/betagouv/bhasile/issues/1045).
- Refactorisation des uploads de fichiers [#994](https://github.com/betagouv/bhasile/issues/994).
- Correction de problèmes liés à l'upsert des utilisateurs (plusieurs tentatives) [#1046](https://github.com/betagouv/bhasile/issues/1046), [#1044](https://github.com/betagouv/bhasile/issues/1044), [#1042](https://github.com/betagouv/bhasile/issues/1042).
- Mise à jour de plusieurs dépendances (voir section "Autres changements").
- Ajout de règles ESLint et formatage avec Prettier pour améliorer la qualité du code [#1011](https://github.com/betagouv/bhasile/issues/1011).
- Correction d'un bug qui empêchait d'accepter des valeurs négatives pour `cumulResultatNet` [#1023](https://github.com/betagouv/bhasile/issues/1023).
- Suppression de TODOs dans le code [#1010](https://github.com/betagouv/bhasile/issues/1010).
- Correction d'un crash des activités [#1008](https://github.com/betagouv/bhasile/issues/1008).

### Autres changements
- Préparation de l'application pour l'année 2026 : mise à jour des données de test, correction des typologies d'années [#1031](https://github.com/betagouv/bhasile/issues/1031), [#1030](https://github.com/betagouv/bhasile/issues/1030), [#1029](https://github.com/betagouv/bhasile/issues/1029), [#1028](https://github.com/betagouv/bhasile/issues/1028).
- Nettoyage du code après l'upload des fichiers [#1047](https://github.com/betagouv/bhasile/issues/1047).
- Correction de l'email du DPO [#1054](https://github.com/betagouv/bhasile/issues/1054).
- Correction de l'utilisation de la clé de fichier comme clé étrangère [#1053](https://github.com/betagouv/bhasile/issues/1053).
- Suppression des avenants orphelins et correction de leur `parentId` [#1058](https://github.com/betagouv/bhasile/issues/1058).
- Mise à jour de la matrice d'impact [#1039](https://github.com/betagouv/bhasile/issues/1039).
- Mises à jour de dépendances : `read-excel-file` (6.0.3 -> 7.0.0) [#1052](https://github.com/betagouv/bhasile/issues/1052), plusieurs mises à jour mineures et correctives [#1051](https://github.com/betagouv/bhasile/issues/1051), `immutable` (5.1.4 -> 5.1.5) [#1043](https://github.com/betagouv/bhasile/issues/1043), `fast-xml-parser` (4.5.3 -> 4.5.4) [#1038](https://github.com/betagouv/bhasile/issues/1038), `jsdom` (27.4.0 -> 28.0.0) [#1007](https://github.com/betagouv/bhasile/issues/1007), plusieurs mises à jour mineures et correctives [#1036](https://github.com/betagouv/bhasile/issues/1036), `rollup` (4.53.2 -> 4.59.0) [#1035](https://github.com/betagouv/bhasile/issues/1035), plusieurs mises à jour mineures et correctives [#1024](https://github.com/betagouv/bhasile/issues/1024), [#1006](https://github.com/betagouv/bhasile/issues/1006).
