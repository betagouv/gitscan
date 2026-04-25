## Changelog : tchap-e2e-playwright (30 derniers jours, au 23 avril 2026)

### Résumé
Ce changelog couvre les améliorations apportées aux tests d'authentification et de création de salles Tchap. Les modifications incluent la correction d'un problème de création de salle, l'ajout de tests pour la réactivation silencieuse de compte, et la suppression de la création de comptes hérités sans MAS. La documentation a également été mise à jour pour inclure des informations sur l'utilisation de Docker.

### Évolutions fonctionnelles
- Correction d'un bug empêchant la création de salles. [#40](https://github.com/tchapgouv/tchap-e2e-playwright/issues/40)
- Ajout de tests pour vérifier la réactivation silencieuse d'un compte. [#35](https://github.com/tchapgouv/tchap-e2e-playwright/issues/35)
- Suppression de la fonctionnalité de création de compte sans passer par le service d'authentification Matrix (MAS). [#36](https://github.com/tchapgouv/tchap-e2e-playwright/issues/36)

### Évolutions techniques
- Mise à jour de l'image Docker Playwright vers la version v1.59.1-noble. [#38](https://github.com/tchapgouv/tchap-e2e-playwright/issues/38)
- Intégration de Biome pour le formatage du code. [#36](https://github.com/tchapgouv/tchap-e2e-playwright/issues/36)

### Autres changements
- Mise à jour de la documentation README pour inclure des instructions sur l'utilisation de Docker. [#36](https://github.com/tchapgouv/tchap-e2e-playwright/issues/36)
- Amélioration de la documentation README.
