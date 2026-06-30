## Changelog : sites-conformes (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, les évolutions de Sites Conformes se concentrent sur l'amélioration du processus de publication, la correction de bugs et la préparation du déploiement sur Scalingo. Des améliorations ont également été apportées à la gestion des médias et à la configuration du projet, notamment via l'automatisation du versionnement et de la publication sur PyPi.

### Évolutions fonctionnelles
- Correction d'une erreur 500 qui se produisait lors du changement de type d'en-tête avec une image d'arrière-plan. [#512](https://github.com/numerique-gouv/sites-conformes/issues/512)
- Correction d'une erreur 500 lors de l'absence d'image. [#531](https://github.com/numerique-gouv/sites-conformes/issues/531)
- Amélioration de la gestion des médias avec des noms de dossiers spécifiques pour la descente et la restauration des médias.
- Mise en place d'un déploiement en un clic sur Scalingo (avec correction). [#487](https://github.com/numerique-gouv/sites-conformes/issues/487)
- Ajout de la possibilité de choisir la balise d'en-tête (heading tag) dans le stepper.
- Ajout d'un titre sur les tags sélectionnés.
- Ajout de tags non ordonnés.
- Internationalisation (i18n) : plusieurs commits pour l'ajout et la correction de la gestion des traductions.

### Évolutions techniques
- Ajout du versionnement via GitHub Actions et publication sur PyPi. [#515](https://github.com/numerique-gouv/sites-conformes/issues/515)
- Amélioration de la recette d'upgrade pour gérer le projet de démonstration. [#527](https://github.com/numerique-gouv/sites-conformes/issues/527)
- Correction de la configuration Docker. [#519](https://github.com/numerique-gouv/sites-conformes/issues/519)
- Correction des erreurs de validation du fichier `publiccode.yml`. [#496](https://github.com/numerique-gouv/sites-conformes/issues/496)
- Amélioration des scripts de restauration des médias (gestion des erreurs, verbosité).

### Autres changements
- Commentaires ajoutés à certains scripts de migration.
- Revert d'un commit d'ajout de migration.
- Correction de bugs mineurs et améliorations diverses du code.
