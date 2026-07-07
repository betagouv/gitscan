## Changelog : sites-conformes (30 derniers jours, au 25 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à la publication et au déploiement du projet, notamment via l'automatisation du versionnement et de la publication sur PyPi. Des corrections de bugs ont également été implémentées, notamment concernant la gestion des images et des erreurs 500. Des améliorations de l'expérience utilisateur sont également visibles avec l'ajout de fonctionnalités dans l'interface d'administration.

### Évolutions fonctionnelles
- Amélioration de l'étape de publication pour une meilleure gestion des erreurs et une plus grande fiabilité. [#531](https://github.com/numerique-gouv/sites-conformes/issues/531)
- Correction d'une erreur 500 qui se produisait lors du changement de type d'en-tête avec une image d'arrière-plan. [#512](https://github.com/numerique-gouv/sites-conformes/issues/512)
- Ajout du choix de la balise d'en-tête (heading tag) dans le stepper d'administration.
- Ajout d'un titre sur les tags sélectionnés dans l'interface d'administration.
- Correction d'une erreur 500 liée à l'absence d'image. [#90da814](https://github.com/numerique-gouv/sites-conformes/commit/90da814)

### Évolutions techniques
- Mise en place du versionnement via GitHub Actions et publication sur PyPi. [#515](https://github.com/numerique-gouv/sites-conformes/issues/515)
- Amélioration de la recette de mise à niveau pour gérer le projet de démonstration. [#527](https://github.com/numerique-gouv/sites-conformes/issues/527)
- Mise en place du déploiement en un clic sur Scalingo (avec correction). [#487](https://github.com/numerique-gouv/sites-conformes/issues/487)
- Correction de la configuration Docker. [#519](https://github.com/numerique-gouv/sites-conformes/issues/519)
- Correction des erreurs de validation du fichier `publiccode.yml`. [#496](https://github.com/numerique-gouv/sites-conformes/issues/496)
- Amélioration des scripts de restauration et de téléchargement des médias (gestion des erreurs, verbosité).
- Ajout de commentaires pour faciliter le déploiement sur Scalingo.

### Autres changements
- Internationalisation (i18n) : Ajout et correction de traductions.
- Refactorisation et corrections mineures du code.
