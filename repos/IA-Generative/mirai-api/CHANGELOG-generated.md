## Changelog : mirai-api (30 derniers jours, au 26 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la mise en place d'une documentation complète et accessible pour l'API MirAI.  Une infrastructure de documentation basée sur VitePress a été implémentée, permettant aux développeurs de consulter facilement les spécifications de l'API et de comprendre son fonctionnement. Des améliorations ont également été apportées à l'intégration continue et au déploiement continu (CI/CD).

### Évolutions fonctionnelles
- Ajout d'une documentation initiale pour l'API MirAI via VitePress. [#1](https://github.com/IA-Generative/mirai-api/issues/1) (impliqué par les commits c5906f2, 74721b2, ed75e00)
- Mise à jour de la documentation du service à partir des spécifications Swagger réelles. [#1](https://github.com/IA-Generative/mirai-api/issues/1) (commit ed75e00)
- Modification de l'ordre de la section "Présentation" dans la navigation et la barre latérale de la documentation. [#1](https://github.com/IA-Generative/mirai-api/issues/1) (commit 7acd6c2)

### Évolutions techniques
- Implémentation d'un pipeline GitLab DSO (DevSecOps) et d'un workflow CD (Continuous Delivery) GitHub. [#2](https://github.com/IA-Generative/mirai-api/issues/2) (commit d71765b)
- Simplification de la construction des noms d'images Docker dans le pipeline CI GitLab. (commit fd08edd)
- Simplification du tag des images Docker pour la documentation à `mirai-api/docs:latest`. (commit cf52da0)
- Mise à jour du référentiel d'images dans le chart Helm pour utiliser le registre Harbor. (commit d0a2580)
- Correction de la configuration `imagePullSecrets` dans le chart Helm pour utiliser une liste de `LocalObjectReference`. (commit d38d60d)
- Renommage de `imagePullSecrets` en `registry-pull-secret` dans le chart Helm. (commit ef07f41)
- Installation de Git dans l'étape de construction Docker pour permettre la mise à jour de la date de dernière modification dans VitePress. (commit ea7c621)
- Ajout d'une configuration VitePress. (commit 66c5eda)

### Autres changements
- Suppression du dossier `src` obsolète du fichier README. (commit c355f67)
