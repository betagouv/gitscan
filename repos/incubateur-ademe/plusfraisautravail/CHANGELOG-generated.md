## Changelog : plusfraisautravail (30 derniers jours, au 28 juillet 2026)

### Résumé
Ce mois-ci, le projet a connu une refonte majeure de son système de gestion de contenu (CMS) avec la migration vers Wagtail et l'intégration de sites-conformes. Des améliorations significatives ont également été apportées à l'infrastructure de déploiement et à la gestion des médias, notamment pour faciliter la restauration et la synchronisation des données. L'intégration de Climadiag commune a également été finalisée.

### Évolutions fonctionnelles
- Intégration de Climadiag commune, permettant son affichage et son utilisation au sein de l'application. [#21](https://github.com/incubateur-ademe/plusfraisautravail/issues/21)
- Ajout de sites-conformes pour une meilleure gestion et conformité des sites web. [#23](https://github.com/incubateur-ademe/plusfraisautravail/pull/23)
- Amélioration du texte du lien de l'alerte pour une meilleure clarté et urgence.
- Correction de l'affichage de Climadiag, notamment le positionnement de l'intégration après le pied de page.
- Correction du pointage de Climadiag en production vers l'environnement de staging PFMV en attendant un token de production.

### Évolutions techniques
- Migration du CMS vers Wagtail avec le package sites-conformes, modernisant ainsi l'infrastructure de gestion de contenu.
- Refonte de l'infrastructure de déploiement avec Terraform, incluant l'ajout de workflows pour la destruction et le nettoyage des ressources.
- Amélioration de la gestion des secrets et des identifiants de base de données, notamment la correction de la génération du mot de passe Postgres.
- Mise en place d'une nouvelle stratégie de synchronisation des médias entre les buckets, avec des outils pour la sauvegarde et la restauration.
- Utilisation de l'API v1 pour le déploiement du CMS.
- Amélioration de la gestion des erreurs et des connexions à la base de données dans le CMS.
- Migration vers Publicodes. [#20](https://github.com/incubateur-ademe/plusfraisautravail/pull/20)

### Autres changements
- Ajout d'une entrée de workflow pour remplacer les variables d'environnement avec `tofu_replace`.
- Simplification du processus de restauration de la base de données.
- Ajout de la possibilité de charger les variables d'environnement via un fichier `.env`.
- Correction de divers problèmes de configuration et de déploiement.
