## Changelog : st-ansible (30 derniers jours, au 26 juillet 2026)

### Résumé
Cette nouvelle version apporte des améliorations significatives à la gestion des déploiements de La Suite Territoriale, notamment avec l'introduction d'un outil en ligne de commande (st-cli) pour simplifier les opérations de bootstrap et de déploiement. Des corrections et des refactorings ont également été effectués pour faciliter les déploiements sur des environnements mono-serveur.

### Évolutions fonctionnelles
- Ajout de l'outil `st-cli` pour la gestion des environnements LST (bootstrap et déploiement) [#27](https://github.com/suitenumerique/st-ansible/issues/27).
- Possibilité d'utiliser des marqueurs `@openbao` sur les champs non sensibles dans `st-cli`.
- Ajout de la gestion des enregistrements des réunions (meet) et personnalisation du logo.
- Ajout de variables pour configurer le nombre de lignes d'historique et les redirecteurs pour le module mpa-rspamd.
- Ajout de variables pour configurer les scores de rejet et désactivation du module dkim_signing pour rspamd.
- Amélioration de la configuration Nginx et des valeurs par défaut pour le rôle drive.

### Évolutions techniques
- Refactorisation des rôles pour permettre des déploiements sur des serveurs uniques en ajustant les UID, GID et ports. [#26](https://github.com/suitenumerique/st-ansible/issues/26)
- Mise à jour de Restic vers la version 0.19.1 et correction du workflow de mise à niveau.
- Mise à jour des actions GitHub (checkout, docker/login, setup-python, etc.) vers leurs dernières versions.
- Ajout de la configuration Renovate pour la gestion automatisée des dépendances.
- Intégration d'antsibull-changelog pour la génération automatique du changelog.

### Autres changements
- Ajout de références à `st-cli` dans le README.
- Correction des messages du contrôleur rspamd concernant le port par défaut.
- Correction des noms de composition pour les configurations mono-hôte.
- Ajout de la configuration Renovate et d'une cible Makefile correspondante.
- Ajout d'enregistrements de la réunion du 25/07/2026.
