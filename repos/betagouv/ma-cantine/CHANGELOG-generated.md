## Changelog : ma-cantine (30 derniers jours, au 23 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la traçabilité des données (qui a créé quoi), l'enrichissement des informations disponibles (guides CNRC, champs d'achats) et l'optimisation des processus internes (gestion des logs, refactoring du code). Des améliorations spécifiques ont été apportées aux diagnostics et aux achats, notamment pour faciliter la gestion des données et améliorer l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout de nouveaux guides du CNRC dans la section "Ressources" ([#6835](https://github.com/betagouv/ma-cantine/issues/6835)).
- Amélioration de l'affichage des champs "EGalim" et "Origine" dans la gestion des achats ([#6826](https://github.com/betagouv/ma-cantine/issues/6826)).
- Possibilité de sélectionner une cantine lors de la duplication d'un achat ([#6823](https://github.com/betagouv/ma-cantine/issues/6823)).
- Ajout de champs caractéristiques et famille de produit dans la gestion des achats ([#6782](https://github.com/betagouv/ma-cantine/issues/6782)).
- Ajout de la modification d'un achat à partir du nouveau formulaire ([#6783](https://github.com/betagouv/ma-cantine/issues/6783)).
- Ajout d'une autocomplétion pour les champs "Description" et "Fournisseurs" dans la gestion des achats ([#6797](https://github.com/betagouv/ma-cantine/issues/6797)).
- Ajout d'un nouveau champ `groupe_snapshot` dans les diagnostics, visible dans l'administration ([#6799](https://github.com/betagouv/ma-cantine/issues/6799)).

### Évolutions techniques
- Ajout d'informations sur l'application OAuth2 ayant créé une cantine, un bilan, un achat ou une évaluation de gaspillage ([#6843](https://github.com/betagouv/ma-cantine/issues/6843)).
- Implémentation d'une classe de base `MaCantineBaseCommand` pour la gestion des logs des commandes ([#6838](https://github.com/betagouv/ma-cantine/issues/6838)).
- Logging des résultats des commandes dans une table dédiée `CommandLog` ([#6837](https://github.com/betagouv/ma-cantine/issues/6837)).
- Refactoring de la gestion des métadonnées dans l'API pour une meilleure organisation ([#6829](https://github.com/betagouv/ma-cantine/issues/6829)).
- Amélioration de la gestion des erreurs et des retours d'API (renvoi de 404 lorsque la cantine est inconnue ou l'objet n'y appartient pas) ([#6811](https://github.com/betagouv/ma-cantine/issues/6811), [#6812](https://github.com/betagouv/ma-cantine/issues/6812), [#6814](https://github.com/betagouv/ma-cantine/issues/6814), [#6815](https://github.com/betagouv/ma-cantine/issues/6815), [#6816](https://github.com/betagouv/ma-cantine/issues/6816)).
- Refactoring et nettoyage du code lié aux diagnostics et aux évaluations de gaspillage.
- Suppression du code lié à l'API Adresse, qui n'est plus utilisée ([#6787](https://github.com/betagouv/ma-cantine/issues/6787)).
- Amélioration des scripts de remplissage des champs calculés des diagnostics ([#6754](https://github.com/betagouv/ma-cantine/issues/6754)).
- Ajout de nouveaux querysets pour faciliter le filtrage des diagnostics ([#6735](https://github.com/betagouv/ma-cantine/issues/6735), [#6736](https://github.com/betagouv/ma-cantine/issues/6736)).

### Autres changements
- Mise à jour de la documentation pour expliquer les commandes liées à la télédéclaration ([#6738](https://github.com/betagouv/ma-cantine/issues/6738)).
- Correction de tests suite à des modifications du code.
- Mise à jour des valeurs autorisées pour les champs "Origines" et "Définition de locale" dans la gestion des achats ([#6803](https://github.com/betagouv/ma-cantine/issues/6803)).
- Correction de bugs et améliorations diverses suite à des phases de recette interne.
