## Changelog : cdtn-admin (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la gestion des contributions, notamment en ajoutant un système de "challenger" pour les modifications du SMIC et en corrigeant des bugs liés à la publication et à la mise à jour des contributions. Des améliorations ont également été apportées à l'ingestion de données et à la recherche, avec une migration vers une instance Elasticsearch interne pour la preproduction.

### Évolutions fonctionnelles
- Ajout d'un système de "challenger" pour les modifications du SMIC sur les contributions, permettant une validation plus rigoureuse des informations. [#1679](https://github.com/SocialGouv/cdtn-admin/issues/1679)
- Correction d'un bug empêchant la bonne dépublication des contributions. [#1678](https://github.com/SocialGouv/cdtn-admin/issues/1678)
- Correction de la gestion des sections d'alerte ayant un titre vide. [#1670](https://github.com/SocialGouv/cdtn-admin/issues/1670)
- Amélioration de la mise à jour des documents lors de la modification d'une question dans une contribution. [#1667](https://github.com/SocialGouv/cdtn-admin/issues/1667)
- Amélioration des suggestions. [#1672](https://github.com/SocialGouv/cdtn-admin/issues/1672)

### Évolutions techniques
- Migration vers une instance Elasticsearch interne pour l'environnement de préproduction, améliorant potentiellement les performances et la stabilité de la recherche. [#1668](https://github.com/SocialGouv/cdtn-admin/issues/1668)
- Mise à jour du mapping Elasticsearch pour améliorer l'ingestion de données (contributions, infographies, informations, modèles de courrier) et conversion du HTML en texte brut. [#1665](https://github.com/SocialGouv/cdtn-admin/issues/1665)

### Autres changements
- Aucune information supplémentaire à signaler.
