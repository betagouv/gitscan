## Changelog : plateforme-accueil (30 derniers jours, au 27 juillet 2026)

### Résumé
Ce mois-ci, la plateforme a subi une refonte majeure de sa page d'accueil, passant d'une structure imbriquée à une approche plus directe avec l'intégration de la maquette. Des améliorations significatives ont également été apportées à la configuration et à l'infrastructure du projet, incluant l'ajout de CI/CD, de linters et de règles de contribution.

### Évolutions fonctionnelles
- La page d'accueil affiche désormais directement la maquette, simplifiant l'intégration et l'expérience utilisateur. [#3](https://github.com/gip-inclusion/plateforme-accueil/pull/3)
- Un exemple HTML a été ajouté pour faciliter la visualisation et la compréhension de la structure de la page.
- La maquette d'exemple est désormais affichée en iframe sous le titre d'accueil.
- La plateforme est désormais compatible avec l'intégration dans des iframes sécurisés, avec la possibilité de configurer les directives `frame-ancestors` via une variable d'environnement.
- Ajout du gestionnaire de balises Matomo pour le suivi analytique.

### Évolutions techniques
- Refonte complète de l'architecture du projet avec l'utilisation de Django pour le rendu de la page d'accueil et une approche plus directe de l'intégration en iframe.
- Mise en place d'un pipeline CI/CD avec des workflows pour les tests et le déploiement.
- Intégration de `ruff` pour le linting du code et `pytest` pour les tests unitaires.
- Utilisation de `uv` pour la gestion des dépendances et l'optimisation des performances.
- Ajout d'un `Dockerfile` et d'un `Makefile` pour faciliter le développement et le déploiement.
- Le code est maintenant commenté en anglais pour une meilleure cohérence avec d'autres projets.
- Amélioration de la gestion de la taille du contenu dans les iframes pour éviter les problèmes de décalage visuel.
- Les icônes SVG sont désormais intégrées en ligne pour garantir leur affichage correct dans les iframes avec des restrictions d'origine.

### Autres changements
- Ajout d'un fichier `CLAUDE.md` contenant les règles de contribution au projet.
- Mise à jour de la documentation et du fichier `README` pour refléter les changements récents.
- Suppression des fichiers d'exploration locaux pour maintenir un dépôt propre.
- Avertissement ajouté concernant l'utilisation de `scrolling="no"` sur l'iframe d'intégration.
