## Changelog : menshen (30 derniers jours, au 22 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'implémentation de la fonctionnalité d'échange de jetons OAuth 2.0, une fonctionnalité clé du projet.  Des refactorings ont également été effectués pour préparer l'arrivée de cette nouvelle fonctionnalité et améliorer la maintenance du code.

### Évolutions fonctionnelles
- Implémentation d'une première version de l'échange de jetons OAuth 2.0. [#1234](https://github.com/suitenumerique/menshen/issues/1234) (implémentation en cours)

### Évolutions techniques
- Refactoring de l'application `tx` et déplacement vers un nouveau module `token_exchange` pour une meilleure organisation du code.
- Mise à jour de la version de Python utilisée pour le packaging.
- Suppression de l'application API, probablement en anticipation de la nouvelle fonctionnalité d'échange de jetons.
- Fixation de la version de PostgreSQL à 16 pour assurer la stabilité de l'environnement.

### Autres changements
- Mise à jour des dépendances GitHub Actions.
- Mise à jour de l'image Docker `ghcr.io/astral-sh/uv` vers la version v0.11.2.
- Mise à jour des dépendances Python.
