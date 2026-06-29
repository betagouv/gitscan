## Changelog : cdtn-admin (30 derniers jours, au 25 juin 2026)

### Résumé
Ce changelog présente les améliorations apportées à l'outil d'administration du Code du Travail Numérique au cours du dernier mois. Les principales évolutions concernent l'enrichissement des fonctionnalités de gestion des contributions (ajout de types, détection automatique de salaires, calculs sur le SMIC) et l'ajout d'outils pour la gestion des données (dump de la base de données).

### Évolutions fonctionnelles
- Ajout d'un nouveau type de contribution : "bon à savoir" [#1691](https://github.com/SocialGouv/cdtn-admin/issues/1691)
- Détection automatique des salaires exprimés en pourcentage du SMIC dans le challenger [#1689](https://github.com/SocialGouv/cdtn-admin/issues/1689)
- Renommage de l'outil "Trouver sa CC" pour plus de clarté [#1669](https://github.com/SocialGouv/cdtn-admin/issues/1669)
- Ajout de méthodes de calcul sur le SMIC annuel pour les contributions [#1685](https://github.com/SocialGouv/cdtn-admin/issues/1685)
- Ajout d'un challenger pour les modifications du SMIC sur les contributions [#1679](https://github.com/SocialGouv/cdtn-admin/issues/1679)

### Évolutions techniques
- Ajout d'un script permettant de réaliser un dump de la base de données à une date précise (PITR - Point In Time Recovery) [#1687](https://github.com/SocialGouv/cdtn-admin/issues/1687)
- Le fichier `next-env.d.ts` généré par Next.js est maintenant ignoré par le système de contrôle de version.

### Autres changements
- Mise en place d'un package Python pour l'analyse des statistiques [#1690](https://github.com/SocialGouv/cdtn-admin/issues/1690)
- Publication des versions 2.77.0, 2.76.0, 2.75.1 et 2.75.0.
