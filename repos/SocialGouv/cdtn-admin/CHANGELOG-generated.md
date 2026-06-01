## Changelog : cdtn-admin (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, l'administration du Code du Travail Numérique a bénéficié d'améliorations concernant la gestion des contributions, notamment en ce qui concerne le SMIC et la publication/dépublication de ces contributions. Des corrections de bugs ont également été apportées pour améliorer la qualité des suggestions et la gestion des alertes.

### Évolutions fonctionnelles
- Ajout de méthodes de calcul du SMIC annuel pour les contributions [#1685](https://github.com/SocialGouv/cdtn-admin/issues/1685).
- Ajout d'un système de vérification (challenger) lors des modifications du SMIC sur les contributions [#1679](https://github.com/SocialGouv/cdtn-admin/issues/1679).
- Correction d'un bug lors de la dépublication d'une contribution [#1678](https://github.com/SocialGouv/cdtn-admin/issues/1678).
- Amélioration des suggestions proposées [#1672](https://github.com/SocialGouv/cdtn-admin/issues/1672).

### Évolutions techniques
- Migration vers une instance interne d'Elasticsearch (ES) pour l'environnement de pré-production [#1668](https://github.com/SocialGouv/cdtn-admin/issues/1668).
- Mise à jour du mapping Elasticsearch pour améliorer l'indexation des contributions, infographies, informations et modèles de courrier [#1665](https://github.com/SocialGouv/cdtn-admin/issues/1665).  Conversion du HTML en texte pour une meilleure recherche.
- Gestion du cas où une section peut avoir un titre vide dans les alertes [#1670](https://github.com/SocialGouv/cdtn-admin/issues/1670).

### Autres changements
- Publication des versions 2.75.0, 2.74.0, 2.73.4, 2.73.3 et 2.72.3.
