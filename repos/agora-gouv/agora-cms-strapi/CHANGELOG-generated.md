## Changelog : agora-cms-strapi (30 derniers jours, au 10 juillet 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la stabilité et des performances de la plateforme, notamment en ajustant la configuration du serveur web Nginx et en optimisant l'utilisation de la mémoire. Des améliorations fonctionnelles ont également été apportées, comme l'ajout de la fonction permettant d'identifier l'auteur d'une réponse et l'ajout de clusters de mots pour la semaine libre. Enfin, une migration vers Strapi V5 a été réalisée.

### Évolutions fonctionnelles
- Ajout de la fonction permettant d'afficher l'auteur d'une réponse. [#46](https://github.com/agora-gouv/agora-cms-strapi/pull/46)
- Ajout de clusters de mots pour la fonctionnalité "semaine libre". [#48](https://github.com/agora-gouv/agora-cms-strapi/pull/48)

### Évolutions techniques
- Migration de la plateforme vers Strapi V5. [#47](https://github.com/agora-gouv/agora-cms-strapi/pull/47)
- Augmentation des timeouts et des buffers Nginx pour améliorer la gestion des requêtes.
- Ajustement des paramètres de la mémoire Node.js pour optimiser les performances.
- Retour en arrière de la configuration Nginx précédente suite à des problèmes. [#49](https://github.com/agora-gouv/agora-cms-strapi/pull/49)
- Mise à jour de la version de Node.js. [#50](https://github.com/agora-gouv/agora-cms-strapi/pull/50)
