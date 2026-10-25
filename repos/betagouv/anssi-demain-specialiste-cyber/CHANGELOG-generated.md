## Changelog : anssi-demain-specialiste-cyber (30 derniers jours, au 23 octobre 2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape importante avec l'ajout de nouveaux parcours pédagogiques via la section "Se former et s'entraîner". L'identité visuelle a été ajustée et une vaste opération de nettoyage technique a été menée pour moderniser le code et améliorer la stabilité de l'environnement de développement.

### Évolutions fonctionnelles
- **Nouveaux contenus** : Implémentation de la page "Se former et s'entraîner en ligne" et de sa route dédiée.
- **Nouveaux services** : Mise à disposition d'API pour les parcours de sélection "Je me mesure" et "Je m'entraîne".
- **Améliorations de l'interface** :
    - Optimisation de l'affichage du mode sombre.
    - Corrections de textes (wording) sur la page d'accueil et les sections de présentation.
    - Correction de l'affichage du bloc "Comment ça marche ?".
    - Mise en place d'une image générique pour pallier l'absence d'illustrations.
- **Identité visuelle** : Retrait du logo et de la tagline "Innovation ANSSI" de l'en-tête.

### Évolutions techniques
- **Refactoring et nettoyage** : Suppression massive de surcharges de types inutiles sur de nombreuses bibliothèques (Axios, Svelte, Lodash, etc.) pour alléger le projet.
- **Modernisation du socle** : 
    - Migration de la configuration Vitest vers le format ESM.
    - Utilisation de standards plus récents pour les configurations Vite (`import.meta.dirname`).
- **Outillage de développement** :
    - Introduction de Nix pour la gestion de l'environnement de travail (shell Nix).
    - Automatisation du tri des imports.
    - Centralisation des instructions pour les agents d'IA.
- **Infrastructure et CI/CD** :
    - Mise à jour de l'environnement de CI vers Ubuntu 26.04.
    - Mise à jour de plusieurs workflows GitHub Actions.
- **Maintenance et sécurité** :
    - Mise à jour de dépendances critiques (Svelte, Knex, Axios, Zod, etc.).
    - Nettoyage des logs de debug liés à l'authentification.

### Autres changements
- **Documentation** : Réorganisation complète du guide de développement pour une meilleure lisibilité.
- **Configuration** : Optimisation du planning des mises à jour automatiques (Renovate).
