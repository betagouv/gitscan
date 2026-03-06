## Changelog : people (30 derniers jours)

### Résumé
Les dernières mises à jour de l'application "people" se concentrent sur l'amélioration de la gestion des invitations, des statistiques, et de l'expérience utilisateur, notamment avec l'ajout d'icônes et la suppression d'invitations. Des corrections de bugs ont également été apportées pour améliorer la stabilité et la fiabilité de l'application. Enfin, des mises à jour techniques ont été effectuées pour corriger des vulnérabilités de sécurité et améliorer la configuration de l'environnement de développement.

### Évolutions fonctionnelles
- Ajout d'une icône au bouton de configuration d'un domaine. [#1054](https://github.com/suitenumerique/people/issues/1054)
- Possibilité pour un administrateur de supprimer des invitations. [#1052](https://github.com/suitenumerique/people/issues/1052)
- Comptabilisation des alias dans l'endpoint de statistiques.
- Ajout des alias à la démo.
- Prise en compte de la casse lors de la recherche d'emails existants. [#1056](https://github.com/suitenumerique/people/issues/1056)

### Évolutions techniques
- Déplacement des exceptions liées aux invitations vers le cœur de l'application.
- Simplification des tests liés aux invitations de domaines par email.
- Mise à jour de la version de Python à 3.14.2 pour la configuration Docker.
- Mise à jour de la bibliothèque `next` vers la version 15.5.10 pour corriger une vulnérabilité de sécurité.
- Mise à jour des dépendances Python.

### Autres changements
- Mise à jour des chaînes de traduction.
- Publication des versions 1.23.1 et 1.23.0.
- Correction de linter warnings.
- Correction d'un problème d'upload dans Crowdin.
- Correction d'une tentative d'envoi d'invitations à des utilisateurs existants.
