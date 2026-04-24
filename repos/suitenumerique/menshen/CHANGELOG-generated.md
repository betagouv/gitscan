## Changelog : menshen (30 derniers jours, au 22 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'implémentation initiale de la fonctionnalité d'échange de jetons OAuth 2.0, qui constitue le cœur de métier de Menshen. Des refactorings ont été effectués pour préparer l'arrivée de cette fonctionnalité et simplifier la structure du projet. Des mises à jour de configuration et de dépendances ont également été réalisées pour assurer la stabilité et la sécurité du système.

### Évolutions fonctionnelles
- Implémentation d'une première version de l'échange de jetons OAuth 2.0. [#1234](https://github.com/suitenumerique/menshen/issues/1234) (implémentation en cours)

### Évolutions techniques
- Refactorisation de la structure des applications, déplacement de l'application `tx` vers `token_exchange` pour une meilleure organisation.
- Suppression de l'application `api` qui n'était plus nécessaire.
- Mise à jour de la version de Python utilisée pour le packaging.
- Fix de la configuration de Renovate pour une gestion plus précise des dépendances.
- Épingle de la version de PostgreSQL à la version 16 pour garantir la stabilité.
- Activation du gestionnaire Docker de Renovate pour automatiser les mises à jour des images Docker.

### Autres changements
- Correction d'un bug où le manager était activé par catégorie au lieu de son nom.
- Correction de la configuration de Renovate.
- Mise à jour des dépendances GitHub Actions et des images Docker `ghcr.io/astral-sh/uv` et `quay.io/keycloak/keycloak`.
