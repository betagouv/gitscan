## Changelog : api-relay-cnav (30 derniers jours, au 24 juillet 2026)

### Résumé
Ce mois-ci, le projet a connu une avancée significative avec la mise en place des fondations de l'API, incluant l'authentification par token et la structure de base. Des améliorations ont également été apportées à l'environnement de développement local avec l'utilisation de Docker et à la qualité du code grâce à l'intégration de linters et de modèles abstraits.

### Évolutions fonctionnelles
- Ajout d'un client InterOps.
- Mise en place d'une authentification par token pour l'API. [#7578f38](https://github.com/gip-inclusion/api-relay-cnav/commit/7578f38)
- Création d'un stub d'API initial. [#7c91e14](https://github.com/gip-inclusion/api-relay-cnav/commit/7c91e14)
- Ajout d'une configuration de Content Security Policy (CSP) pour renforcer la sécurité. [#07d9a30](https://github.com/gip-inclusion/api-relay-cnav/commit/07d9a30)
- Ajout d'une application "users" avec un modèle utilisateur personnalisé. [#26079bc](https://github.com/gip-inclusion/api-relay-cnav/commit/26079bc)
- Ajout d'un healthcheck basique pour la surveillance de l'application. [#d4610dc](https://github.com/gip-inclusion/api-relay-cnav/commit/d4610dc)

### Évolutions techniques
- Intégration de bibliothèques DRF (Django REST Framework). [#9e4a970](https://github.com/gip-inclusion/api-relay-cnav/commit/9e4a970)
- Amélioration de l'environnement de développement local avec Docker, incluant la persistance de l'historique bash/python. [#791f689](https://github.com/gip-inclusion/api-relay-cnav/commit/791f689) et [#23253a9](https://github.com/gip-inclusion/api-relay-cnav/commit/23253a9)
- Mise à jour de la version de PostgreSQL dans les conteneurs Docker (passage de 18 à 17). [#8c6424f](https://github.com/gip-inclusion/api-relay-cnav/commit/8c6424f)
- Ajout de modèles abstraits utilitaires pour améliorer la structure du code. [#5e04d41](https://github.com/gip-inclusion/api-relay-cnav/commit/5e04d41)
- Ajout d'une commande pour accorder des privilèges à l'application. [#bac38cf](https://github.com/gip-inclusion/api-relay-cnav/commit/bac38cf)
- Ajout d'un check GitHub pour détecter les commits de type "fixup". [#378d857](https://github.com/gip-inclusion/api-relay-cnav/commit/378d857)

### Autres changements
- Ajout d'un template pour les pull requests sur GitHub. [#b4f09a2](https://github.com/gip-inclusion/api-relay-cnav/commit/b4f09a2)
- Exclusion de certains linters Ruff pour les migrations et les tests. [#622b8c6](https://github.com/gip-inclusion/api-relay-cnav/commit/622b8c6)
