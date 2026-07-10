## Changelog : ma-cantine (30 derniers jours, au 6 juillet 2026)

### Résumé
Les dernières mises à jour de ma-cantine améliorent l'expérience utilisateur dans la gestion des achats, notamment avec une meilleure présentation des informations et la prise en charge de nouveaux critères comme l'origine des produits et le circuit court. Des améliorations techniques importantes ont été apportées à l'historisation des données et à l'API, renforçant la traçabilité et la sécurité.

### Évolutions fonctionnelles
- **Achats :** Amélioration de la présentation visuelle des libellés et des valeurs dans les formulaires d'achat.
- **Achats :** Remontée du bloc facture pour une meilleure accessibilité.
- **Achats :** Ajout de la possibilité de dupliquer un achat en sélectionnant une cantine spécifique.
- **Achats :** Mise à jour des valeurs autorisées pour les origines et la définition du local.
- **Contact :** Ajout d'un bandeau de service réduit.
- **Ressources :** Ajout des nouveaux guides du CNRC.
- **Famille de produit :** Renommage de la catégorie 'Boulangerie / Pâtisserie fraîches' (suppression de 'et surgelées').
- **Imports :** Correction du lien vers l'ancienne page d'import des achats SIRET.
- **Achats :** Ajout de la prise en compte des critères "EGalim", "Origine", "Local" et "Circuit Court" dans les achats.

### Évolutions techniques
- **API :** Regroupement des endpoints API par lot fonctionnel pour une meilleure organisation.
- **API :** Correction de warnings dans la console Swagger.
- **API :** Restriction de l'accès aux achats aux seuls éditeurs autorisés via OAuth2.
- **API :** Ouverture de l'accès aux éditeurs (OAuth2) pour la création d'achats.
- **Historisation :** Ajout d'un nouveau champ `history_source_api_oauth2_application` pour suivre l'application ayant modifié un objet.
- **Historisation :** Ajout du champ `history_source` à plusieurs modèles (Cantine, Diagnostic, Mesure de gaspillage, Action sur les ressources).
- **Historisation :** Remplacement de `authentication_method` par `history_source`.
- **Historisation :** Déplacement des signaux dans le modèle pour une meilleure organisation.
- **Commandes de gestion :** Ajout d'une classe de base `MaCantineBaseCommand` pour gérer le loggage des résultats des commandes.
- **Commandes de gestion :** Loggage des résultats des commandes dans une table dédiée `CommandLog`.
- **Diagnostics :** Amélioration du script pour remplir les champs `invalid_reason_list` et `warning_reason_list`.
- **Diagnostics :** Marquage des TD avec un coût de repas inférieur à 0.1 comme aberrants.
- **API :** Amélioration de la gestion des erreurs 404 lorsque la cantine est inconnue.
- **API :** Utilisation de `IsCanteenManagerUrlParam` au lieu de `IsLinkedCanteenManager` pour une meilleure cohérence.

### Autres changements
- **Documentation API :** Masquage du champ `creation_source` dans Swagger.
- **Documentation API :** Remplissage du `help_text` des champs avec leur `verbose_name`.
- **Achats :** Correction d'un problème de pre-commit sur le fichier `achats.json`.
- **Achats :** Mise à jour des valeurs dans `definition_local` et ajout de `definition_local_km` suite aux modifications apportées.
- **Achats :** Ajustements sur le formulaire d'achat.
- **Achats :** Ajout de nouvelles propriétés `categories_egalim`, `origine`, `est_local` et `est_circuit_court`.
- **Achats :** Refonte de `definition_local` avec l'ajout d'un nouveau champ `definition_local_km` et modification des choix.
