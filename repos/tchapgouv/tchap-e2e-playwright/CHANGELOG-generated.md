## Changelog : tchap-e2e-playwright (30 derniers jours, au 29 avril 2026)

### Résumé
Ce changelog couvre les dernières améliorations apportées aux tests d'authentification et de création de salles Tchap, en utilisant Playwright. Les modifications incluent des corrections de bugs, des mises à jour de documentation, et l'intégration de nouveaux outils de linting (Biome) pour améliorer la qualité du code. Une mise à jour de Playwright a également été effectuée pour bénéficier des dernières fonctionnalités et corrections.

### Évolutions fonctionnelles
- Correction du test de déconnexion pour assurer un fonctionnement correct.
- Correction de la création de salle, résolvant le problème signalé dans l'issue [#40](https://github.com/tchapgouv/tchap-e2e-playwright/issues/40).
- Mise à jour du code de vérification dans les tests pour une meilleure fiabilité.
- Suppression de la création de comptes hérités sans MAS (Matrix Authentication Service), simplifiant le processus d'authentification.

### Évolutions techniques
- Mise à jour de Playwright vers la version v1.59.1-noble, via l'image Docker `mcr.microsoft.com/playwright:v1.59.1-noble` (voir [#38](https://github.com/tchapgouv/tchap-e2e-playwright/issues/38)).
- Intégration de Biome comme outil de linting pour améliorer la qualité et la cohérence du code (voir [#36](https://github.com/tchapgouv/tchap-e2e-playwright/issues/36)).
- Déplacement du module vers le dossier `synapse`.

### Autres changements
- Amélioration de la documentation README.md avec des informations sur l'utilisation de Docker.
- Ajout de documentation pour l'utilisation de Docker.
- Ajout de tests int02.
