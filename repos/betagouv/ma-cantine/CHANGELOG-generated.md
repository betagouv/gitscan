## Changelog : ma-cantine (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration des fonctionnalités de télédéclaration des bilans, notamment avec de nouveaux scripts et des corrections de bugs. Des améliorations ont également été apportées à l'interface utilisateur et à l'observabilité des données, ainsi que des ajustements techniques pour faciliter le développement et la maintenance.

### Évolutions fonctionnelles
- Ajout d'un script permettant de télédéclarer une liste de bilans hors campagne ([#6671](https://github.com/betagouv/ma-cantine/issues/6671)).
- Nouveau script pour télédéclarer tous les bilans en correction ([#6666](https://github.com/betagouv/ma-cantine/issues/6666)).
- Ajout d'un filtre au tableau de bord permettant d'afficher uniquement les bilans télédéclarés ([#6655](https://github.com/betagouv/ma-cantine/issues/6655)).
- Amélioration de l'affichage du pourcentage des valeurs durables et de qualité dans la télédéclaration ([#6668](https://github.com/betagouv/ma-cantine/issues/6668)).
- Ajout des dates de campagne dans l'interface de campagne de correction ([#6607](https://github.com/betagouv/ma-cantine/issues/6607)).
- Modification de l'affichage des couverts : remplacement du nombre de couverts jours par le nombre de couverts annuels pour les satellites ([#6624](https://github.com/betagouv/ma-cantine/issues/6624)).
- Ajout du nouveau statut "CORRECTION" pour les bilans ([#6616](https://github.com/betagouv/ma-cantine/issues/6616)).
- Modification de l'emplacement du bloc de correction dans l'interface de télédéclaration ([#6626](https://github.com/betagouv/ma-cantine/issues/6626)).
- Ajout d'un indicateur du nombre de filtres sélectionnés dans la liste déroulante de filtres ([#6654](https://github.com/betagouv/ma-cantine/issues/6654)).
- Amélioration de l'organisation des actions sur les cantines ([#6613](https://github.com/betagouv/ma-cantine/issues/6613)).

### Évolutions techniques
- Refactor de la logique de récupération des dates de fin de campagne pour la télédéclaration ([#6657](https://github.com/betagouv/ma-cantine/issues/6657)).
- Simplification du code des règles métiers encadrant la télédéclaration ([#6656](https://github.com/betagouv/ma-cantine/issues/6656)).
- Suppression du code lié aux anciens imports de bilans ([#6642](https://github.com/betagouv/ma-cantine/issues/6642)).
- Ajout de `1TD1Site` dans les exports bruts pour l'ETL ([#6632](https://github.com/betagouv/ma-cantine/issues/6632)).
- Pré-calcul de champs pour le script de génération `1TD1Site` ([#6627](https://github.com/betagouv/ma-cantine/issues/6627)).
- Branchement de `1TD1Site` pour 2025 ([#6614](https://github.com/betagouv/ma-cantine/issues/6614)).
- Amélioration du script de génération `1TD1Site` pour gérer l'année 2025 ([#6618](https://github.com/betagouv/ma-cantine/issues/6618)).
- Correction de l'API Diagnostics pour renvoyer uniquement les pourcentages d'approbation ([#6664](https://github.com/betagouv/ma-cantine/issues/6664)).
- Correction pour ne renvoyer que les pourcentages et badges des bilans des cantines publiques ([#6663](https://github.com/betagouv/ma-cantine/issues/6663)).

### Autres changements
- Correction du lien dans le bandeau d'information de la campagne de correction ([#6675](https://github.com/betagouv/ma-cantine/issues/6675)).
- Correction d'une faute d'orthographe dans les mentions légales ([#6640](https://github.com/betagouv/ma-cantine/issues/6640)).
- Suppression du tiret dans le texte "ma-cantine" ([#6633](https://github.com/betagouv/ma-cantine/issues/6633)).
- Correction de l'affichage de la police Marianne ([#6669](https://github.com/betagouv/ma-cantine/issues/6669)).
- Suppression du message "Non renseignée" pour la colonne 'commune' du tableau de bord pour les groupes ([#6653](https://github.com/betagouv/ma-cantine/issues/6653)).
- Ajout de filtres pour les diagnostics TD générés ([#6582](https://github.com/betagouv/ma-cantine/issues/6582)).
- Mise à jour de la police Marianne avec un fichier d'import dédié ([#6621](https://github.com/betagouv/ma-cantine/issues/6621)).
- Suppression du message d'alerte sur les données incorrectes pour l'année 2024 dans l'observatoire ([#6620](https://github.com/betagouv/ma-cantine/issues/6620)).
- Correction de bugs liés aux règles métiers de télédéclaration après la fin de la campagne de correction ([#6637](https://github.com/betagouv/ma-cantine/issues/6637), [#6641](https://github.com/betagouv/ma-cantine/issues/6641), [#6652](https://github.com/betagouv/ma-cantine/issues/6652)).
- Empêcher la modification d'un bilan en SUBMITTED après la fin de la campagne de correction ([#6650](https://github.com/betagouv/ma-cantine/issues/6650)).
- Empêcher la modification d'un bilan en DRAFT après la fin de la campagne ([#6636](https://github.com/betagouv/ma-cantine/issues/6636)).
- Ne pas afficher le bouton "Modifier mes données" si le bilan n'est pas télédéclaré ([#6629](https://github.com/betagouv/ma-cantine/issues/6629)).
