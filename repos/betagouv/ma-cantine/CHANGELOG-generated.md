## Changelog : ma-cantine (30 derniers jours, au 2026-06-25)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives sur la gestion des achats, notamment une refonte de l'interface et l'ajout de nouveaux champs d'information. Des efforts ont également été déployés pour améliorer la qualité des données, en particulier concernant les diagnostics et les évaluations du gaspillage, avec l'ajout de champs de traçabilité et des corrections de données. Enfin, des optimisations techniques ont été apportées pour améliorer la performance et la maintenabilité du code.

### Évolutions fonctionnelles
- **Achats :** Le formulaire d'achat a été amélioré avec une présentation sur trois colonnes et la suppression du fond bleu. [#6847](https://github.com/betagouv/ma-cantine/issues/6847)
- **Achats :** Ajout de la possibilité de sélectionner une cantine lors de la duplication d'un achat. [#6823](https://github.com/betagouv/ma-cantine/issues/6823)
- **Achats :** Ajout de l'autocomplétion pour les champs "Description" et "Fournisseurs". [#6797](https://github.com/betagouv/ma-cantine/issues/6797)
- **Achats :** Ajout des champs "Caractéristiques" et "Famille de produit". [#6782](https://github.com/betagouv/ma-cantine/issues/6782)
- **Achats :** Début de la migration de la page de création d'achat vers la nouvelle interface (Vue3). [#6759](https://github.com/betagouv/ma-cantine/issues/6759)
- **Achats :** Mise à jour des valeurs autorisées pour le champ "Origines" et réorganisation des valeurs pour "Définition de locale". [#6803](https://github.com/betagouv/ma-cantine/issues/6803)
- **Achats :** Ajout de la modification d'un achat à partir du nouveau formulaire. [#6783](https://github.com/betagouv/ma-cantine/issues/6783)
- **Achats :** Remplacement de l'ancienne URL par la nouvelle URL officielle. [#6789](https://github.com/betagouv/ma-cantine/issues/6789)
- **Ressources :** Ajout des nouveaux guides du CNRC. [#6835](https://github.com/betagouv/ma-cantine/issues/6835)
- **Diagnostics :** Amélioration du script pour remplir les champs `invalid_reason_list` & `warning_reason_list` pour les diagnostics 1TD1Site. [#6820](https://github.com/betagouv/ma-cantine/issues/6820)
- **Diagnostics :** Marquage comme aberrant des diagnostics avec un coût de repas inférieur à 0.1. [#6795](https://github.com/betagouv/ma-cantine/issues/6795)
- **API :** Stockage de l'information sur l'application OAuth2 ayant créé la cantine, le bilan, l'achat ou l'évaluation du gaspillage. [#6843](https://github.com/betagouv/ma-cantine/issues/6843)

### Évolutions techniques
- **Commandes de gestion :** Ajout d'une nouvelle classe de base `MaCantineBaseCommand` pour gérer le loggage des résultats des commandes. [#6838](https://github.com/betagouv/ma-cantine/issues/6838)
- **Commandes de gestion :** Loggage des résultats des commandes dans une table dédiée `CommandLog`. [#6837](https://github.com/betagouv/ma-cantine/issues/6837)
- **API :** Amélioration de la manière de créer les champs metadata et suppression de leur renvoi dans les réponses. [#6829](https://github.com/betagouv/ma-cantine/issues/6829)
- **API :** Utilisation de `IsCanteenManagerUrlParam` au lieu de `IsLinkedCanteenManager` dans plusieurs vues pour une meilleure cohérence. [#6815](https://github.com/betagouv/ma-cantine/issues/6815), [#6812](https://github.com/betagouv/ma-cantine/issues/6812), [#6814](https://github.com/betagouv/ma-cantine/issues/6814)
- **API :** Retour d'une erreur 404 si l'objet n'appartient pas à la cantine. [#6816](https://github.com/betagouv/ma-cantine/issues/6816)
- **Diagnostics :** Amélioration du script pour remplir les champs calculés (dont le nouveau `cout_repas`). [#6754](https://github.com/betagouv/ma-cantine/issues/6754)
- **Diagnostics :** Ajout d'un nouveau champ `cout_repas` pour stocker le coût du repas. [#6753](https://github.com/betagouv/ma-cantine/issues/6753)
- **Données Géo :** Suppression du code lié à l'API Adresse, car elle n'est plus utilisée. [#6787](https://github.com/betagouv/ma-cantine/issues/6787)
- **Achats :** Séparation de FRANCE de CIRCUIT_COURT & LOCAL dans les calculs d'aggrégation. [#6731](https://github.com/betagouv/ma-cantine/issues/6731)
- **Achats :** Renommage des champs du modèle en français. [#6765](https://github.com/betagouv/ma-cantine/issues/6765)
- **Tests :** Homogénéisation des tests API suite aux changements récents. [#6757](https://github.com/betagouv/ma-cantine/issues/6757)

### Autres changements
- Correction de plusieurs tests suite aux modifications apportées.
- Divers correctifs suite au recettage avant mise en ligne des achats. [#6800](https://github.com/betagouv/ma-cantine/issues/6800)
- Ajout de champs `creation_user` et `creation_source` pour la traçabilité de la création des cantines, diagnostics et évaluations du gaspillage. [#6750](https://github.com/betagouv/ma-cantine/issues/6750), [#6761](https://github.com/betagouv/ma-cantine/issues/6761), [#6763](https://github.com/betagouv/ma-cantine/issues/6763)
- Ajout d'un nouveau champ `groupe_snapshot` pour les diagnostics 1TD1Site. [#6799](https://github.com/betagouv/ma-cantine/issues/6799)
