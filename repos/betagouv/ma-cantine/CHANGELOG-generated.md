## Changelog : ma-cantine (30 derniers jours, au 13 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent principalement sur l'amélioration de la gestion des achats, notamment avec une refonte du formulaire et l'ajout de nouvelles fonctionnalités pour les caractéristiques des produits. Des corrections et améliorations techniques ont également été apportées, notamment au niveau de l'API et des diagnostics, pour une meilleure robustesse et une plus grande clarté du code.

### Évolutions fonctionnelles
- Le formulaire de création et de modification des achats a été amélioré avec une division des caractéristiques en 4 sections pour une meilleure organisation.
- Ajout de la possibilité de choisir "EUROPE" comme origine des produits dans les achats.
- Ajout des champs "caractéristiques" et "famille de produit" aux achats.
- Mise à jour des valeurs autorisées pour l'origine des produits et de l'ordre des valeurs de "Définition de locale".
- Ajout des livrables GT sanitaire et médico-social aux ressources.
- Remplacement de l'ancienne URL par la nouvelle URL officielle pour les achats.
- Ajout d'une autocomplétion pour les champs "Description" et "Fournisseurs" dans les achats.
- Ajout d'une vidéo explicative (remplacée par un lien vers la documentation) sur le formulaire d'achat.

### Évolutions techniques
- Refactorisation de l'API pour utiliser `IsCanteenManagerUrlParam` au lieu de `IsLinkedCanteenManager` pour une meilleure cohérence.
- Amélioration de la gestion des erreurs en renvoyant un code 404 lorsque l'objet n'appartient pas à la cantine.
- Amélioration des calculs d'agrégation pour gérer correctement l'origine "EUROPE".
- Suppression du code lié à l'ancienne API Adresse, simplifiant ainsi le code et améliorant la performance.
- Amélioration des tests et correction de tests cassés suite aux refactorisations.
- Amélioration du script de remplissage des champs "calculés" pour les diagnostics.
- Ajout de nouveaux querysets pour faciliter le filtrage des données de diagnostic.
- Ajout d'un nouveau champ `cout_repas` pour stocker le coût du repas et éviter les recalculs.
- Amélioration des scripts de remplissage des champs `warning_reason_list` et `invalid_reason_list` pour les diagnostics.
- Suppression du script `field_gen.py` car il n'est plus utilisé.
- Correction d'un bug empêchant la création de cantines via l'API OAuth2.
- Correction de l'export Open Data.

### Autres changements
- Ajout d'une page de documentation expliquant les commandes liées à une campagne de télédéclaration.
- Mise à jour des données PAT (Produits d'Accueil et de Territoire) pour le frontend.
- Correction de quelques tests et amélioration de la lisibilité du code.
- Mise à jour des dépendances et publication de nouvelles versions (2026.37.1, 2026.36.1, 2026.35.0, 2026.34.0, 2026.33.4, 2026.33.3).
