## Changelog : cdtn-admin (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, l'administration de cdtn-admin a bénéficié d'améliorations concernant la gestion des contributions, notamment en lien avec le SMIC, ainsi que des corrections de bugs pour une meilleure stabilité et une indexation plus performante des contenus. Des migrations vers une instance Elasticsearch interne ont également été réalisées pour la pré-production.

### Évolutions fonctionnelles
- Ajout d'un mécanisme de "challenger" pour les modifications du SMIC sur les contributions, permettant une validation plus rigoureuse des informations. [#1679](https://github.com/SocialGouv/cdtn-admin/issues/1679)
- Correction d'un bug empêchant la bonne dépublication des contributions. [#1678](https://github.com/SocialGouv/cdtn-admin/issues/1678)
- Amélioration de la gestion des sections d'alertes, permettant de gérer le cas où un titre de section est vide. [#1670](https://github.com/SocialGouv/cdtn-admin/issues/1670)
- Correction de l'affichage des suggestions. [#1672](https://github.com/SocialGouv/cdtn-admin/issues/1672)

### Évolutions techniques
- Migration vers une instance interne d'Elasticsearch (ES) pour l'environnement de pré-production, améliorant potentiellement la performance et la fiabilité de la recherche. [#1668](https://github.com/SocialGouv/cdtn-admin/issues/1668)
- Mise à jour du mapping Elasticsearch et conversion du HTML en texte pour améliorer l'indexation des contributions, infographies, informations et modèles de courrier. [#1665](https://github.com/SocialGouv/cdtn-admin/issues/1665)

### Autres changements
- Aucune information supplémentaire ne ressort des commits analysés.
