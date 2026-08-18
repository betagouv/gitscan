## Changelog : conseillers-entreprises (30 derniers jours, au 13 août 2026)

### Résumé
Ce mois-ci, la plateforme a bénéficié d'améliorations significatives de son interface d'administration, notamment pour la gestion des coopérations, des rapports et des experts. Les utilisateurs disposent désormais de plus d'autonomie grâce à la gestion en libre-service des clés API. La communication automatisée par email a été affinée pour plus de clarté, tandis que l'infrastructure technique a été mise à jour (Ruby, Rails) et optimisée.

### Évolutions fonctionnelles

**Administration et Pilotage**
- Amélioration de la gestion des "Experts" dans les formulaires d'administration (correction des doublons et ajout de codes manquants) [#4639](https://github.com/betagouv/conseillers-entreprises/pull/4639).
- Ajout de la possibilité pour les administrateurs de consulter directement tous les exports d'antennes depuis le menu "Outils" [#4616](https://github.com/betagouv/conseillers-entreprises/pull/4616).
- Amélioration du suivi des antennes avec l'application de filtres sur les compteurs dans le contrôleur de monitoring [#4643](https://github.com/betagouv/conseillers-entreprises/pull/4643).
- Ajout de la colonne `imported_at` dans la vue administration des utilisateurs pour un meilleur suivi des données [#4641](https://github.com/betagouv/conseillers-entreprises/pull/4641).

**Coopérations et Sponsors**
- Refonte majeure de l'interface utilisateur pour les sections "Coopérations" et "Rapports" [#4616](https://github.com/betagouv/conseillers-entreprises/pull/4616).
- Ajustement des droits d'accès : les sponsors peuvent désormais consulter les rapports d'antennes, mais pas les données de "matches" [#4607](https://github.com/betagouv/conseillers-entreprises/pull/4607).
- Ajout d'un filtre par institution pour la consultation des statistiques de correspondance des coopérations [#4607](https://github.com/betagouv/conseillers-entreprises/pull/4607).

**Expérience Utilisateur et Communication**
- Mise en place de l'auto-gestion des clés API : les utilisateurs peuvent désormais générer et gérer leurs propres jetons d'accès [#4605](https://github.com/betagouv/conseillers-entreprises/pull/4605).
- Optimisation des emails automatisés (rappels, notifications de mauvaise qualité, etc.) avec des objets plus explicites et une meilleure logique de repli [#4635](https://github.com/betagouv/conseillers-entreprises/pull/4635), [#4630](https://github.com/betagouv/conseillers-entreprises/pull/4630).
- Enrichissement des témoignages avec l'ajout de métadonnées (images, citations, balises articles) pour une meilleure présentation [#4602](https://github.com/betagouv/conseillers-entreprises/pull/4602).
- Mise à jour de la vidéo YouTube sur la page "Comment ça marche" [#4636](https://github.com/betagouv/conseillers-entreprises/pull/4636).

### Évolutions techniques

**Infrastructure et Performance**
- Optimisation de la stratégie de cache : expérimentation de `solid_cache` suivie d'un retour à `redis` pour la stabilité de l'application [#4654](https://github.com/betagouv/conseillers-entreprises/pull/4654), [#4608](https://github.com/betagouv/conseillers-entreprises/pull/4608).
- Amélioration des performances de l'API des sujets en évitant les requêtes N+1 [#4604](https://github.com/betagouv/conseillers-entreprises/pull/4604).
- Mise en place du monitoring du taux de succès du cache (*cache hit rate*) via AppSignal [#4627](https://github.com/betagouv/conseillers-entreprises/pull/4627).

**Core et API**
- Mise à jour majeure de l'environnement technique : passage à Ruby 4.0.6 et mise à jour de Rails [#4617](https://github.com/betagouv/conseillers-entreprises/pull/4617), [#4628](https://github.com/betagouv/conseillers-entreprises/pull/4628).
- Nouvelle API pour les "Sujets" incluant une documentation Swagger et des spécifications complètes [#4604](https://github.com/betagouv/conseillers-entreprises/pull/4604).

**DevOps et Monitoring**
- Refactorisation et modularisation des tâches de déploiement en production et d'annonces de déploiement pour une meilleure gestion des erreurs [#4613](https://github.com/betagouv/conseillers-entreprises/pull/4613).
- Activation du monitoring AppSignal sur l'environnement de staging [#4640](https://github.com/betagouv/conseillers-entreprises/pull/4640).

### Autres changements
- Nettoyage de la base de données par la suppression d'anciennes migrations obsolètes [#4629](https://github.com/betagouv/conseillers-entreprises/pull/4629).
