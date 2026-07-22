## Changelog : ma-cantine (30 derniers jours, au 21 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des achats, avec une refonte de l'interface et de l'API pour intégrer de nouvelles informations comme l'origine locale des produits et les catégories Egalim. Des corrections de bugs et des améliorations techniques ont également été apportées pour une meilleure stabilité et performance de la plateforme.

### Évolutions fonctionnelles
- Ajout d'un bandeau de service réduit sur la page contact.
- Amélioration de l'interface d'import des achats pour supporter les prix avec virgule comme séparateur décimal.
- Correction du bug empêchant l'envoi du formulaire "Acteurs de l'écosystème".
- Correction de l'affichage de la colonne "definition_local_km" lors de l'import des achats.
- Amélioration de la distinction visuelle des libellés et des valeurs dans le formulaire d'achat.
- Restauration du lien vers l'ancienne page d'import des achats SIRET.

### Évolutions techniques
- Refactorisation de la logique de gestion des cantines pour une meilleure organisation du code.
- Amélioration des URLs de l'API pour les endpoints liés aux équipes et aux résumés d'achats.
- Ajout d'un nouvel endpoint `/check` pour vérifier l'état de remplissage et détecter les erreurs des cantines.
- Mise en place d'un logger pour les résultats des commandes de gestion, stockés dans une nouvelle table `CommandLog`.
- Ajout des champs `creation_user` et `creation_source` pour suivre l'origine des créations et modifications d'objets.
- Refactorisation des validateurs d'évaluation du gaspillage.
- Amélioration de la gestion des accès à l'API pour les éditeurs (OAuth2).
- Refonte de la gestion des caractéristiques des achats (origine, circuit court, local) avec de nouveaux champs et une API dédiée.
- Correction d'un warning dans la console Swagger.

### Autres changements
- Documentation de l'API mise à jour pour cacher certains champs non pertinents.
- Remplissage des champs `creation_user` et `creation_source` dans les données existantes grâce à l'historisation.
- Nettoyage du code et des tests dans le module d'évaluation du gaspillage.
- Correction d'un problème de pre-commit sur le fichier `achats.json`.
- Suppression d'un groupe snapshot de l'historisation des diagnostics.
- Ajout d'un nouveau champ `history_source_api_oauth2_application` pour tracer l'application OAuth2 ayant modifié un objet.
- Ajout de `history_source` à d'autres modèles (Canteen, Diagnostic, WasteMeasurement, ResourceAction).
- Remplacement de `authentication_method` par `history_source`.
- Déplacement des signals dans les modèles.
