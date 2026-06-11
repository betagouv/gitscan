## Changelog : dahlia (30 derniers jours, au 2026-06-09)

### Résumé
Ce changelog présente la création et les premières évolutions de l'application web DAHLIA, destinée à la gestion des dossiers DALO, DAHO et DAHU. Les efforts se sont concentrés sur la mise en place de l'infrastructure, l'intégration du SSO ProConnect, l'amélioration du processus de récupération des dossiers via le scraping, et la correction de bugs liés à l'anonymisation et à la déconnexion.

### Évolutions fonctionnelles
- Intégration du Single Sign-On (SSO) ProConnect pour l'authentification des utilisateurs [#7](https://github.com/MTES-MCT/dahlia/issues/7).
- Mise en place du scraping de tous les types de dossiers, avec anonymisation des données sensibles [#5](https://github.com/MTES-MCT/dahlia/issues/5) et [#6](https://github.com/MTES-MCT/dahlia/issues/6).
- Amélioration de la robustesse du scraping avec un mécanisme de ré-essai en cas d'erreurs temporaires [#8](https://github.com/MTES-MCT/dahlia/issues/8).
- Correction d'un bug empêchant l'anonymisation complète des données [#11](https://github.com/MTES-MCT/dahlia/issues/11).
- Correction d'un problème de déconnexion automatique après la connexion [#10](https://github.com/MTES-MCT/dahlia/issues/10).

### Évolutions techniques
- Première version de l'application web déployée sur Scalingo [#1](https://github.com/MTES-MCT/dahlia/issues/1) et [#3](https://github.com/MTES-MCT/dahlia/issues/3).
- Ajout de `ts-node` comme dépendance de production pour le scraping [#9](https://github.com/MTES-MCT/dahlia/issues/9).
- Correction d'un problème lié au checkout avant le déploiement [#4](https://github.com/MTES-MCT/dahlia/issues/4).
- Initialisation du dépôt avec un premier commit [#1](https://github.com/MTES-MCT/dahlia/commit/abcac2c).

### Autres changements
- Mise à jour de la configuration du gestionnaire de paquets pour utiliser npm [#2](https://github.com/MTES-MCT/dahlia/issues/2).
