## Changelog : just-code (30 derniers jours, au 10 septembre 2026)

### Résumé
Le projet a considérablement évolué, passant d'une expérimentation initiale basée sur Docker à un environnement de test multi-runtimes plus flexible. Il permet désormais de choisir entre différents types d'environnements isolés (sandboxes), incluant l'ajout du support pour macOS, ce qui ouvre de nouvelles possibilités de tests pour les agents de code.

### Évolutions fonctionnelles
- **Multi-runtimes :** Possibilité de sélectionner explicitement le runtime de la sandbox à utiliser (Microsandbox, Tart, etc.) [#2](https://github.com/etalab-ia/just-code/pull/2).
- **Support macOS :** Ajout du runtime macOS via Tart, permettant notamment des tests liés à Xcode [#4](https://github.com/etalab-ia/just-code/pull/4).
- **Amélioration de l'expérience utilisateur :**
    - Passage par défaut sur macOS Tahoe avec un système de nommage plus stable.
    - Ajout de la possibilité de configurer la MTU pour assurer la compatibilité avec les connexions VPN.

### Évolutions techniques
- **Nouveaux environnements :** Intégration de Microsandbox comme alternative à Docker [#2](https://github.com/etalab-ia/just-code/pull/2).
- **Stabilité du runtime Tart :**
    - Correction de la gestion des mots de passe et des requêtes réseau (curl).
    - Optimisation de la fiabilité du backend (gestion des sondes de santé, rafraîchissement du bootstrap et cycle de vie des VM).
    - Résolution de problèmes de réseau et de partage restreint suite aux revues de code.
- **Refactorisation :**
    - Simplification du nommage des machines virtuelles Tart.
    - Renommage de la commande de démarrage (la recette `up` devient `start`).

### Autres changements
- **Identité du projet :** Renommage officiel du dépôt en `just-code`, ajout d'une licence MIT et mise à jour du README.
- **Documentation :** Mise à jour des instructions d'installation pour le composant Tart.
