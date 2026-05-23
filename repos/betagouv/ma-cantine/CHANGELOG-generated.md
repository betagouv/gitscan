## Changelog : ma-cantine (30 derniers jours, au 20 mai 2026)

### Résumé
Ce mois-ci, les évolutions de ma-cantine se concentrent sur l'amélioration des données géo, la correction de bugs liés aux achats et aux télédéclarations, ainsi que des optimisations techniques pour une meilleure performance et maintenance du code. De nouvelles fonctionnalités ont été ajoutées concernant les ressources et les livrables GT sanitaire et médico-social.

### Évolutions fonctionnelles
- Ajout des livrables GT sanitaire et médico-social dans la section Ressources. ([#6733](https://github.com/betagouv/ma-cantine/issues/6733))
- Améliorations apportées au formulaire d'achats (libellés, champs obligatoires, explications). ([#6734](https://github.com/betagouv/ma-cantine/issues/6734))
- Correction de l'affichage du pourcentage des valeurs durables et de qualité dans les télédéclarations. ([#6668](https://github.com/betagouv/ma-cantine/issues/6668))
- Correction du lien vers les CGU dans le frontend. ([#6701](https://github.com/betagouv/ma-cantine/issues/6701))
- Correction du non affichage de la police Marianne. ([#6669](https://github.com/betagouv/ma-cantine/issues/6669))

### Évolutions techniques
- Mise à jour du script dédié à la mise à jour des données PAT (données géo). ([#6725](https://github.com/betagouv/ma-cantine/issues/6725))
- Optimisation de l'API des achats : nettoyage des champs renvoyés par l'endpoint `canteenPurchasesPercentageSummary`. ([#6730](https://github.com/betagouv/ma-cantine/issues/6730))
- Refactoring de l'API et des tests liés à la création de diagnostics à partir des achats. ([#6728](https://github.com/betagouv/ma-cantine/issues/6728))
- Suppression du script `field_gen.py` car il n'est plus utilisé. ([#6726](https://github.com/betagouv/ma-cantine/issues/6726))
- Amélioration de la commande `diagnostic_fill_invalid_reason_list` (application et récapitulatif des statistiques). ([#6700](https://github.com/betagouv/ma-cantine/issues/6700))
- Regroupement des statistiques d'agrégation des achats dans une queryset dédiée. ([#6706](https://github.com/betagouv/ma-cantine/issues/6706))
- Lister les groupes de caractéristiques pour faciliter leur réutilisation. ([#6702](https://github.com/betagouv/ma-cantine/issues/6702))
- Réorganisation des champs dans les modèles (Meta et timestamps en bas). ([#6703](https://github.com/betagouv/ma-cantine/issues/6703))
- Amélioration de la sécurité : sanitisation du paramètre `next`. ([#6709](https://github.com/betagouv/ma-cantine/issues/6709))
- Refactoring de l'API de recherche d'entreprises pour ne pas utiliser de camelCase dans la transformation des résultats. ([#6710](https://github.com/betagouv/ma-cantine/issues/6710))

### Autres changements
- Mise à jour des fichiers de référence PAT (données géo). ([#6693](https://github.com/betagouv/ma-cantine/issues/6693))
- Correction d'un bug dans l'export Open Data. ([#6722](https://github.com/betagouv/ma-cantine/issues/6722))
- Suppression des tâches asynchrones liées à la récupération des données géo. ([#6691](https://github.com/betagouv/ma-cantine/issues/6691))
- Diverses corrections et améliorations liées aux télédéclarations. ([#6671](https://github.com/betagouv/ma-cantine/issues/6671), [#6657](https://github.com/betagouv/ma-cantine/issues/6657), [#6656](https://github.com/betagouv/ma-cantine/issues/6656), [#6673](https://github.com/betagouv/ma-cantine/issues/6673))
- Mise à jour des dépendances Wagtail et Django. ([#6696](https://github.com/betagouv/ma-cantine/issues/6696), [#6697](https://github.com/betagouv/ma-cantine/issues/6697))
