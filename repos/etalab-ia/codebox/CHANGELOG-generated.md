## Changelog : codebox (30 derniers jours, au 14 novembre 2026)

### Résumé
Ce mois a marqué un tournant majeur pour le projet avec le renommage officiel de `just-code` en `codebox`. L'expérience utilisateur a été profondément remaniée grâce à un nouvel assistant de configuration (wizard) plus intuitif et une interface en ligne de commande plus stable. Le système est désormais plus robuste, notamment grâce à de nouvelles capacités de récupération de données en cas d'interruption et une meilleure gestion des modèles d'IA.

### Évolutions fonctionnelles
- **Changement de nom :** Renommage global de `just-code` vers `codebox` (incluant le CLI, les chemins et les modules). **Attention : ce changement est une rupture de compatibilité.**
- **Assistant de configuration (Wizard) :** 
    - Introduction d'un nouvel assistant interactif pour la première installation et la configuration des modèles.
    - Ajout d'un écran de récapitulatif permettant de valider ou modifier les choix avant l'application.
    - Intégration d'étapes dédiées pour la configuration de l'accès GitHub et de la clé API Albert.
- **Gestion des modèles :** 
    - Support de la sélection de plusieurs modèles.
    - Ajout du modèle Ministral comme option de petit modèle via OpenCode.
- **Interface utilisateur (TUI) :** 
    - Amélioration de la stabilité de l'interface terminal (gestion du curseur et du redimensionnement des listes).
    - Polissage des textes et des messages de confirmation en français.
- **Fin de session :** Nouvel écran de fin de session permettant de récupérer les modifications en cours.
- **Harnais d'agent :** Support de "Pi" comme second harnais d'agent ([#176](https://github.com/etalab-ia/codebox/issues/176)).
- **Statistiques :** Mise en place de la collecte de statistiques d'usage soumise au consentement de l'utilisateur.

### Évolutions techniques
- **Récupération et Workspace :** 
    - Implémentation d'un mécanisme de récupération transactionnelle pour le workspace.
    - Amélioration de la gestion des conflits entre les modifications de l'hôte et celles de l'agent lors d'une reprise après interruption.
- **Microsandbox :** 
    - Mise à jour du runtime Microsandbox (v0.7.14).
    - Ajout d'un chemin de récupération spécifique pour les instances Microsandbox arrêtées lors d'une mise à jour.
- **Sécurité et Secrets :** 
    - Amélioration de la détection des secrets (le détecteur est désormais fourni directement au lieu d'être sollicité auprès de l'hôte).
    - Renforcement des mécanismes de validation des fichiers et des configurations du projet pour prévenir l'exécution de code non approuvé.
- **Architecture et Infrastructure :** 
    - Restructuration du dépôt en monorepo avec le déplacement du CLI dans `apps/codebox`.
    - Introduction de Moon v2 et de nouveaux scaffolds pour la gestion du projet.
    - Migration vers OpenCode v2.2.5.

### Autres changements
- **Documentation :** Mise à jour massive de la documentation, notamment sur les protocoles de qualification (macOS, Linux, Windows) et la gestion des secrets.
- **Localisation :** Travail important de traduction et d'harmonisation des messages système en français.
