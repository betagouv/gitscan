## Changelog : st-ansible (30 derniers jours, au 26 juillet 2026)

### Résumé
Cette nouvelle version apporte des améliorations significatives à la gestion des environnements La Suite Territoriale. Elle inclut l'introduction d'un outil en ligne de commande (st-cli) pour simplifier le déploiement et la gestion, ainsi que des refactorings pour permettre des installations sur une seule machine. Des corrections et des mises à jour de versions de composants ont également été intégrées.

### Évolutions fonctionnelles
- Introduction de l'outil `st-cli` pour la gestion des environnements LST. [#27](https://github.com/suitenumerique/st-ansible/issues/27)
- Ajout de la gestion des enregistrements des réunions (meet) et personnalisation du logo.
- Possibilité d'utiliser des marqueurs `@openbao` sur des champs non sensibles avec `st-cli`.
- Amélioration de la configuration de Rspamd avec l'ajout de scores et la désactivation du greylisting.

### Évolutions techniques
- Refactorisation des rôles pour permettre des déploiements sur une seule machine en ajustant les UID, GID et ports. [#26](https://github.com/suitenumerique/st-ansible/issues/26)
- Mise en place de la configuration Renovate pour la gestion automatisée des dépendances.
- Intégration d'antsibull-changelog pour la génération automatique du changelog.
- Mise à jour de plusieurs actions GitHub (checkout, docker/login, setup-python, etc.) vers leurs dernières versions.
- Mise à jour de Restic vers la version 0.19.1 et correction du workflow de mise à niveau.
- Mise à jour de Podman vers la version 1.20.2 et Ansible.posix vers la version 2.2.2.

### Autres changements
- Ajout de références à `st-cli` dans le fichier README.
- Correction des noms de composition pour les configurations mono-hôte.
- Ajout de variables pour configurer le nombre de lignes d'historique et les redirecteurs de Rspamd.
- Correction du port par défaut du contrôleur Rspamd.
