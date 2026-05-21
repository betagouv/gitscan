## Changelog : ma-cantine (30 derniers jours, au 20 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration des données géo, des formulaires d'achats, des exports de données (ETL) et de la gestion des télédéclarations. Des corrections de bugs et des refactorings techniques ont également été réalisés pour améliorer la stabilité et la maintenabilité du code.

### Évolutions fonctionnelles
- Ajout des livrables GT sanitaire et médico-social aux ressources ([#6733](https://github.com/betagouv/ma-cantine/issues/6733)).
- Améliorations diverses sur le formulaire d'achats (libellés, champs obligatoires, explications) ([#6734](https://github.com/betagouv/ma-cantine/issues/6734)).
- Ajout d'un filtre "bilan télédéclaré" au tableau de bord ([#6655](https://github.com/betagouv/ma-cantine/issues/6655)).
- Correction de l'affichage du pourcentage des valeurs durables et de qualité dans les télédéclarations ([#6668](https://github.com/betagouv/ma-cantine/issues/6668)).
- Correction de l'URL vers les CGU du frontend ([#6701](https://github.com/betagouv/ma-cantine/issues/6701)).

### Évolutions techniques
- Refactoring de l'API Validata pour vérifier la validité des fichiers avant l'export Open Data ([#6713](https://github.com/betagouv/ma-cantine/issues/6713)).
- Refactoring de l'API Adresse pour rendre l'appel à la fonction indépendant de l'objet 'response' ([#6712](https://github.com/betagouv/ma-cantine/issues/6712)).
- Amélioration de la commande `diagnostic_fill_invalid_reason_list` pour faciliter l'application et le récapitulatif des statistiques ([#6700](https://github.com/betagouv/ma-cantine/issues/6700)).
- Ajout de querysets dédiés pour les achats (pour l'utilisateur et pour l'année) ([#6719](https://github.com/betagouv/ma-cantine/issues/6719)).
- Suppression du script `field_gen.py` car il n'est plus utilisé ([#6726](https://github.com/betagouv/ma-cantine/issues/6726)).
- Suppression du code lié aux anciens imports de bilans ([#6642](https://github.com/betagouv/ma-cantine/issues/6642)).
- Refactoring des tests de l'endpoint de création de diagnostics à partir des achats ([#6728](https://github.com/betagouv/ma-cantine/issues/6728)).
- Amélioration de la gestion des données géo PAT, avec un script dédié à la mise à jour des données ([#6725](https://github.com/betagouv/ma-cantine/issues/6725)).
- Correction d'un problème lié aux caractères spéciaux dans les données PAT ([#6715](https://github.com/betagouv/ma-cantine/issues/6715)).

### Autres changements
- Mise à jour de la police Marianne pour corriger un problème d'affichage ([#6669](https://github.com/betagouv/ma-cantine/issues/6669)).
- Correction d'un lien dans le bandeau d'information concernant la campagne de correction ([#6675](https://github.com/betagouv/ma-cantine/issues/6675)).
- Sécurisation du paramètre 'next' pour éviter des failles de sécurité ([#6709](https://github.com/betagouv/ma-cantine/issues/6709)).
- Correction de l'affichage de "Non renseignée" dans la colonne 'commune' du tableau de bord pour les groupes ([#6653](https://github.com/betagouv/ma-cantine/issues/6653)).
- Ajout d'un indicateur du nombre de filtres sélectionnés dans la liste déroulante ([#6654](https://github.com/betagouv/ma-cantine/issues/6654)).
