## Changelog : ma-cantine (30 derniers jours, au 8 juin 2026)

### Résumé
Ce mois-ci, les évolutions de ma-cantine se concentrent principalement sur le module Achats, avec une refonte de l'interface et l'ajout de nouvelles fonctionnalités pour faciliter la saisie et la gestion des informations. Des améliorations techniques ont également été apportées pour optimiser le code et corriger des erreurs.

### Évolutions fonctionnelles
- **Achats :** Ajout de la possibilité de modifier un achat directement depuis le nouveau formulaire. ([#6783](https://github.com/betagouv/ma-cantine/issues/6783))
- **Achats :** Début de la migration de la page de création d'achat vers Vue.js, modernisant l'interface utilisateur. ([#6759](https://github.com/betagouv/ma-cantine/issues/6759))
- **Achats :** Mise à jour de l'URL utilisée pour récupérer les données, assurant la compatibilité avec la nouvelle source officielle. ([#6789](https://github.com/betagouv/ma-cantine/issues/6789))
- **Achats :** Ajout de l'autocomplétion dans les champs "Description" et "Fournisseurs" pour une saisie plus rapide et précise. ([#6797](https://github.com/betagouv/ma-cantine/issues/6797))
- **Achats :** Ajout des champs "Caractéristiques" et "Famille de produit" pour une description plus détaillée des achats. ([#6782](https://github.com/betagouv/ma-cantine/issues/6782))
- **Ressources :** Ajout des livrables GT sanitaire et médico-social. ([#6733](https://github.com/betagouv/ma-cantine/issues/6733))

### Évolutions techniques
- **API :** Amélioration de la gestion des erreurs 404 pour les objets non liés à une cantine. ([#6816](https://github.com/betagouv/ma-cantine/issues/6816), [#6815](https://github.com/betagouv/ma-cantine/issues/6815), [#6814](https://github.com/betagouv/ma-cantine/issues/6814), [#6812](https://github.com/betagouv/ma-cantine/issues/6812))
- **Achats :** Refactorisation du code pour une meilleure lisibilité et maintenabilité, notamment en séparant les règles métiers et en renommant les champs du modèle. ([#6805](https://github.com/betagouv/ma-cantine/issues/6805), [#6804](https://github.com/betagouv/ma-cantine/issues/6804), [#6765](https://github.com/betagouv/ma-cantine/issues/6765))
- **Achats :** Amélioration des calculs d'agrégation pour prendre en compte les achats en EUROPE. ([#6788](https://github.com/betagouv/ma-cantine/issues/6788))
- **Données Géo :** Suppression du code inutile lié à l'ancienne API Adresse. ([#6787](https://github.com/betagouv/ma-cantine/issues/6787))
- **Diagnostics :** Simplification du code et suppression de champs inutiles. ([#6794](https://github.com/betagouv/ma-cantine/issues/6794))
- **ETL :** Réactivation des exports cantines (Open Data & Metabase) à une fréquence journalière. ([#6725](https://github.com/betagouv/ma-cantine/issues/6725))
- **ETL :** Ajout de WasteMeasurements dans les exports brutes (dbt). ([#6705](https://github.com/betagouv/ma-cantine/issues/6705))

### Autres changements
- **Documentation :** Ajout d'une page expliquant les commandes en lien avec une campagne de télédéclaration. ([#6738](https://github.com/betagouv/ma-cantine/issues/6738))
- **Tests :** Correction de plusieurs tests suite aux modifications apportées. ([#6801](https://github.com/betagouv/ma-cantine/issues/6801), [#6781](https://github.com/betagouv/ma-cantine/issues/6781))
- **Sécurité :** Sanitize du paramètre 'next' pour prévenir les failles de sécurité. ([#6709](https://github.com/betagouv/ma-cantine/issues/6709))
