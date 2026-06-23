## Changelog : trackdechets (30 derniers jours, au 22 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la sécurité avec l'implémentation de la récupération de compte via un code de récupération et la gestion des réinitialisations MFA. Des corrections de bugs ont été apportées pour améliorer la stabilité et l'expérience utilisateur, notamment concernant la signature des bordereaux et la gestion des transporteurs. Des améliorations ont également été apportées à l'interface utilisateur et à la gestion des conteneurs.

### Évolutions fonctionnelles
- **Récupération de compte :** Ajout de la possibilité de récupérer son compte via un code de récupération. [#4799](https://github.com/MTES-MCT/trackdechets/issues/4799)
- **Gestion MFA :** Implémentation d'un panneau d'administration pour gérer les réinitialisations MFA. [#4804](https://github.com/MTES-MCT/trackdechets/issues/4804) et [#4793](https://github.com/MTES-MCT/trackdechets/issues/4793)
- **Notifications de sécurité :** Ajout de notifications de sécurité liées à la récupération manuelle de compte. [#4805](https://github.com/MTES-MCT/trackdechets/issues/4805) et [#4793](https://github.com/MTES-MCT/trackdechets/issues/4793)
- **Bordereaux BSFF :** Correction d'un bug empêchant l'enregistrement des bordereaux de regroupement BSFF. [#4808](https://github.com/MTES-MCT/trackdechets/issues/4808) et [#4788](https://github.com/MTES-MCT/trackdechets/issues/4788)
- **Interface utilisateur :** Amélioration de l'interface utilisateur pour la saisie des numéros de contenant (caractères spéciaux autorisés). [#4786](https://github.com/MTES-MCT/trackdechets/issues/4786)
- **Gestion des détenteurs :** Ajout d'un onglet détenteur et des champs manquants associés.
- **Labels PAOH & VHU :** Correction des labels Réelle & Estimée pour PAOH & VHU. [#4783](https://github.com/MTES-MCT/trackdechets/issues/4783)

### Évolutions techniques
- **Refactoring :** Refactoring du composant `SecondFactor` pour une meilleure clarté.
- **Tests :** Corrections et améliorations des tests d'intégration.
- **Pipeline :** Corrections de problèmes liés aux pipelines CI/CD.
- **Complexité cognitive :** Réduction de la complexité cognitive dans la classe `SecondFactor`. [#4792](https://github.com/MTES-MCT/trackdechets/issues/4792)

### Autres changements
- **Corrections de bugs :** Plusieurs corrections de bugs concernant le blocage de la modification du transporteur sur VHU/BSDA, la signature des transporteurs BSDD et le retour de la recette aperçu.
- **Documentation :** Mise à jour de la documentation et ajout d'un bandeau MEP 2026-06. [#4789](https://github.com/MTES-MCT/trackdechets/issues/4789)
- **Linting :** Corrections des erreurs de linting.
