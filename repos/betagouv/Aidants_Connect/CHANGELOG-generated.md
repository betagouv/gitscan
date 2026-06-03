## Changelog : Aidants_Connect (30 derniers jours, au 01 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'accessibilité et l'expérience utilisateur, notamment sur la page d'accueil et les parcours aidants. Des corrections ont également été apportées concernant les exports pour les Organismes de Formation (OF) et la gestion des URLs de callback. Une refonte du parcours d'ajout d'aidant avec le changement de structure a été réalisée.

### Évolutions fonctionnelles
- **Parcours d'ajout d'aidant :** Refonte complète du parcours d'ajout d'aidant avec intégration du changement de structure. [#1736](https://github.com/betagouv/Aidants_Connect/issues/1736)
- **Exports OF :** Amélioration des exports des inscrits pour les Organismes de Formation, notamment pour les formations "Attendant". [#1778](https://github.com/betagouv/Aidants_Connect/issues/1778)
- **Correction URL de callback :** Correction d'une erreur concernant l'URL de callback. [#1776](https://github.com/betagouv/Aidants_Connect/issues/1776)
- **Menu espace aidant :** Simplification du menu de l'espace aidant et restructuration des URLs. [#1751](https://github.com/betagouv/Aidants_Connect/issues/1751)
- **Parcours de changement de structure :** Amélioration des formulations et des messages du parcours de changement de structure. [#1774](https://github.com/betagouv/Aidants_Connect/issues/1774)

### Évolutions techniques
- **Accessibilité :** Amélioration significative de l'accessibilité générale de l'application, incluant la structure sémantique, l'utilisation d'ARIA roles, la gestion du focus et l'amélioration des titres et des listes. [#1773](https://github.com/betagouv/Aidants_Connect/issues/1773)
- **Suppression iframe Brevo :** Suppression de l'iframe Brevo de la page d'accueil pour améliorer l'accessibilité et la réactivité.
- **Mise à jour des dépendances :** Mise à jour de toutes les dépendances avant la mise à jour vers Django 5.2. [#1779](https://github.com/betagouv/Aidants_Connect/issues/1779)
- **Refactoring templates :** Refactoring de plusieurs templates (accueil, statistiques, FAQ, habilitation) pour améliorer la structure sémantique et l'accessibilité.
- **Correction alignement DSFR :** Correction d'un problème d'alignement dans le Design System FR (DSFR) en ajustant les propriétés flex.

### Autres changements
- Suppression de meta tags et de code legacy inutiles.
- Ajout de tests pour la validation des emails lors des demandes de changement de structure.
- Amélioration de la validation des emails dans le formulaire de demande de changement de structure.
