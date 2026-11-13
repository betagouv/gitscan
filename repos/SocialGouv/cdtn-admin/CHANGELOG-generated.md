## Changelog : cdtn-admin (30 derniers jours, au 12 novembre 2026)

### Résumé
Ce mois-ci, l'outil d'administration a été enrichi de nouvelles capacités d'analyse statistique et de tableaux de bord via l'intégration de Metabase. La gestion des contenus (actualités et contributions) a été considérablement fluidifiée par de nombreuses améliorations fonctionnelles, tandis que la sécurité et l'infrastructure ont été renforcées pour garantir un déploiement plus stable et sécurisé.

### Évolutions fonctionnelles
- **Actualités** :
  - Enrichissement du contenu avec l'ajout d'images, de sections « Pour aller plus loin » et de « Références » ([#1722](https://github.com/SocialGouv/cdtn-admin/issues/1722)).
  - Amélioration de la gestion des dates (publication, modification et gestion du fuseau horaire) ([#1730](https://github.com/SocialGouv/cdtn-admin/issues/1730), [#1731](https://github.com/SocialGouv/cdtn-admin/issues/1731)).
  - Rendu de l'image facultative ([#1735](https://github.com/SocialGouv/cdtn-admin/issues/1735)) et correction de l'affichage des notifications de suppression ([#1742](https://github.com/SocialGouv/cdtn-admin/issues/1742)).
- **Contributions** :
  - Amélioration globale du processus de création ([#1727](https://github.com/SocialGouv/cdtn-admin/issues/1727)).
  - Automatisation de la mise à jour de la date lors de la publication ([#1726](https://github.com/SocialGouv/cdtn-admin/issues/1726)).
  - Correction du comportement du surlignage ([#1737](https://github.com/SocialGouv/cdtn-admin/issues/1737)).
- **Analyse & Statistiques** :
  - Nouveaux indicateurs disponibles : taux de complétion des pages modèles ([#1724](https://github.com/SocialGouv/cdtn-admin/issues/1724)), données sur les actualités ([#1728](https://github.com/SocialGouv/cdtn-admin/issues/1728)) et analyse du parcours après contribution ([#7562](https://github.com/SocialGouv/cdtn-admin/issues/7562) / [#1738](https://github.com/SocialGouv/cdtn-admin/issues/1738)).
  - Intégration de Metabase pour permettre la création de tableaux de bord personnalisés.
- **Export & Gestion de contenu** :
  - Ajout des liens recommandés dans l'export des fiches Service-Public ([#1719](https://github.com/SocialGouv/cdtn-admin/issues/1719)).
  - Correction pour empêcher la double création, sauvegarde ou publication de contenus ([#1736](https://github.com/SocialGouv/cdtn-admin/issues/1736)).

### Évolutions techniques
- **Infrastructure & Sécurité** :
  - Unification de l'image Docker pour l'ensemble des environnements ([#1743](https://github.com/SocialGouv/cdtn-admin/issues/1743)).
  - Mise à jour de Node.js pour corriger des vulnérabilités de sécurité ([#1732](https://github.com/SocialGouv/cdtn-admin/issues/1732)).
- **Données** :
  - Nettoyage et optimisation des scripts d'agrégation de données.
