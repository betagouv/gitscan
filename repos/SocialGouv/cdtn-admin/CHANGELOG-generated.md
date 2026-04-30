## Changelog : cdtn-admin (30 derniers jours, au 10 mai 2026)

### Résumé
Ce mois-ci, l'administration de cdtn-admin a bénéficié de l'ajout de la gestion des actualités, d'améliorations de la recherche grâce à la migration vers une instance Elasticsearch interne et de corrections de bugs concernant l'ingestion de contenu et l'affichage des alertes. Des ajustements ont également été apportés pour optimiser l'outil "Comprendre sa procédure de licenciement".

### Évolutions fonctionnelles
- **Actualités :** Ajout de la fonctionnalité permettant de gérer les actualités (liste, ajout, modification). [#1655](https://github.com/SocialGouv/cdtn-admin/issues/1655)
- **Outil "Comprendre sa procédure de licenciement" :** Suppression des pages "informations" inutiles dans cet outil. [#1657](https://github.com/SocialGouv/cdtn-admin/issues/1657)
- **Alertes :** Correction d'un bug empêchant l'affichage correct des alertes lorsque le titre d'une section est vide. [#1670](https://github.com/SocialGouv/cdtn-admin/issues/1670)
- **Ingestion de contenu :** Amélioration de l'ingestion de contributions, d'infographies, d'informations et de modèles de courrier en convertissant le HTML en texte et en mettant à jour le mapping Elasticsearch. [#1665](https://github.com/SocialGouv/cdtn-admin/issues/1665)

### Évolutions techniques
- **Elasticsearch :** Migration vers une instance interne d'Elasticsearch pour l'environnement de pré-production. [#1668](https://github.com/SocialGouv/cdtn-admin/issues/1668)
- **Recherche :** Amélioration des suggestions de recherche en boostant les thèmes et en ajoutant des synonymes.
- **Configuration :** Correction d'un problème lié au fichier `.env` de Next.js.

### Autres changements
- Mise à jour des synonymes utilisés pour la recherche.
- Correction de la mise à jour des documents lors de la modification d'une question.
