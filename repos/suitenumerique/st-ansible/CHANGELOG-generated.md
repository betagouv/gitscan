## Changelog : st-ansible (30 derniers jours, au 10 août 2026)

### Résumé
Cette période a été marquée par l'intégration de l'outil `st-cli`, l'amélioration de la visibilité des tâches Ansible via un nouveau mode d'affichage compact, et la mise à jour de plusieurs composants de sécurité et de services (ClamAV, Valkey, Rspamd).

### Évolutions fonctionnelles
- **Intégration de la CLI** : Premier commit et intégration de l'outil `st-cli`.
- **Nouvelle interface Ansible** : Ajout d'un callback "compact" pour un affichage plus clair et concis des résultats de tâches.
- **Amélioration de la CLI** : Possibilité d'utiliser des marqueurs `@openbao` sur des champs non-secrets.
- **Module Meet** : Ajout du support pour les enregistrements.

### Évolutions techniques
- **Mise à jour des services (conteneurs)** : Actualisation des images Docker pour ClamAV (v1.5.4), Valkey (v9.1.1) et Rspamd (v4.1.4).
- **CI/CD & Automatisation** :
    - Mise en place de `antsibull-changelog` pour l'automatisation des notes de version.
    - Configuration de Renovate pour la gestion des dépendances.
    - Optimisation de la gestion des tags pour la CLI (push uniquement du tag `latest`).
- **Workflows** : Amélioration du workflow de mise à jour de Restic.

### Autres changements
- **Documentation** : Amélioration de la documentation de la CLI, des instructions de mise à jour et ajout de références à `st-cli` dans le README.
- **Maintenance** : Corrections mineures sur le rendu du changelog.
