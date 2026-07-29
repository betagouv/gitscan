## Changelog : sylvasan (30 derniers jours, au 28 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives sur le web et l'application mobile, notamment l'ajout de fonctionnalités de suivi (follow-ups) des enquêtes, la gestion de la duplication d'enquêtes, et des corrections d'erreurs pour une meilleure expérience utilisateur. De nombreuses mises à jour de dépendances ont également été intégrées pour assurer la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- Ajout de la fonctionnalité de création, modification et suppression des follow-ups via l'interface web. [#433](https://github.com/betagouv/sylvasan/pull/433)
- Possibilité de dupliquer une enquête existante. [#429](https://github.com/betagouv/sylvasan/pull/429)
- Affichage des follow-ups dans l'interface web.
- Ajout de la possibilité de voir les données d'un follow-up depuis le web.
- Amélioration de la navigation post-followup.
- Ajout de la possibilité de remplir des suivis.
- Ajout d'une validation pour la condition d'affichage.
- Ajout d'une URL pour créer des follow-ups directement à partir d'une réponse.
- Ajout de la possibilité d'ajouter une observation à une réponse d'une autre personne.
- Affichage du nom du répondant et d'une couleur différente pour les pins d'autres personnes.
- Ajout de la gestion des vocabulaires pour les champs de réponse. [#435](https://github.com/betagouv/sylvasan/pull/435)
- Ajout de champs par défaut pour les types de champs select, radio et autocomplete. [#434](https://github.com/betagouv/sylvasan/pull/434)
- Ajout de messages d'erreur pour l'authentification.
- Publication d'une version de test ouverte pour Android.
- Publication d'une version preprod pour Android.

### Évolutions techniques
- Mise à jour de nombreuses dépendances (Django, React, Node.js, Sentry, etc.) pour améliorer la sécurité et la performance.
- Refactoring de la sélection d'organisation/pôle vers un composable.
- Utilisation de Typescript pour améliorer la qualité du code.
- Ajout de tests unitaires pour les follow-ups au niveau des applications surveys et responses.
- Mise à jour de la configuration du precommit.
- Ajout de modèles et migrations pour les follow-ups.
- Correction d'un bug lié à la sauvegarde des brouillons.
- Correction d'un bug lié à la modification des suivis.
- Suppression de l'appel au store depuis ResponsePinCard.
- Ajout de documentation sur les permissions des rôles.
- Ajout de PostGIS et PointField pour les réponses.
- Mise à jour des versions des applications mobiles (iOS et Android).

### Autres changements
- Ajout d'informations sur la provenance des données et des précisions concernant les données géographiques et les images.
- Suppression de l'URL des données.
- Correction d'un problème lié au flag "busy" qui restait actif après un unmount.
- Suppression de la compression d'image. [#416](https://github.com/betagouv/sylvasan/pull/416)
- Configuration de l'open testing sur le Play Store. [#417](https://github.com/betagouv/sylvasan/pull/417)
- Amélioration de la structure du code et correction de remarques issues des revues de code.
