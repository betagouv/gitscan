## Changelog : st-ansible (30 derniers jours, au 05/08/2026)

### Résumé
Ce mois-ci, le projet a franchi une étape majeure avec l'intégration de `st-cli` pour simplifier la gestion des déploiements. Les capacités de l'outil ont été enrichies, notamment avec la gestion des enregistrements pour les réunions et une meilleure visibilité lors de l'exécution des tâches Ansible grâce à un nouvel affichage compact.

### Évolutions fonctionnelles
- **Gestion des environnements** : Intégration de `st-cli` pour faciliter le pilotage des déploiements et des environnements.
- **Composant Meet** : Ajout de la prise en charge des enregistrements de réunions.
- **Sécurité** : Extension de l'utilisation des marqueurs `@openbao` aux champs non-secrets.
- **Correction** : Rectification du port par défaut du contrôleur Rspamd.

### Évolutions techniques
- **Interface Ansible** : Création et amélioration d'un nouveau plugin de callback ("compact") permettant un affichage plus clair et concis des tâches et de la progression.
- **Workflow de mise à jour** : Correction du processus de mise à jour pour Restic.
- **Automatisation CI/CD** : 
    - Optimisation de la publication des tags pour suivre la collection `st-cli`.
    - Mise en place de `antsibull-changelog` pour la génération automatique des notes de version.
    - Intégration de Renovate pour la gestion automatisée des dépendances.

### Autres changements
- **Documentation** : Amélioration de la documentation de l'interface en ligne de commande (CLI), des procédures de mise à jour et mise à jour du README avec les références à `st-cli`.
