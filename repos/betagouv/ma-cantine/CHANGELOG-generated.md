## Changelog : ma-cantine (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, les évolutions de ma-cantine se concentrent sur l'amélioration de la gestion des achats, notamment avec une refonte du formulaire et l'ajout de nouvelles caractéristiques. Des corrections et des optimisations techniques ont également été apportées, en particulier au niveau de l'API et de la gestion des données, pour une meilleure performance et fiabilité de la plateforme.

### Évolutions fonctionnelles
- **Achats :** Ajout d'un sélecteur de cantine lors de la duplication d'un achat, facilitant la réutilisation des informations. [#6823](https://github.com/betagouv/ma-cantine/issues/6823)
- **Achats :** Refonte du formulaire de création et de modification d'achat avec une division des caractéristiques en quatre sections pour une meilleure organisation. [#6720](https://github.com/betagouv/ma-cantine/issues/6720)
- **Achats :** Ajout des champs "Caractéristiques" et "Famille de produit" pour une description plus précise des achats. [#6782](https://github.com/betagouv/ma-cantine/issues/6782)
- **Achats :** Ajout de la possibilité de modifier un achat directement depuis le nouveau formulaire. [#6783](https://github.com/betagouv/ma-cantine/issues/6783)
- **Achats :** Amélioration de l'autocomplétion dans les champs "Description" et "Fournisseurs" pour une saisie plus rapide et précise. [#6797](https://github.com/betagouv/ma-cantine/issues/6797)
- **Achats :** Ajout de la caractéristique "EUROPE" pour une meilleure catégorisation des origines des produits. [#6708](https://github.com/betagouv/ma-cantine/issues/6708)
- **Ressources :** Ajout des livrables GT sanitaire et médico-social. [#6733](https://github.com/betagouv/ma-cantine/issues/6733)
- **Bandeau Démo :** Mise à jour du texte explicatif. [#6717](https://github.com/betagouv/ma-cantine/issues/6717)

### Évolutions techniques
- **API :** Amélioration de la gestion des permissions et des accès aux données via l'utilisation de `IsCanteenManagerUrlParam` pour une meilleure sécurité et cohérence. [#6815](https://github.com/betagouv/ma-cantine/issues/6815), [#6812](https://github.com/betagouv/ma-cantine/issues/6812), [#6814](https://github.com/betagouv/ma-cantine/issues/6814)
- **API :** Correction pour renvoyer un code 404 lorsque l'objet demandé n'appartient pas à la cantine concernée. [#6816](https://github.com/betagouv/ma-cantine/issues/6816)
- **Achats :** Refactorisation des règles métiers pour garantir la cohérence des données (dates futures, incompatibilité FRANCE/EUROPE). [#6805](https://github.com/betagouv/ma-cantine/issues/6805), [#6804](https://github.com/betagouv/ma-cantine/issues/6804)
- **Diagnostics :** Amélioration du script de remplissage des champs `invalid_reason_list` et `warning_reason_list`. [#6820](https://github.com/betagouv/ma-cantine/issues/6820)
- **Diagnostics :** Ajout du champ `cout_repas` pour stocker le coût du repas et éviter les recalculs. [#6753](https://github.com/betagouv/ma-cantine/issues/6753)
- **Diagnostics :** Ajout du champ `warning_reason_list` pour stocker des informations non bloquantes sur les diagnostics. [#6732](https://github.com/betagouv/ma-cantine/issues/6732)
- **1TD1Site :** Ajout du champ `groupe_snapshot` pour les TD générées. [#6799](https://github.com/betagouv/ma-cantine/issues/6799)
- **Données Géo :** Suppression du code lié à l'API Adresse, qui n'est plus utilisée. [#6787](https://github.com/betagouv/ma-cantine/issues/6787)
- **ETL :** Restauration de la fréquence d'export des données des cantines (Open Data & Metabase) à quotidien. [#6725](https://github.com/betagouv/ma-cantine/issues/6725)
- **ETL :** Désactivation temporaire des exports de télédéclaration vers Metabase. [#6723](https://github.com/betagouv/ma-cantine/issues/6723)

### Autres changements
- **Documentation :** Ajout d'une page expliquant les commandes liées à une campagne de télédéclaration. [#6738](https://github.com/betagouv/ma-cantine/issues/6738)
- **Tests :** Correction de plusieurs tests suite aux modifications récentes. [#6801](https://github.com/betagouv/ma-cantine/issues/6801), [#6781](https://github.com/betagouv/ma-cantine/issues/6781)
- **Release :** Publication des versions 2026.37.1, 2026.37.0, 2026.36.1, 2026.36.0, 2026.35.0, 2026.34.0, 2026.33.4 et 2026.33.3. [#6802](https://github.com/betagouv/ma-cantine/issues/6802), [#6785](https://github.com/betagouv/ma-cantine/issues/6785), [#6762](https://github.com/betagouv/ma-cantine/issues/6762), [#6749](https://github.com/betagouv/ma-cantine/issues/6749), [#6744](https://github.com/betagouv/ma-cantine/issues/6744), [#6739](https://github.com/betagouv/ma-cantine/issues/6739), [#6721](https://github.com/betagouv/ma-cantine/issues/6721)
