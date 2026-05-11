## Changelog : doctorat-gouv (30 derniers jours, au 21 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'intégration d'Amethis, l'amélioration de l'expérience utilisateur, notamment au niveau du header et des tooltips, et l'affichage des informations, en particulier sur la page de détails des candidatures. Plusieurs corrections de bugs ont également été apportées pour améliorer la stabilité et la réactivité de l'application.

### Évolutions fonctionnelles
- Intégration des boutons Amethis en bas de la page de détails des candidatures. [#31](https://github.com/betagouv/doctorat-gouv/pull/31)
- Ajout de deux boutons pour Amethis sur la page de détails des candidatures. [#32](https://github.com/betagouv/doctorat-gouv/pull/32)
- Activation du scheduler Amethis. [#32](https://github.com/betagouv/doctorat-gouv/pull/32)
- Affichage de plus d'informations dans la rubrique financement. [#33](https://github.com/betagouv/doctorat-gouv/pull/33)
- Amélioration de l'affichage des tooltips sur les versions desktop et mobile.
- Intégration de l'affichage du menu langue dans le menu camembert en version mobile.
- Augmentation de la taille de la colonne matricule suite à une demande d'Amethis.
- Ajout de `innerHTML` pour interpréter les balises HTML d'ADUM et Amethis, permettant une meilleure mise en forme des champs longs. [#32](https://github.com/betagouv/doctorat-gouv/pull/32)

### Évolutions techniques
- Refactoring du code concernant le header.
- Préparation des versions 0.2.8 et 0.2.9.
- Ajout de mapping pour la source et l'URL de candidature.

### Autres changements
- Correction de problèmes d'affichage du header en version mobile (débordement horizontal, `fr-header__service::before`).
- Diminution de la taille de l'icône info-bulle sur les versions desktop et mobile.
- Correction d'un problème de fermeture des tooltips.
- Amélioration de l'affichage du bouton Amethis en version mobile.
- Réduction de l'espace entre les boutons.
- Correction d'un problème d'affichage du tooltip en version mobile.
- Augmentation de la taille de l'icône de l'info-bulle dans le header.
- Amélioration de l'affichage du tooltip en version desktop.
- Modification des messages des tooltips.
