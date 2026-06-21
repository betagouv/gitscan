## Changelog : cdtn-admin (30 derniers jours, au 17 juin 2026)

### Résumé
Ce mois-ci, l'administration du Code du Travail Numérique a bénéficié d'améliorations significatives concernant la gestion des contributions, notamment l'ajout de fonctionnalités pour le SMIC et la détection automatique de salaires. De plus, de nouveaux outils ont été mis à disposition et des améliorations ont été apportées à la gestion des sauvegardes de la base de données.

### Évolutions fonctionnelles
- Ajout d'un challenger pour les modifications du SMIC sur les contributions, permettant une meilleure gestion des impacts des évolutions du SMIC. [#1679](https://github.com/SocialGouv/cdtn-admin/issues/1679)
- Ajout de méthodes de calcul sur le SMIC annuel pour les contributions. [#1685](https://github.com/SocialGouv/cdtn-admin/issues/1685)
- Détection automatique des salaires en pourcentage du SMIC dans le challenger de contributions. [#1689](https://github.com/SocialGouv/cdtn-admin/issues/1689)
- Renommage de l'outil "Trouver sa CC" pour une meilleure clarté. [#1669](https://github.com/SocialGouv/cdtn-admin/issues/1669)
- Possibilité de réaliser un dump (sauvegarde) de la base de données à une date précise (PITR - Point In Time Recovery). [#1687](https://github.com/SocialGouv/cdtn-admin/issues/1687)

### Évolutions techniques
- Aucune évolution technique majeure n'a été signalée dans les commits analysés.

### Autres changements
- Mises à jour de version : 2.76.0, 2.75.1, 2.75.0, 2.74.0.
