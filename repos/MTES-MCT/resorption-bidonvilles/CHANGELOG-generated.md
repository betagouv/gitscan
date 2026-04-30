## Changelog : resorption-bidonvilles (30 derniers jours, au 20 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des financements DIHAL, l'ajout d'indicateurs de mise à jour de la population, et la correction de plusieurs bugs pour une meilleure expérience utilisateur. Des améliorations techniques ont également été apportées pour la sécurité, la performance et la qualité du code.

### Évolutions fonctionnelles
- Ajout de l'adresse email du demandeur d'accès lors d'une demande. [#1451](https://github.com/MTES-MCT/resorption-bidonvilles/pull/1451)
- Possibilité de filtrer les actions par année de financement DIHAL. [#1455](https://github.com/MTES-MCT/resorption-bidonvilles/pull/1455)
- Affichage de l'année de financement DIHAL sur les badges correspondants. [#1455](https://github.com/MTES-MCT/resorption-bidonvilles/pull/1455)
- Intégration d'indicateurs de mise à jour de la population dans l'email récapitulatif hebdomadaire. [#1460](https://github.com/MTES-MCT/resorption-bidonvilles/pull/1460)
- Affichage des indicateurs de mise à jour de la population sur 3 mois. [#1460](https://github.com/MTES-MCT/resorption-bidonvilles/pull/1460)
- Ajout d'une popup pour l'export des actions. [#1452](https://github.com/MTES-MCT/resorption-bidonvilles/pull/1452)
- Correction de la formulation des taux de mises à jour. [#1462](https://github.com/MTES-MCT/resorption-bidonvilles/pull/1462)
- Correction d'un bug empêchant le rechargement de la page lors du clic sur un élément de la liste "Années avec financements renseignés". [#1457](https://github.com/MTES-MCT/resorption-bidonvilles/pull/1457)

### Évolutions techniques
- Utilisation de la version mutualisée des JSON pour les seeders. [#1456](https://github.com/MTES-MCT/resorption-bidonvilles/pull/1456)
- Refactoring pour améliorer la qualité du code et le score SonarQube. [#1459](https://github.com/MTES-MCT/resorption-bidonvilles/pull/1459)
- Sécurisation et transmission des données pour le header des actions.
- Changement de l'URL d'accès à Matomo pour utiliser le lien proxifié. [#1451](https://github.com/MTES-MCT/resorption-bidonvilles/pull/1451)
- Correction de l'expiration du jeton d'activation (passée de 10 minutes à 168 heures). [#1457](https://github.com/MTES-MCT/resorption-bidonvilles/pull/1457)
- Simplification de l'appel à la fakeAction et amélioration du test unitaire associé.

### Autres changements
- Correction de plusieurs erreurs de linting.
- Mise à jour des fichiers générés et ajout d'un exemple de preview.
- Amélioration de l'affichage de l'erreur d'export avec la DSFR.
- Correction du lien de demande d'info en demande d'accès.
- Correction du nom de la fonction et de certains blocs de code.
- Amélioration de la hauteur de la popup.
- Renommage du fichier image.
- Publication des versions v2.49.1, v2.49.2, v2.49.3, v2.49.4, v2.50.0 et v2.51.0.
