## Changelog : ma-cantine (30 derniers jours, au 6 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives sur la gestion des achats, notamment l'ajout de nouvelles informations liées à l'origine des produits (circuit court, local) et la refonte de l'API pour faciliter leur intégration. Des améliorations ont également été apportées à l'historisation des données et à la gestion des diagnostics.

### Évolutions fonctionnelles
- Ajout d'un bandeau de service réduit sur la page Contact.
- Amélioration de la distinction visuelle des libellés et valeurs dans les formulaires d'achats.
- Remontée du bloc de facture dans les achats.
- Possibilité de dupliquer un achat en sélectionnant une autre cantine.
- Ajout de nouveaux guides du CNRC dans la section Ressources.
- Correction du lien vers l'ancienne page d'import des achats SIRET.
- Renommage de la catégorie 'Boulangerie / Pâtisserie fraîches' (suppression de 'et surgelées').

### Évolutions techniques
- Refonte de l'API des achats : nouveaux endpoints pour la création, la lecture, la modification et la suppression des achats, ainsi que pour la gestion des factures.
- Ajout de champs pour l'origine des produits (categories_egalim, origine, est_local, est_circuit_court) et de la définition du local avec un champ pour la distance en km.
- Amélioration de l'historisation des données : ajout d'un champ `history_source` pour identifier l'application ayant modifié un objet, et propagation de ce champ à plusieurs modèles (Canteen, Diagnostic, WasteMeasurement, ResourceAction).
- Remplacement de `authentication_method` par `history_source` dans l'historisation.
- Déplacement des signaux d'historisation dans les modèles.
- Amélioration de la gestion des logs pour les commandes de gestion.
- Ajout de champs `creation_user` et `creation_source` pour suivre l'origine de la création des données.
- Correction de bugs dans le script de remplissage des champs `invalid_reason_list` et `warning_reason_list` pour les diagnostics.
- Marquage des TD avec un coût repas inférieur à 0.1 comme aberrantes.
- Regroupement des endpoints API par lot fonctionnel.
- Amélioration de l'affichage des champs "EGalim" et "Origine" dans les achats.

### Autres changements
- Documentation de l'API : masquage du champ `creation_source` dans Swagger et remplissage du `help_text` des champs avec leur `verbose_name`.
- Correction de warnings affichés dans la console Swagger.
- Ajustements sur le formulaire d'achats.
- Mise à jour des valeurs dans `definition_local` et ajout de `definition_local_km` pour les imports.
- Suppression de la dépendance à un fichier `achats.json` obsolète.
