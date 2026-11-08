## Changelog : accounts (30 derniers jours, au 05 novembre 2026)

### Résumé
Cette période a été marquée par un renforcement de la gestion des utilisateurs et de l'administration, une stabilisation des processus d'authentification OIDC et une amélioration significative de la visibilité technique (observabilité) du système.

### Évolutions fonctionnelles
- **Administration** : 
    - Ajout de filtres pour identifier les utilisateurs dont l'email n'est pas normalisé.
    - Mise en place d'une interface en lecture seule pour la gestion des fournisseurs d'identité.
    - Correction d'un plantage lors d'échecs de connexion à l'interface d'administration Django.
- **Authentification & OIDC** : 
    - Amélioration du processus de déconnexion (meilleure gestion des jetons invalides et réduction des redirections frontend).
    - Support du scope de rôles ProConnect et suivi des rôles d'agents.
    - Corrections sur les paramètres de réponse OIDC (`iss` et `sub`).
- **Expérience utilisateur** : 
    - Intégration du logo "Projets" sur la page de connexion.
    - Normalisation systématique des adresses email pour garantir une correspondance cohérente des comptes.

### Évolutions techniques
- **Observabilité** : Mise en place du traçage et du profilage avec Sentry, et activation des spans Django pour un meilleur suivi des performances.
- **CI/CD & Infrastructure** : 
    - Optimisation des pipelines de CI : build natif des assets frontend (sans QEMU) et gestion optimisée du cache pour les navigateurs Playwright.
    - Ajout d'un environnement `Sandbox` et d'une tâche planifiée (cron job) via Helm.
- **Stabilité & Dépendances** : 
    - Stabilisation de la compatibilité avec `python-social-auth` (retour à la version 6.x suite à des instabilités avec la v7).
    - Mises à jour de Redis, Celery et Pylint.
- **Tests** : Résolution de tests instables (*flaky tests*) concernant l'OIDC et l'API de recherche utilisateur.

### Autres changements
- Nettoyage du code (suppression de fonctions inutilisées).
- Harmonisation du formatage du changelog et de la documentation.
