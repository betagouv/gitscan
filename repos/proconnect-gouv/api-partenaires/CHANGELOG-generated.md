## Changelog : api-partenaires (30 derniers jours, au 22 juillet 2026)

### Résumé
Ce mois-ci, l'API Partenaires a été entièrement mise en place, passant d'un simple squelette de projet à une API fonctionnelle permettant la configuration des partenaires via une base de données MongoDB.  L'infrastructure CI/CD a également été configurée pour automatiser les tests et le déploiement.

### Évolutions fonctionnelles
- Implémentation de l'API de configuration des partenaires, stockée dans MongoDB. [#2](https://github.com/proconnect-gouv/api-partenaires/pull/2)
- Ajout d'un exemple d'intégration pour la modification des FQDN des fournisseurs : `edit_provider_fqdns`.
- Documentation des routes, de la configuration et des tests d'intégration.

### Évolutions techniques
- Migration du projet vers Bun pour la compilation en binaire statique via un Dockerfile multi-étapes.
- Mise en place d'une infrastructure CI/CD complète avec des workflows pour les tests, la construction Docker et les mises à jour de dépendances (dependabot). [#1](https://github.com/proconnect-gouv/api-partenaires/pull/1)
- Utilisation de Docker Compose pour simplifier l'environnement de développement et de test.
- Suppression de la protection par liste blanche d'adresses IP au niveau de l'application, et renommage de la collection des fournisseurs.
- Amélioration de la configuration des images Docker et ajout de la surveillance de Compose.
- Suppression des actions `setup-compose` et `quiet-build` obsolètes.

### Autres changements
- Documentation de l'exemple de contrat `AUTHORIZED_IPS` pour le proxy.
- Initialisation du projet avec un squelette de base.
- Ajout de tests d'intégration et exécution dynamique des exemples en CI.
