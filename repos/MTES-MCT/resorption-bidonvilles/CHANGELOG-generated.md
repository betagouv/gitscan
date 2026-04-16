## Changelog : resorption-bidonvilles (30 derniers jours, au 9 avril 2026)

### Résumé
Cette version apporte des améliorations significatives à l'export des données, notamment en termes de filtrage et de gestion des informations financières. Des corrections ont été apportées pour améliorer la stabilité et la fiabilité de l'application, ainsi que des optimisations de code et de l'interface utilisateur. L'authentification et la gestion des permissions ont également été renforcées.

### Évolutions fonctionnelles
- Ajout d'un filtre pour l'export des actions, permettant de sélectionner uniquement les actions financées par la DIHAL. [#1451](https://github.com/MTES-MCT/resorption-bidonvilles/issues/1451)
- Amélioration de l'export des actions : prise en compte du delta pour les mises à jour du nombre d'habitants et affichage du taux de mise à jour des habitants. [#1439](https://github.com/MTES-MCT/resorption-bidonvilles/issues/1439) et [#1437](https://github.com/MTES-MCT/resorption-bidonvilles/issues/1437)
- Ajout d'une popup d'export des actions avec un taux calculé. [#1452](https://github.com/MTES-MCT/resorption-bidonvilles/issues/1452)
- Ajout de statistiques de sites financés par la DIHAL. [#1449](https://github.com/MTES-MCT/resorption-bidonvilles/issues/1449)
- Amélioration de la gestion des erreurs et affichage d'une notification informative en cas de données introuvables. [#1443](https://github.com/MTES-MCT/resorption-bidonvilles/issues/1443)
- Possibilité d'accorder l'accès à l'export des actions aux opérateurs et correspondants sur leur territoire. [#1442](https://github.com/MTES-MCT/resorption-bidonvilles/issues/1442)
- Correction de l'expiration du jeton d'activation (passée de 10 minutes à 168 heures). [#1457](https://github.com/MTES-MCT/resorption-bidonvilles/issues/1457)

### Évolutions techniques
- Refactoring du code pour améliorer la lisibilité et la maintenabilité.
- Utilisation de `Number.parseInt` et `Number.parseFloat` à la place de `parseInt` et `parseFloat`.
- Mise à jour des dépendances et correction des conflits.
- Amélioration de la gestion des erreurs et des validations.
- Utilisation de la forme mutualisée pour les seeders. [#1456](https://github.com/MTES-MCT/resorption-bidonvilles/issues/1456)
- Sécurisation et transmission des données pour le header des actions. [#1451](https://github.com/MTES-MCT/resorption-bidonvilles/issues/1451)
- DSFRisation de l'affichage de l'erreur d'export.
- Correction du calcul du taux d'actions financées par la DIHAL ayant une MAJ < 3 mois.
- Amélioration du score du code (SonarQube).
- Correction de l'affichage du département dans l'onglet 'tous'.
- Ajout de lodash pour faciliter certaines opérations.

### Autres changements
- Amélioration de la documentation.
- Correction de divers bugs et problèmes mineurs.
- Suppression de logs inutiles.
- Mise à jour des images et des fichiers de configuration.
- Correction de l'import des fichiers JSON pour les seeders.
- Correction de la gestion du click sur certains éléments.
- Correction de variables et de noms de fichiers pour plus de clarté.
- Amélioration de la hauteur de la popup.
- Renommage de fichiers images.
- Correction de la gestion des dates de mise à jour de la population.
- Ajout de badges de statistiques.
- Correction de l'affichage des badges de statistiques.
- Amélioration de l'affichage des erreurs.
- Ajout de tests unitaires.
- Correction de l'envoi de mails.
- Correction de la validation des emails.
- Ajout de commentaires et de documentation.
