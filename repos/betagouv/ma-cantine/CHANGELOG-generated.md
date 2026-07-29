## Changelog : ma-cantine (30 derniers jours, au 28 juillet 2026)

### Résumé
Les dernières évolutions de ma-cantine se concentrent sur l'amélioration de la gestion des achats, notamment l'ajout de nouvelles informations sur les produits (origine, circuit court, etc.) et la refonte de l'API associée. Des améliorations ont également été apportées à la gestion des images des cantines et à la correction de bugs sur les formulaires et les imports.

### Évolutions fonctionnelles
- Ajout de la possibilité de passer un prix HT avec un séparateur virgule lors des imports d'achats.
- Correction du bug empêchant l'envoi du formulaire "Acteurs de l'écosystème".
- Correction de la colonne "definition_local_km" lors des imports d'achats.
- Ajout d'un bandeau de service réduit sur la page de contact.
- Amélioration de la distinction visuelle des libellés et des valeurs dans les formulaires d'achats.
- Remontée du bloc de facture dans l'interface d'achat.

### Évolutions techniques
- Refactor de la gestion des factures liées aux achats, permettant de les sauvegarder ou supprimer même si l'achat n'est pas valide.
- Ajout de nouvelles propriétés aux cantines : logo, gestionnaires.
- Développement d'endpoints API dédiés à la gestion des logos des cantines (récupération, upload, suppression).
- Refactor de l'API pour regrouper les endpoints par lots fonctionnels.
- Amélioration des URLs de certains endpoints API (Achats, Cantines).
- Ajout de la possibilité d'ignorer les validations lors de la sauvegarde ou suppression d'objets.
- Ajout de champs de date de création et de modification aux images des cantines.
- Ajout d'un endpoint API pour vérifier si les informations d'une cantine sont complètes.
- Ajout d'un nouveau champ `history_source` pour tracer l'origine des modifications des objets.
- Refactor de l'historisation des données.
- Amélioration de la documentation de l'API (ajout de descriptions, masquage de certains champs).
- Restriction de l'accès aux achats aux seuls éditeurs autorisés via OAuth2.
- Ajout d'un endpoint dédié à la création d'achats avec les nouvelles caractéristiques (origine, circuit court, etc.).

### Autres changements
- Correction d'un warning dans la console lié à la documentation Swagger.
- Correction d'un lien obsolète sur la page d'import des achats SIRET.
- Renommage d'une catégorie de produits ("Boulangerie / Pâtisserie fraîches et surgelées" -> "Boulangerie / Pâtisserie fraîches").
- Suppression d'un groupe snapshot de l'historisation des diagnostics.
- Mise à jour des dépendances et release de nouvelles versions (2026.40.2, 2026.40.1, 2026.40.0, 2026.39.1, 2026.39.0).
