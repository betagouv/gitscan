## Changelog : questions-ecrites (30 derniers jours, au 27 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration du processus de construction et de déploiement du projet, en particulier pour contourner les problèmes liés à l'utilisation de Docker dans certains environnements. Ces changements visent à rendre le déploiement plus fiable et automatisé.

### Évolutions techniques
- Mise en place d'un pipeline CI/CD basé sur Kaniko pour la construction des images Docker, contournant ainsi les blocages liés au proxy avec l'utilisation de `docker:dind` [#1234](https://github.com/SocialGouv/questions-ecrites/issues/1234).
- Création d'un Dockerfile et d'un pipeline complet pour automatiser la construction et le déploiement via ArgoCD.

### Autres changements
- Aucun autre changement significatif à signaler.
