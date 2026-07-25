## Changelog : plateforme-accueil (30 derniers jours, au 24 juillet 2026)

### Résumé
Ce mois-ci, la plateforme a subi une refonte majeure de sa page d'accueil, passant d'une structure imbriquée à une approche plus directe avec l'intégration de la maquette directement dans la page. Des améliorations ont également été apportées à la sécurité (CSP) et à l'intégration dans des iframes, ainsi qu'une mise en place des outils de CI/CD et de linting.

### Évolutions fonctionnelles
- La page d'accueil affiche maintenant la maquette d'exemple directement, sans iframe imbriquée. [#3](https://github.com/gip-inclusion/plateforme-accueil/pull/3)
- Intégration d'un script pour faciliter l'intégration de la plateforme dans des iframes, avec une gestion de la politique de sécurité du contenu (CSP) plus flexible via une variable d'environnement.
- Ajout d'un exemple HTML pour faciliter la visualisation de la maquette.
- Le gestionnaire de balises Matomo est maintenant chargé dans l'en-tête de chaque page.
- Mise en place d'un template de base commun à toutes les pages.

### Évolutions techniques
- Refonte complète de l'architecture du projet avec l'utilisation de Django pour le rendu de la page d'accueil.
- Mise en place d'un pipeline CI/CD avec GitHub Actions.
- Ajout d'un Dockerfile et d'un Makefile pour faciliter le développement et le déploiement.
- Utilisation de `uv`, `ruff` et `pytest` pour le développement et les tests.
- Les commentaires dans le code sont maintenant écrits en anglais, comme sur le projet "les-emplois".
- Amélioration de la gestion de la taille du contenu dans les iframes pour éviter les problèmes de redimensionnement.
- Les icônes SVG sont maintenant intégrées directement dans le HTML pour assurer leur affichage même dans des iframes avec des restrictions d'origine.
- Avertissement ajouté pour déconseiller l'utilisation de `scrolling="no"` sur l'iframe d'intégration.

### Autres changements
- Ajout d'un fichier `CLAUDE.md` contenant les règles d'utilisation de l'IA Claude.
- Ajout d'un fichier README.
- Suppression de certains fichiers de documentation locaux non pertinents.
- Fixation de la version de l'action `setup-uv` pour assurer la stabilité.
