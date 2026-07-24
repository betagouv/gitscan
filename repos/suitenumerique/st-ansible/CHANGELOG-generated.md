## Changelog : st-ansible (30 derniers jours, au 22 juillet 2026)

### Résumé
Cette nouvelle version apporte des améliorations significatives pour faciliter le déploiement de La Suite Territoriale, notamment en permettant des installations sur des machines uniques. Un outil en ligne de commande, `st-cli`, a été ajouté pour simplifier la gestion des environnements. Des ajustements ont également été effectués sur la configuration de Rspamd et de Drive pour une meilleure stabilité et flexibilité.

### Évolutions fonctionnelles
- Ajout de l'outil en ligne de commande `st-cli` pour la gestion des environnements LST [#27](https://github.com/suitenumerique/st-ansible/issues/27).
- Correction du port par défaut du contrôleur rspamd dans les rôles.
- Correction des noms de composition pour les configurations mono-hôte.
- Possibilité de configurer le nombre de lignes d'historique et de redirecteurs pour `st_messages_mpa_rspamd`.
- Ajout de variables pour configurer les scores `add_header` et `rewrite_subject` dans Rspamd, et désactivation du greylisting.
- Correction de la configuration Nginx et des valeurs par défaut dans le rôle Drive.
- Possibilité de désactiver le module `dkim_signing` dans Rspamd.

### Évolutions techniques
- Refactorisation des UID, GID et ports dans les rôles pour permettre des déploiements sur une seule machine [#26](https://github.com/suitenumerique/st-ansible/issues/26).
- Mise à jour de Restic vers la version 0.19.1 et correction du workflow de mise à niveau.
- Mise à jour de plusieurs actions GitHub vers leurs dernières versions.
- Ajout de la configuration Renovate pour la gestion automatisée des dépendances.
- Intégration de `antsibull-changelog` pour la génération automatique du changelog.

### Autres changements
- Ajout de références à `st-cli` dans le fichier README.
- Ajout d'un Makefile target pour Renovate.
