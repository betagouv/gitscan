## Changelog : ma-cantine (30 derniers jours, au 18 juin 2026)

### Résumé
Les dernières mises à jour de ma-cantine se concentrent sur l'amélioration de la gestion des achats, notamment en termes de données d'origine des produits et de duplication des achats. Des améliorations ont également été apportées aux diagnostics, avec un focus sur la détection des anomalies et le calcul des coûts. Enfin, des corrections et des refactorings techniques ont été effectués pour améliorer la stabilité et la maintenabilité du code.

### Évolutions fonctionnelles
- **Achats :** Ajout d'un sélecteur de cantine lors de la duplication d'un achat, facilitant ainsi la réutilisation des informations. [#6823](https://github.com/betagouv/ma-cantine/issues/6823)
- **Achats :** Modification de l'affichage des champs "EGalim" et "Origine" pour une meilleure clarté. [#6826](https://github.com/betagouv/ma-cantine/issues/6826)
- **Achats :** Mise à jour des valeurs autorisées pour les "Origines" et réorganisation des valeurs de "Définition de locale". [#6803](https://github.com/betagouv/ma-cantine/issues/6803)
- **Diagnostics :** Amélioration de la détection des diagnostics anormaux en identifiant ceux dont le coût du repas est inférieur à 0.1. [#6795](https://github.com/betagouv/ma-cantine/issues/6795)
- **Diagnostics :** Amélioration du script de remplissage des champs `invalid_reason_list` et `warning_reason_list` pour les bilans 1TD1Site. [#6820](https://github.com/betagouv/ma-cantine/issues/6820)
- **Ressources :** Ajout des livrables GT sanitaire et médico-social. [#6733](https://github.com/betagouv/ma-cantine/issues/6733)

### Évolutions techniques
- **API :** Refactorisation de l'API pour renvoyer un code 404 lorsque l'objet demandé n'appartient pas à la cantine concernée (Diagnostics, Waste Measurements, Teledeclaration). [#6816](https://github.com/betagouv/ma-cantine/issues/6816), [#6815](https://github.com/betagouv/ma-cantine/issues/6815), [#6814](https://github.com/betagouv/ma-cantine/issues/6814), [#6812](https://github.com/betagouv/ma-cantine/issues/6812)
- **API :** Utilisation de `IsCanteenManagerUrlParam` au lieu de `IsLinkedCanteenManager` pour une meilleure gestion des permissions. [#6815](https://github.com/betagouv/ma-cantine/issues/6815), [#6812](https://github.com/betagouv/ma-cantine/issues/6812)
- **Achats :** Amélioration des règles métiers pour s'assurer que la date d'achat n'est pas future et que les origines "EUROPE" et "FRANCE" ne cohabitent pas. [#6805](https://github.com/betagouv/ma-cantine/issues/6805), [#6804](https://github.com/betagouv/ma-cantine/issues/6804)
- **1TD1Site :** Ajout du champ `groupe_snapshot` aux diagnostics et affichage dans l'admin. [#6799](https://github.com/betagouv/ma-cantine/issues/6799), [#6818](https://github.com/betagouv/ma-cantine/issues/6818)
- **Diagnostics :** Calcul des champs agrégés et des pourcentages à chaque sauvegarde, au lieu de les calculer uniquement lors de la télédeclaration. [#6752](https://github.com/betagouv/ma-cantine/issues/6752)
- **Diagnostics :** Ajout d'un nouveau champ `cout_repas` pour stocker le coût du repas et éviter les recalculs. [#6753](https://github.com/betagouv/ma-cantine/issues/6753)
- **Diagnostics :** Ajout d'un nouveau champ `warning_reason_list` pour stocker des informations non bloquantes. [#6732](https://github.com/betagouv/ma-cantine/issues/6732)
- **Données Géo :** Suppression du code lié à l'API Adresse, car elle n'est plus utilisée. [#6787](https://github.com/betagouv/ma-cantine/issues/6787)
- **Cantines :** Suppression de l'appel à l'API Adresse lors de la création d'une cantine, corrigeant un problème dans le formulaire de création. [#6766](https://github.com/betagouv/ma-cantine/issues/6766)
- **Tests :** Correction de plusieurs tests suite à des modifications récentes. [#6781](https://github.com/betagouv/ma-cantine/issues/6781), [#6801](https://github.com/betagouv/ma-cantine/issues/6801)

### Autres changements
- **Documentation :** Ajout d'une page expliquant les commandes liées à une campagne de télédéclaration. [#6738](https://github.com/betagouv/ma-cantine/issues/6738)
- **Achats :** Renommage des champs du modèle en français pour une meilleure lisibilité. [#6765](https://github.com/betagouv/ma-cantine/issues/6765)
- **Achats :** Diverses corrections et améliorations sur le formulaire suite à des tests internes. [#6740](https://github.com/betagouv/ma-cantine/issues/6740)
- **Achats :** Remplacement de la vidéo explicative par un lien vers la documentation. [#6742](https://github.com/betagouv/ma-cantine/issues/6742)
