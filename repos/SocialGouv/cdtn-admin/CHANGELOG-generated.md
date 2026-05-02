## Changelog : cdtn-admin (30 derniers jours, au 10 mai 2026)

### Résumé
Ce mois-ci, l'administration de cdtn-admin a bénéficié de plusieurs améliorations, notamment l'ajout de la gestion des actualités, la migration vers une instance Elasticsearch interne pour la pré-production, et des corrections de bugs concernant l'ingestion de données et la gestion des sections d'alertes. Des optimisations ont également été apportées à la recherche grâce à la mise à jour des synonymes.

### Évolutions fonctionnelles
- **Actualités :** Ajout de la fonctionnalité permettant de gérer les actualités (liste, ajout, modification) [#1655](https://github.com/SocialGouv/cdtn-admin/issues/1655).
- **Infographies :** Suppression des anciennes pages "informations" liées à l'outil "comprendre sa procédure de licenciement" [#1657](https://github.com/SocialGouv/cdtn-admin/issues/1657).
- **Alertes :** Correction d'un bug empêchant la gestion correcte des sections d'alerte ayant un titre vide [#1670](https://github.com/SocialGouv/cdtn-admin/issues/1670).
- **Recherche :** Amélioration des suggestions de recherche grâce à la mise à jour des synonymes et au renforcement des thèmes.

### Évolutions techniques
- **Elasticsearch :** Migration vers une instance Elasticsearch interne pour l'environnement de pré-production [#1668](https://github.com/SocialGouv/cdtn-admin/issues/1668).
- **Ingestion de données :** Mise à jour du mapping et conversion du HTML en texte pour les contributions, infographies, informations et modèles de courrier [#1665](https://github.com/SocialGouv/cdtn-admin/issues/1665).
- **Configuration :** Correction du fichier `.env` pour Next.js.

### Autres changements
- Mise à jour des synonymes pour améliorer la recherche.
- Correction de la mise à jour des documents lors de la modification d'une question.
