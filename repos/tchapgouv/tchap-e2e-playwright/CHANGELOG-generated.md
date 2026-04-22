## Changelog : tchap-e2e-playwright (30 derniers jours, au 2026-04-20)

### Résumé
Ce changelog présente les améliorations apportées aux tests d'authentification OIDC avec Keycloak et aux tests Tchap minimaux. Les changements incluent des tests pour la réactivation silencieuse de compte, la suppression de la création de comptes hérités sans MAS, et une documentation améliorée pour l'utilisation de Docker. Une mise à jour de l'image Playwright a également été effectuée.

### Évolutions fonctionnelles
- Ajout de tests pour la réactivation silencieuse de compte. [#35](https://github.com/tchapgouv/tchap-e2e-playwright/issues/35)
- Suppression de la création de comptes hérités sans MAS, simplifiant ainsi le processus d'authentification. [#36](https://github.com/tchapgouv/tchap-e2e-playwright/issues/36)

### Évolutions techniques
- Mise à jour de l'image Docker Playwright vers la version v1.59.1-noble pour bénéficier des dernières corrections et améliorations. [#38](https://github.com/tchapgouv/tchap-e2e-playwright/issues/38)
- Restructuration de certains fichiers pour une meilleure organisation du projet.

### Autres changements
- Amélioration de la documentation README pour inclure des instructions sur l'utilisation de Docker.
- Ajout de documentation pour l'utilisation de Docker.
- Déplacement de fichiers vers un niveau supérieur dans l'arborescence du projet.
