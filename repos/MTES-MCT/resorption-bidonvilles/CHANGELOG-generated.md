## Changelog : resorption-bidonvilles (30 derniers jours, au 20 avril 2026)

### Résumé
Cette version apporte des améliorations significatives au suivi des financements DIHAL, avec l'ajout de filtres et d'indicateurs de mise à jour de population. Des corrections ont été apportées pour améliorer la précision des données affichées et la sécurité de l'application. L'interface utilisateur a également été améliorée avec des mises à jour de design et des corrections de bugs.

### Évolutions fonctionnelles
- Ajout du filtre par année de financement DIHAL, permettant un affichage plus précis des actions financées. [#2659](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2659)
- Affichage des indicateurs de mise à jour de population dans l'email récapitulatif hebdomadaire. [#2662](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2662)
- Affichage de l'année de financement DIHAL sur les badges correspondants. [#2659](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2659)
- Ajout du champ adresse email du demandeur d'accès. [#2661](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2661)
- Correction du lien "demande d'info" qui redirigeait vers une mauvaise page (maintenant "demande d'accès"). [#2666](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2666)
- Correction du calcul du taux d'actions financées par la DIHAL avec une mise à jour de moins de 3 mois. [#2649](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2649)
- Correction du comportement de la page lors du clic sur un élément de la liste "Années avec financements renseignés" (évite le rechargement de la page). [#2657](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2657)

### Évolutions techniques
- Changement de l'URL d'accès à Matomo pour utiliser le lien proxifié. [#2660](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2660)
- Ajout du paramètre `trackerScriptUrl` pour une configuration plus flexible du suivi. [#2660](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2660)
- Amélioration de la sécurité et transmission des données pour le header des actions.
- Intégration du header des actions avec le taux calculé.
- Correction de l'expiration du jeton d'activation (passée de 10 minutes à 168 heures). [#2658](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2658)
- Refactoring et simplification du code pour améliorer la maintenabilité et la performance.
- Amélioration du score du code suite à l'analyse SonarQube.
- DSFRisation de l'affichage de l'erreur d'export.

### Autres changements
- Correction de plusieurs erreurs de linting. [#2659](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2659)
- Correction de l'affichage du département dans l'onglet 'tous'.
- Correction de quelques erreurs de typage et de logique dans le code.
- Documentation mise à jour.
