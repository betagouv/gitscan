## Changelog : ma-cantine (30 derniers jours, au 1er septembre 2026)

### Résumé
Ce mois-ci, le projet a connu une transformation majeure de l'interface de gestion des établissements, avec l'introduction de nouvelles pages dédiées et une refonte visuelle. Les capacités de diagnostic ont été considérablement enrichies par l'ajout de nouveaux champs de données et de règles de contrôle plus strictes. Enfin, la sécurité a été renforcée pour les profils administratifs grâce à l'implémentation de l'authentification à deux facteurs (2FA).

### Évolutions fonctionnelles
- **Gestion des établissements et des gestionnaires**
    - Refonte complète de l'espace établissement : création des pages "Mes informations", "Ma page publique", "Cantine du groupe" et "Toutes mes télédéclarations" ([#6902](https://github.com/betagouv/ma-cantine/issues/6902), [#6921](https://github.com/betagouv/ma-cantine/issues/6921), [#6906](https://github.com/betagouv/ma-cantine/issues/6906), [#6907](https://github.com/betagouv/ma-cantine/issues/6907)).
    - Ajout d'une nouvelle page "Mes gestionnaires" ([#6909](https://github.com/betagouv/ma-cantine/issues/6909)).
    - Amélioration de l'expérience utilisateur : ajout d'un bandeau d'information ([#7048](https://github.com/betagouv/ma-cantine/issues/7048)), mise en place d'une pagination dynamique dans les tableaux ([#6950](https://github.com/betagouv/ma-cantine/issues/6950)), et mise à jour des coloris des badges ([#6982](https://github.com/betagouv/ma-cantine/issues/6982)).
    - Optimisation de l'accessibilité et corrections d'affichage (typos, alignements, responsive) ([#6948](https://github.com/betagouv/ma-cantine/issues/6948), [#7017](https://github.com/betagouv/ma-cantine/issues/7017), [#7016](https://github.com/betagouv/ma-cantine/issues/7016)).
    - Correction de la recherche par commune et SIREN ([#6976](https://github.com/betagouv/ma-cantine/issues/6976)).

- **Diagnostics et Bilans**
    - Enrichissement des données de diagnostic avec de nouveaux champs (origines France, Europe, circuit court, local, et par familles de produits) ([#7019](https://github.com/betagouv/ma-cantine/issues/7019), [#7006](https://github.com/betagouv/ma-cantine/issues/7006), [#7005](https://github.com/betagouv/ma-cantine/issues/7005)).
    - Ajout du champ obligatoire `nombre_repas_an` pour les déclarations à partir de 2026 ([#7010](https://github.com/betagouv/ma-cantine/issues/7010)).
    - Renforcement des règles métier pour garantir la cohérence des données (ex: cohérence des taux bio/équitable, vérification des droits du déclarant) ([#7012](https://github.com/betagouv/ma-cantine/issues/7012), [#7007](https://github.com/betagouv/ma-cantine/issues/7007), [#7004](https://github.com/betagouv/ma-cantine/issues/7004)).
    - Amélioration de la consultation des justificatifs PDF pour les télédéclarations ([#6958](https://github.com/betagouv/ma-cantine/issues/6958)).

- **Administration**
    - Ajout de fonctionnalités de restauration pour les achats et les cantines archivés ([#6979](https://github.com/betagouv/ma-cantine/issues/6979), [#6952](https://github.com/betagouv/ma-cantine/issues/6952)).
    - Ajout de liens vers les arrêtés Legifrance dans les dates de campagne de télédéclaration ([#7014](https://github.com/betagouv/ma-cantine/issues/7014)).

### Évolutions techniques
- **Sécurité**
    - Mise en place de l'authentification à deux facteurs (2FA) via TOTP pour les utilisateurs superusers et staff ([#7040](https://github.com/betagouv/ma-cantine/issues/7040), [#7044](https://github.com/betagouv/ma-cantine/issues/7044), [#7046](https://github.com/betagouv/ma-cantine/issues/7046)).

- **API et Backend**
    - Optimisation et refonte des endpoints API pour les Diagnostics ([#6991](https://github.com/betagouv/ma-cantine/issues/6991), [#6990](https://github.com/betagouv/ma-cantine/issues/6990), [#6975](https://github.com/betagouv/ma-cantine/issues/6975)), les Bilans ([#6974](https://github.com/betagouv/ma-cantine/issues/6974), [#6981](https://github.com/betagouv/ma-cantine/issues/6981)) et les Achats ([#7042](https://github.com/betagouv/ma-cantine/issues/7042)).
    - Utilisation d'endpoints dédiés pour la gestion des images, des logos et des justificatifs ([#6953](https://github.com/betagouv/ma-cantine/issues/6953), [#6954](https://github.com/betagouv/ma-cantine/issues/6954), [#6983](https://github.com/betagouv/ma-cantine/issues/6983)).
    - Correction de la configuration de stockage S3 suite à la mise à jour de la bibliothèque `boto3` ([#7039](https://github.com/betagouv/ma-cantine/issues/7039), [#7028](https://github.com/betagouv/ma-cantine/issues/7028)).

- **Architecture et Maintenance**
    - Refactorisation de la gestion des applications installées (`INSTALLED_APPS`) pour une meilleure séparation des responsabilités ([#7033](https://github.com/betagouv/ma-cantine/issues/7033)).
    - Nettoyage et optimisation de la gestion des dépendances dans `pyproject` ([#6985](https://github.com/betagouv/ma-cantine/issues/6985), [#6791](https://github.com/betagouv/ma-cantine/issues/6791)).
    - Homogénéisation des tests de l'API ([#6944](https://github.com/betagouv/ma-cantine/issues/6944)).
