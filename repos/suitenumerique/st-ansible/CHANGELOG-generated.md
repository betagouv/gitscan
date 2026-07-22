## Changelog : st-ansible (30 derniers jours, au 21 juillet 2026)

### Résumé
Cette nouvelle version apporte des améliorations significatives pour faciliter le déploiement de La Suite Territoriale, notamment en permettant des installations sur des serveurs uniques. Une interface en ligne de commande (CLI) a été ajoutée pour simplifier la gestion des environnements. Des ajustements ont également été faits aux rôles existants pour une meilleure configuration et des options plus flexibles.

### Évolutions fonctionnelles
- Ajout de l'interface en ligne de commande `st-cli` pour la gestion des environnements LST. [#27](https://github.com/suitenumerique/st-ansible/issues/27)
- Possibilité de configurer le nombre de lignes conservées pour l'historique de RSPAMD via la variable `st_messages_mpa_rspamd_history_nrows`.
- Possibilité de configurer le nombre de redirecteurs RSPAMD via la variable `st_messages_mpa_rspamd_redirectors`.
- Configuration améliorée de Nginx dans le rôle `drive` avec des valeurs par défaut ajustées.
- Ajout de la variable `st_messages_mpa_rspamd_reject_score` pour contrôler le score de rejet de RSPAMD.
- Désactivation du module `dkim_signing` dans RSPAMD.

### Évolutions techniques
- Refactorisation des rôles pour permettre des déploiements sur des serveurs uniques en ajustant les UID, GID et ports. [#26](https://github.com/suitenumerique/st-ansible/issues/26)
- Correction du port par défaut du contrôleur RSPAMD dans le rôle `rspamd`. [#92f8aea](https://github.com/suitenumerique/st-ansible/commit/92f8aea)
- Correction des noms de composition pour les configurations mono-hôte. [#504dbb0](https://github.com/suitenumerique/st-ansible/commit/504dbb0)
- Ajout de la configuration d'antsibull-changelog, Makefile et job CI pour la génération automatique du changelog. [#13](https://github.com/suitenumerique/st-ansible/issues/13)
- Ajout de la possibilité de configurer des en-têtes et de réécrire l'objet des emails dans RSPAMD. [#3ee8c3e](https://github.com/suitenumerique/st-ansible/commit/3ee8c3e)
- Désactivation du greylisting dans RSPAMD. [#3ee8c3e](https://github.com/suitenumerique/st-ansible/commit/3ee8c3e)
