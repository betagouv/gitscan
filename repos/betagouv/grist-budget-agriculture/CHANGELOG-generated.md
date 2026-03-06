## Changelog : grist-budget-agriculture (30 derniers jours)

### Résumé
Les dernières mises à jour se concentrent sur l'amélioration du traitement des informations budgétaires, notamment l'extraction et l'analyse des données provenant de fichiers Excel (INFBUD). Des efforts ont également été faits pour simplifier et optimiser le code, ainsi que pour améliorer la documentation et la gestion des tâches planifiées.

### Évolutions fonctionnelles
- Amélioration de l'extraction des informations importantes des fichiers Excel, permettant une meilleure analyse des données budgétaires. [#254e9f2](https://github.com/betagouv/grist-budget-agriculture/commit/254e9f2)
- Préparation de l'envoi d'emails récapitulatifs concernant les informations de l'INFBUD, avec une limitation aux Budgets de Consommation (BC) en écart. [#254e9f2](https://github.com/betagouv/grist-budget-agriculture/commit/254e9f2), [#efc6969](https://github.com/betagouv/grist-budget-agriculture/commit/efc6969)
- Simplification du traitement des INFBUD MTE (Ministère de la Transition Écologique). [#f524729](https://github.com/betagouv/grist-budget-agriculture/commit/f524729)

### Évolutions techniques
- Ajout de la dépendance `imap_tools` pour permettre le déplacement des emails. [#d8294e3](https://github.com/betagouv/grist-budget-agriculture/commit/d8294e3)
- Suppression du module PPA (Peste Porcine Africaine) et renforcement du linting automatique pour améliorer la qualité du code. [#e1ff3bd](https://github.com/betagouv/grist-budget-agriculture/commit/e1ff3bd)
- Correction des cron jobs pour assurer leur bon fonctionnement. [#c48281d](https://github.com/betagouv/grist-budget-agriculture/commit/c48281d)
- Correction du chemin vers l'application frontend. [#41bca99](https://github.com/betagouv/grist-budget-agriculture/commit/41bca99)
- Création d'un paquet Python pour faciliter la distribution et l'installation. [#71899a6](https://github.com/betagouv/grist-budget-agriculture/commit/71899a6)
- Simplification de la recherche dans les fichiers Excel reçus. [#7e76add](https://github.com/betagouv/grist-budget-agriculture/commit/7e76add)
- Extraction du traitement du fichier Excel dans un module dédié. [#2d75976](https://github.com/betagouv/grist-budget-agriculture/commit/2d75976)

### Autres changements
- Mise à jour de la documentation. [#5c62155](https://github.com/betagouv/grist-budget-agriculture/commit/5c62155)
- Ajout d'un état des lieux des SF (Services Financiers) manquants. [#2ca8224](https://github.com/betagouv/grist-budget-agriculture/commit/2ca8224)
- Correction du décompte des correspondances. [#93ecb38](https://github.com/betagouv/grist-budget-agriculture/commit/93ecb38)
- Suppression du script exploratoire de la PPA. [#cf041f8](https://github.com/betagouv/grist-budget-agriculture/commit/cf041f8)
