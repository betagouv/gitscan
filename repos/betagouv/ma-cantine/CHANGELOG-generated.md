## Changelog : ma-cantine (30 derniers jours, au 2 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration du suivi de la création des données (cantines, achats, diagnostics) par les utilisateurs, ainsi que sur des optimisations et corrections de bugs, notamment concernant l'API Adresse et les exports de données. Des améliorations ont également été apportées aux achats et aux diagnostics, avec l'ajout de nouveaux champs et la refactorisation du code existant.

### Évolutions fonctionnelles
- Ajout d'un champ "creation_user" pour suivre l'utilisateur ayant créé une cantine.
- Ajout d'un champ "cout_repas" dans les diagnostics pour stocker cette information et éviter les recalculs.
- Amélioration du formulaire de création/modification d'achats avec une meilleure organisation des champs.
- Ajout de la définition "PAT" comme produit local dans les achats.
- Mise à jour du texte explicatif du bandeau de démonstration.
- Correction de l'URL des CGU pour pointer vers le frontend.

### Évolutions techniques
- Suppression de l'utilisation de l'API Adresse dans la création de cantines, résolvant un problème de formulaire.
- Refactorisation du code des achats pour améliorer la lisibilité et la maintenabilité (séparation des calculs d'agrégation, gestion des querysets).
- Amélioration des scripts de remplissage des champs "calculés" dans les diagnostics.
- Amélioration des tests de l'API, notamment pour la création de cantines et de diagnostics.
- Optimisation des exports de données (Open Data, Metabase) et correction d'un bug lié au paramètre datagouv.
- Suppression de code inutile lié à l'API Adresse.
- Suppression d'un script obsolète (field_gen.py).
- Amélioration de la gestion des caractéristiques des achats.
- Correction d'un conflit de migration.

### Autres changements
- Documentation : Ajout d'une page expliquant les commandes liées à une campagne de télédéclaration.
- Mise à jour des données PAT (Produits d'Agriculture Territoriale) pour le frontend.
- Mise à jour des dépendances Django et Wagtail.
