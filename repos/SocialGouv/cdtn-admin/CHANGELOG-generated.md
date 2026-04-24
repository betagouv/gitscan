## Changelog : cdtn-admin (30 derniers jours, au 10 mai 2026)

### Résumé
Les dernières mises à jour de cdtn-admin se concentrent sur l'ajout de nouvelles fonctionnalités pour la gestion des actualités, notamment l'ajout de types d'actualités et la possibilité de les lister, ajouter et modifier via l'interface d'administration. Des corrections ont également été apportées pour améliorer la recherche et le téléchargement des conventions collectives, ainsi que pour la gestion des alertes et des synonymes.

### Évolutions fonctionnelles
- Ajout de la gestion des actualités dans l'interface d'administration : liste, ajout et modification. [#1655](https://github.com/SocialGouv/cdtn-admin/issues/1655)
- Ajout de types d'actualités dans l'interface d'administration. [#1654](https://github.com/SocialGouv/cdtn-admin/issues/1654)
- Suppression des pages informations pour l'outil "Comprendre sa procédure de licenciement". [#1657](https://github.com/SocialGouv/cdtn-admin/issues/1657)
- Amélioration de la recherche grâce à la mise à jour des synonymes et au renforcement des thèmes.
- Correction du téléchargement du fichier des conventions collectives grâce à l'ajout d'un user agent. [#1651](https://github.com/SocialGouv/cdtn-admin/issues/1651)
- Amélioration de la gestion des alertes : elles ne sont plus bloquées si le site travail-emploi est inaccessible. [#1646](https://github.com/SocialGouv/cdtn-admin/issues/1646)

### Évolutions techniques
- Mise à jour de Next.js en version 16.
- Ajout de tests unitaires pour les composants Tiptap. [#1649](https://github.com/SocialGouv/cdtn-admin/issues/1649)
- Mise à jour de la méthode de récupération du contenu du ministère.

### Autres changements
- Correction d'un problème lié au fichier `.env` de Next.js.
