## Changelog : ma-cantine (30 derniers jours, au 13 juillet 2026)

### Résumé
Les dernières mises à jour de ma-cantine améliorent l'expérience utilisateur, notamment dans la gestion des achats avec une refonte de l'interface et de nouvelles fonctionnalités liées aux circuits courts et à l'origine des produits. Des corrections de bugs et des améliorations techniques ont également été apportées pour une meilleure stabilité et performance de la plateforme.

### Évolutions fonctionnelles
- Ajout d'un bandeau de service réduit pour le module Contact.
- Amélioration de la distinction visuelle des libellés et des valeurs dans le formulaire d'achats.
- Remontée du bloc de facture dans le module Achats.
- Renommage de la catégorie 'Boulangerie / Pâtisserie fraîches' en 'Boulangerie / Pâtisserie' dans la gestion des familles de produits.
- Ajout de nouveaux formats d'import pour les achats (SIRET).
- Ajout de guides du CNRC dans la section Ressources.
- Possibilité d'indiquer si un achat est un circuit court ou local, avec la possibilité de préciser la distance en kilomètres.
- Ouverture de l'accès aux éditeurs pour la création, la lecture, la modification et la suppression des achats via OAuth2.

### Évolutions techniques
- Refactor de l'historisation des données : ajout d'un nouveau champ pour identifier l'application OAuth2 ayant modifié un objet (cantine, diagnostic, etc.).
- Amélioration de la gestion des logs pour les commandes de gestion (ajout d'une table dédiée).
- Amélioration de l'API : regroupement des endpoints par lots fonctionnels et restriction de l'accès aux achats pour les éditeurs.
- Correction de warnings dans la console Swagger.
- Suppression de l'historisation du groupe snapshot pour les diagnostics.
- Déplacement des signaux dans les modèles pour une meilleure organisation.
- Masquage du champ `creation_source` dans la documentation Swagger.
- Remplissage des champs `creation_user` et `creation_source` pour les données existantes via l'historisation.

### Autres changements
- Correction de liens et de colonnes dans les imports d'achats.
- Correction du bug d'envoi du formulaire "Acteurs de l'écosystème".
- Mise à jour des serializers pour les achats.
- Amélioration de l'affichage des champs "EGalim" et "Origine" dans les achats.
- Correction d'un problème de pre-commit sur le fichier achats.json.
