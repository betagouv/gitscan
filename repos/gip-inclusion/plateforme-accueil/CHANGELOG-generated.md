## Changelog : plateforme-accueil (30 derniers jours, au 27 juillet 2026)

### Résumé
Ce mois-ci, la plateforme a subi une refonte majeure de sa page d'accueil, passant d'une structure imbriquée à une approche plus directe avec l'intégration de la maquette directement en page. Des améliorations significatives ont également été apportées à la configuration et à l'infrastructure du projet, incluant l'ajout de CI/CD, de linters et de règles de contribution.

### Évolutions fonctionnelles
- La page d'accueil affiche désormais la maquette directement, sans iframe imbriquée. [#3](https://github.com/gip-inclusion/plateforme-accueil/pull/3)
- Un exemple HTML a été ajouté pour faciliter la visualisation et la collaboration.
- La plateforme intègre désormais le gestionnaire de tags Matomo pour le suivi analytique.
- La plateforme utilise un template de base commun à toutes les pages.
- La plateforme permet de définir des `frame-ancestors` supplémentaires via une variable d'environnement pour une meilleure gestion de la sécurité.
- Un avertissement est affiché si l'attribut `scrolling="no"` est utilisé sur l'iframe d'intégration.

### Évolutions techniques
- Refonte complète de l'architecture du projet avec l'utilisation de Django pour le rendu de la page d'accueil.
- Mise en place d'un pipeline CI/CD avec des workflows pour les tests et le déploiement.
- Ajout d'un Dockerfile et d'un Makefile pour faciliter le développement et le déploiement.
- Intégration des outils de linting `ruff` et de formatage `uv` pour garantir la qualité du code.
- Ajout de tests avec `pytest`.
- Les commentaires du code sont désormais écrits en anglais, conformément aux standards du projet les-emplois.
- Le sprite SVG est intégré en ligne pour éviter les problèmes de sécurité liés aux iframes avec des origines opaques.
- Amélioration de la gestion de la taille du contenu pour éviter les problèmes de "viewport ratchet".
- Version du setup-uv action épinglée pour garantir la stabilité.

### Autres changements
- Ajout d'un fichier `CLAUDE.md` contenant les règles de contribution.
- Ajout d'un fichier `README.md` pour une meilleure documentation du projet.
- Ignorer le dossier `docs/explorations` pour éviter de versionner des notes locales.
