## Changelog : st-ansible (30 derniers jours, au 26 juillet 2026)

### Résumé
Cette nouvelle version apporte des améliorations significatives à la gestion des environnements La Suite Territoriale. L'introduction de `st-cli` simplifie le bootstrap et le déploiement, tandis que des refactorings permettent désormais de déployer facilement sur des machines uniques. Des corrections et mises à jour de versions de composants améliorent la stabilité et la sécurité.

### Évolutions fonctionnelles
- Introduction de l'outil en ligne de commande `st-cli` pour gérer le bootstrap et les déploiements. [#27](https://github.com/suitenumerique/st-ansible/issues/27)
- Possibilité d'utiliser des marqueurs `@openbao` sur les champs non sensibles dans `st-cli`.
- Ajout de la gestion des enregistrements pour les réunions (meet).
- Ajout de variables pour configurer le nombre de lignes d'historique et les redirecteurs pour mpa-rspamd.
- Ajout de variables pour configurer les scores de rejet et la désactivation du module dkim_signing pour rspamd.
- Amélioration de la configuration Nginx et des valeurs par défaut pour drive.

### Évolutions techniques
- Refactorisation des rôles pour permettre des déploiements sur des machines uniques en ajustant les UID, GID et ports. [#26](https://github.com/suitenumerique/st-ansible/issues/26)
- Mise à jour de Restic vers la version 0.19.1 et correction du workflow de mise à niveau.
- Mise à jour de plusieurs actions GitHub (checkout, docker/login, setup-python, etc.) vers leurs dernières versions.
- Ajout de la configuration Renovate pour la gestion automatisée des dépendances.
- Intégration d'antsibull-changelog pour la génération automatique du changelog.
- Correction du port par défaut du contrôleur rspamd dans les rôles.
- Correction des noms de composition pour les configurations mono-hôte.

### Autres changements
- Ajout de références à `st-cli` dans le fichier README.
- Ajout de la documentation et des enregistrements de la réunion du 25 juillet.
- Mise à jour des dépendances containers.podman (1.20.2) et ansible.posix (2.2.2).
- Mise à jour de l'image Livekit Server (v1.13.4).
- Ajout de la gestion des logos personnalisés pour meet.
- Séparation du composant egress pour meet et ajout de la fonctionnalité d'enregistrement.
