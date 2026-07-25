## Changelog : api-relay-cnav (30 derniers jours, au 24 juillet 2026)

### Résumé
Ce mois-ci, le projet a connu des avancées significatives dans la mise en place de l'infrastructure API, notamment l'ajout de l'authentification par token, la création d'une structure de projet Django robuste avec une application utilisateurs personnalisée, et l'amélioration de l'environnement de développement local avec Docker. Des mesures de sécurité ont également été implémentées avec l'ajout d'une configuration CSP.

### Évolutions fonctionnelles
- Ajout d'une application "users" avec un modèle utilisateur personnalisé, permettant la gestion des utilisateurs de l'API. [#26079bc](https://github.com/gip-inclusion/api-relay-cnav/commit/26079bc)
- Implémentation de l'authentification par token pour sécuriser l'accès à l'API. [#7578f38](https://github.com/gip-inclusion/api-relay-cnav/commit/7578f38)
- Création d'un stub d'API initial pour définir les bases de l'exposition des fonctionnalités. [#7c91e14](https://github.com/gip-inclusion/api-relay-cnav/commit/7c91e14)
- Ajout d'un healthcheck basique pour surveiller l'état de l'application. [#d4610dc](https://github.com/gip-inclusion/api-relay-cnav/commit/d4610dc)
- Intégration d'un client InterOps. [#57710e7](https://github.com/gip-inclusion/api-relay-cnav/commit/57710e7)

### Évolutions techniques
- Mise à jour de la version de PostgreSQL dans les conteneurs Docker de 18 à 17 pour une meilleure compatibilité. [#8c6424f](https://github.com/gip-inclusion/api-relay-cnav/commit/8c6424f)
- Amélioration de l'environnement de développement local avec Docker, incluant la persistance de l'historique bash/python. [#23253a9](https://github.com/gip-inclusion/api-relay-cnav/commit/23253a9) et [#791f689](https://github.com/gip-inclusion/api-relay-cnav/commit/791f689)
- Ajout d'une configuration de Content Security Policy (CSP) pour renforcer la sécurité de l'application. [#07d9a30](https://github.com/gip-inclusion/api-relay-cnav/commit/07d9a30)
- Mise en place d'un template pour les pull requests sur GitHub. [#b4f09a2](https://github.com/gip-inclusion/api-relay-cnav/commit/b4f09a2)
- Ajout d'une commande pour accorder des privilèges à l'application. [#bac38cf](https://github.com/gip-inclusion/api-relay-cnav/commit/bac38cf)
- Ajout de modèles abstraits utilitaires pour faciliter le développement. [#5e04d41](https://github.com/gip-inclusion/api-relay-cnav/commit/5e04d41)

### Autres changements
- Configuration de Dependabot pour la gestion des dépendances. [#04b187a](https://github.com/gip-inclusion/api-relay-cnav/commit/04b187a)
- Ajout d'un check GitHub pour détecter les commits de type "fixup". [#378d857](https://github.com/gip-inclusion/api-relay-cnav/commit/378d857)
- Suppression d'un test inutile. [#6e0cd76](https://github.com/gip-inclusion/api-relay-cnav/commit/6e0cd76)
- Initialisation du projet Django. [#903ce37](https://github.com/gip-inclusion/api-relay-cnav/commit/903ce37)
- Exclusion de certains linters Ruff pour les migrations et les tests. [#622b8c6](https://github.com/gip-inclusion/api-relay-cnav/commit/622b8c6)
