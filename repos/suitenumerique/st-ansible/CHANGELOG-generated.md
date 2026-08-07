## Changelog : st-ansible (30 derniers jours, au 05/08/2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante avec l'intégration de l'outil `st-cli` pour la gestion des environnements. Les capacités de déploiement ont été renforcées, notamment pour les configurations sur un seul hôte, et l'expérience utilisateur a été améliorée grâce à un affichage Ansible plus lisible et de nouvelles fonctionnalités pour le composant `meet`.

### Évolutions fonctionnelles
- **Intégration de `st-cli`** : Introduction de l'outil pour faciliter la gestion des bootstraps et des déploiements des environnements LST.
- **Gestion des secrets** : Possibilité d'utiliser des marqueurs `@openbao` sur des champs non-secrets via la CLI.
- **Composant `meet`** : Ajout de la fonctionnalité de gestion des enregistrements.
- **Optimisation des rôles `messages`** : 
    - Correction du port par défaut du contrôleur Rspamd.
    - Correction des noms de services Compose pour les installations sur un seul hôte.
    - Ajout de nouvelles variables de configuration pour MPA (historique et redirecteurs Rspamd).
- **Déploiements simplifiés** : Amélioration globale de la compatibilité pour les déploiements sur un seul hôte (single-host).

### Évolutions techniques
- **Nouveau plugin Ansible** : Ajout du callback `compact` pour un affichage plus concis et lisible des tâches en console (une ligne par tâche/hôte avec suivi de progression).
- **Refactorisation système** : Révision des UID, GID et des ports pour permettre des déploiements fluides sur une machine unique.
- **CI/CD** : 
    - Optimisation de la stratégie de publication des tags pour s'aligner sur la collection `st-cli`.
    - Correction du workflow de mise à jour pour `restic`.

### Autres changements
- **Documentation** : Amélioration de la documentation concernant la CLI, les procédures de mise à jour et ajout de références dans le README.
- **Outils et automatisation** : 
    - Mise en place de `antsibull-changelog` pour la génération automatique des notes de version.
    - Configuration de Renovate pour la gestion automatisée des dépendances.
