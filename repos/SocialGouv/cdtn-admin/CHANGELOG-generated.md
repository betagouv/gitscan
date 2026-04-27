## Changelog : cdtn-admin (30 derniers jours, au 10 mai 2026)

### Résumé
Ce mois-ci, l'administration du Code du Travail Numérique a été enrichie avec la gestion des actualités (ajout, modification, liste) et des types d'actualités. Des corrections ont également été apportées pour améliorer la mise à jour des documents lors de la modification de questions et pour optimiser la recherche de suggestions. Enfin, des éléments liés à l'outil "Comprendre sa procédure de licenciement" ont été supprimés.

### Évolutions fonctionnelles
- Ajout de la gestion des actualités : possibilité d'ajouter, modifier et consulter la liste des actualités via l'interface d'administration. [#1655](https://github.com/SocialGouv/cdtn-admin/issues/1655)
- Ajout des types d'actualités dans l'interface d'administration. [#1654](https://github.com/SocialGouv/cdtn-admin/issues/1654)
- Suppression des pages d'informations relatives à l'outil "Comprendre sa procédure de licenciement". [#1657](https://github.com/SocialGouv/cdtn-admin/issues/1657)
- Correction d'un problème de mise à jour des documents lors de la modification d'une question. [#1667](https://github.com/SocialGouv/cdtn-admin/issues/1667)
- Amélioration des suggestions de recherche avec un boost des thèmes et ajout de synonymes.

### Évolutions techniques
- Mise à jour du fichier `.next-env` pour corriger un problème de configuration.
- Mise à jour de la méthode de récupération du contenu du ministère.

### Autres changements
- Mise à jour des synonymes pour améliorer la recherche.
- Ajout de tests unitaires pour Tiptap. [#1649](https://github.com/SocialGouv/cdtn-admin/issues/1649)
- Ajout du user agent pour le téléchargement des conventions collectives. [#1651](https://github.com/SocialGouv/cdtn-admin/issues/1651)
