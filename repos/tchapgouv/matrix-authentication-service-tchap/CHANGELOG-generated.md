## Changelog : matrix-authentication-service-tchap (30 derniers jours, au 10 mai 2026)

### Résumé
Ce changelog fait état d'améliorations significatives concernant les tests d'authentification, notamment l'ajout de tests pour la réactivation silencieuse de compte et la suppression de la création de comptes hérités sans passer par le service d'authentification Matrix (MAS). La documentation a également été enrichie avec des instructions pour l'utilisation de Docker.

### Évolutions fonctionnelles
- Ajout de tests pour la réactivation silencieuse de compte. [#35](https://github.com/tchapgouv/matrix-authentication-service-tchap/issues/35)
- Suppression de la création de comptes hérités sans passer par le MAS, renforçant ainsi la sécurité et la conformité du processus d'authentification. [#36](https://github.com/tchapgouv/matrix-authentication-service-tchap/issues/36)

### Évolutions techniques
- Refactorisation de la structure des fichiers pour une meilleure organisation.
- Ajout de documentation concernant l'utilisation de Docker pour faciliter le déploiement et l'exécution des tests.

### Autres changements
- Mise à jour du fichier README.md pour refléter les changements récents.
