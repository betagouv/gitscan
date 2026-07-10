## Changelog : apistration (30 derniers jours, au 09 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la sécurité, à l'accessibilité et à la gestion des éditeurs. L'ajout de l'endpoint DGFIP TVA et l'amélioration de la gestion des sessions renforcent les fonctionnalités de l'API. Des corrections de bugs et des optimisations de performance ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'un endpoint pour la TVA DGFIP, incluant des informations sur la date de dernière mise à jour et la possibilité de remplacer l'utilisation de l'API européenne de la Commission. [#125](https://github.com/datagouv/apistration/issues/125)
- Amélioration de la gestion des sessions avec une expiration après 12h d'inactivité et une protection renforcée contre les attaques CSRF. [#217](https://github.com/datagouv/apistration/issues/217)
- Refonte de l'interface d'administration des éditeurs avec de nouvelles fonctionnalités de recherche, de filtrage et de gestion des membres. [#139](https://github.com/datagouv/apistration/issues/139)
- Ajout d'un filtre par statut de requête sur le tableau de bord des fournisseurs. [#216](https://github.com/datagouv/apistration/issues/216)
- Remplacement du formulaire d'éditeur Datapass par un questionnaire Typeform. [#250](https://github.com/datagouv/apistration/issues/250)
- Ajout de la possibilité de créer automatiquement des délégations pour les éditeurs lors de la validation DataPass. [#246](https://github.com/datagouv/apistration/issues/246)
- Intégration de la fonctionnalité "explorer-api-fournisseur". [#219](https://github.com/datagouv/apistration/issues/219)
- Ajout de l'affichage de l'ID interne de l'utilisateur sur la page de compte. [#217](https://github.com/datagouv/apistration/issues/217)

### Évolutions techniques
- Migration des spécifications, des fixtures et des cassettes MI association vers JSON. [#254](https://github.com/datagouv/apistration/issues/254)
- Demande explicite de JSON depuis l'API DJEPVA/MI api-association. [#254](https://github.com/datagouv/apistration/issues/254)
- Amélioration de la robustesse des tests pour l'API DGFIP TVA. [#237](https://github.com/datagouv/apistration/issues/237)
- Correction d'une fuite de mémoire dans les tests Timecop pour OpenBureauDate. [#181](https://github.com/datagouv/apistration/issues/181)
- Mise à jour des dépendances (Ruby, Rails, actions Github).
- Amélioration de la gestion des erreurs et des exceptions.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.

### Autres changements
- Amélioration de l'accessibilité du site web (RGAA). [#239](https://github.com/datagouv/apistration/issues/239)
- Correction de typos et amélioration de la documentation.
- Ajout de tests unitaires et d'intégration.
- Mise à jour du changelog.
- Suppression des données agricoles de l'API. [#247](https://github.com/datagouv/apistration/issues/247)
- Ajout de la gestion des incidents Hyperping. [#235](https://github.com/datagouv/apistration/issues/235)
- Correction de problèmes de sécurité liés aux liens externes et à la gestion des jetons. [#240](https://github.com/datagouv/apistration/issues/240)
