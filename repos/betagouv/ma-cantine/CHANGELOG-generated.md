## Changelog : ma-cantine (30 derniers jours, au 19 juin 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives sur la gestion des achats, notamment avec la migration progressive de l'interface de création vers Vue.js et l'ajout de nouveaux champs pour une meilleure description des produits. Des efforts ont également été déployés pour améliorer la qualité des données des diagnostics, avec l'ajout de nouveaux champs et des scripts de correction. Enfin, des optimisations techniques ont été réalisées pour améliorer la performance et la robustesse de l'API.

### Évolutions fonctionnelles

*   **Achats :**
    *   Ajout d'un sélecteur de cantine lors de la duplication d'un achat. [#6823](https://github.com/betagouv/ma-cantine/issues/6823)
    *   Modification de l'affichage des champs "EGalim" et "Origine" pour une meilleure clarté. [#6826](https://github.com/betagouv/ma-cantine/issues/6826)
    *   Ajout des champs "caractéristiques" et "famille de produit" pour une description plus précise des achats. [#6782](https://github.com/betagouv/ma-cantine/issues/6782)
    *   Amélioration de l'autocomplétion des champs "Description" et "Fournisseurs". [#6797](https://github.com/betagouv/ma-cantine/issues/6797)
    *   Ajout de la possibilité de modifier un achat à partir du nouveau formulaire. [#6783](https://github.com/betagouv/ma-cantine/issues/6783)
*   **Diagnostics :**
    *   Marquage automatique des diagnostics avec un coût de repas inférieur à 0.1 comme aberrants. [#6795](https://github.com/betagouv/ma-cantine/issues/6795)
*   **Ressources :** Ajout des nouveaux guides du CNRC. [#6835](https://github.com/betagouv/ma-cantine/issues/6835)
*   **1TD1Site :** Ajout du champ `groupe_snapshot` aux diagnostics et affichage dans l'interface d'administration. [#6799](https://github.com/betagouv/ma-cantine/issues/6799)

### Évolutions techniques

*   **API :**
    *   Amélioration de la gestion des métadonnées pour éviter leur renvoi inutile. [#6829](https://github.com/betagouv/ma-cantine/issues/6829)
    *   Refactorisation de l'API pour utiliser `IsCanteenManagerUrlParam` au lieu de `IsLinkedCanteenManager` pour une meilleure cohérence. [#6815](https://github.com/betagouv/ma-cantine/issues/6815), [#6812](https://github.com/betagouv/ma-cantine/issues/6812), [#6814](https://github.com/betagouv/ma-cantine/issues/6814)
    *   Gestion des erreurs 404 lorsque la cantine n'est pas trouvée. [#6811](https://github.com/betagouv/ma-cantine/issues/6811)
    *   Amélioration de la gestion des autorisations pour les diagnostics et les mesures de gaspillage. [#6816](https://github.com/betagouv/ma-cantine/issues/6816)
*   **Achats :**
    *   Renommage des champs du modèle Achats en français. [#6765](https://github.com/betagouv/ma-cantine/issues/6765)
    *   Ajout de règles métiers pour valider la date des achats (pas dans le futur) et la compatibilité des origines (EUROPE et FRANCE). [#6805](https://github.com/betagouv/ma-cantine/issues/6805), [#6804](https://github.com/betagouv/ma-cantine/issues/6804)
*   **Diagnostics :**
    *   Amélioration des scripts de remplissage des champs `invalid_reason_list` et `warning_reason_list`. [#6820](https://github.com/betagouv/ma-cantine/issues/6820)
    *   Calcul des champs agrégés et des pourcentages à chaque sauvegarde du diagnostic. [#6752](https://github.com/betagouv/ma-cantine/issues/6752)
    *   Ajout de nouveaux querysets pour faciliter le filtrage des diagnostics. [#6736](https://github.com/betagouv/ma-cantine/issues/6736), [#6735](https://github.com/betagouv/ma-cantine/issues/6735)
    *   Ajout du champ `cout_repas` pour stocker le coût du repas. [#6753](https://github.com/betagouv/ma-cantine/issues/6753)
*   **Données Géo :** Suppression du code lié à l'API Adresse. [#6787](https://github.com/betagouv/ma-cantine/issues/6787)

### Autres changements

*   **Documentation :** Ajout d'une page expliquant les commandes liées à une campagne de télédéclaration. [#6738](https://github.com/betagouv/ma-cantine/issues/6738)
*   **Cantines :** Ajout du champ `creation_user` pour suivre l'utilisateur ayant créé la cantine. [#6750](https://github.com/betagouv/ma-cantine/issues/6750)
*   **Diagnostics :** Ajout du champ `creation_user` pour suivre l'utilisateur ayant créé le diagnostic. [#6746](https://github.com/betagouv/ma-cantine/issues/6746)
*   **Achats :** Ajout du champ `creation_user` pour suivre l'utilisateur ayant créé l'achat. [#6745](https://github.com/betagouv/ma-cantine/issues/6745)
