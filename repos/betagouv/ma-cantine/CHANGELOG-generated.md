## Changelog : ma-cantine (30 derniers jours, au 30 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent principalement sur l'amélioration de la gestion des achats, notamment avec l'ajout de nouvelles informations sur l'origine des produits (circuit court, local, etc.) et la refonte de l'interface utilisateur pour la création et la modification des achats. Des améliorations techniques ont également été apportées pour le suivi des modifications des données et l'audit des actions réalisées par les utilisateurs.

### Évolutions fonctionnelles
- **Achats :** Ajout de nouveaux champs pour caractériser les achats : catégories ÉGalim, origine, indication si le produit est local ou en circuit court.
- **Achats :** Refonte de la définition du "local" avec la possibilité de spécifier une distance en kilomètres.
- **Achats :** Possibilité de dupliquer un achat en sélectionnant une cantine différente.
- **Achats :** Amélioration de l'autocomplétion des champs "Description" et "Fournisseurs" lors de la création d'un achat.
- **Achats :** L'API permet désormais de créer, modifier et supprimer des achats via un nouvel endpoint.
- **Achats :** Ajout d'un endpoint dédié à l'upload et la suppression de factures.
- **Ressources :** Ajout des nouveaux guides du CNRC.
- **Diagnostics :** Amélioration du script de remplissage des champs `invalid_reason_list` et `warning_reason_list`.
- **Diagnostics :** Les diagnostics avec un coût de repas inférieur à 0.1 sont maintenant marqués comme aberrants.

### Évolutions techniques
- **Historisation :** Ajout d'un nouveau champ `history_source` pour identifier l'application OAuth2 ayant modifié un objet (cantine, diagnostic, achat, évaluation de gaspillage).
- **Historisation :** Refactorisation du système d'historisation pour améliorer la traçabilité des modifications.
- **API :** Restriction de l'accès aux achats pour les éditeurs, qui ne peuvent désormais accéder qu'à leurs propres achats.
- **API :** Ouverture de l'accès aux achats pour les utilisateurs authentifiés via OAuth2.
- **API :** Amélioration de la gestion des erreurs et des codes de retour (retour d'un 404 si la cantine n'est pas trouvée).
- **Commandes de gestion :** Ajout d'une classe de base pour les commandes de gestion afin de faciliter le logging des résultats.
- **Commandes de gestion :** Les résultats des commandes de gestion sont maintenant enregistrés dans une table dédiée.
- **Tests :** Correction de tests cassés suite aux modifications apportées.
- **Refactoring :** Suppression du code lié à l'ancienne API Adresse.
- **Refactoring :** Simplification du code lié au calcul du coût des repas.

### Autres changements
- **Documentation :** Mise à jour de la documentation de l'API pour refléter les changements apportés.
- **Imports :** Ajout de support pour les nouveaux formats d'import des achats.
- **Imports :** Réorganisation de la page d'import.
- **Achats :** Renommage des champs du modèle Achats en français.
- **Achats :** Mise à jour des valeurs autorisées pour les champs "Origines" et "Définition de locale".
- **Achats :** Correction de divers problèmes d'affichage et de comportement du formulaire d'achat.
