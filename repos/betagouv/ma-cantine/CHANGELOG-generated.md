## Changelog : ma-cantine (30 derniers jours, au 2026-06-03)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration du suivi de la création des données (cantines, achats, diagnostics) avec l'ajout d'un champ "creation_user". Des corrections de bugs et des refactorings ont également été effectués pour améliorer la stabilité et la maintenabilité du code, notamment concernant l'API Adresse et les calculs d'agrégation pour les achats.

### Évolutions fonctionnelles
- Ajout d'un champ "creation_user" pour suivre l'utilisateur ayant créé une cantine.
- Ajout d'un champ "cout_repas" dans les diagnostics pour stocker cette information et éviter des recalculs.
- Amélioration du formulaire de création/modification d'achats avec une meilleure organisation des champs et des explications plus claires.
- Ajout de la définition de produit local "PAT" dans les achats.
- Mise à jour du texte explicatif du bandeau de démonstration.
- Correction d'un lien vers les CGU du frontend.

### Évolutions techniques
- Suppression de l'utilisation de l'API Adresse dans la création de cantines, corrigeant un bug dans le formulaire de création.
- Refactorings importants dans les modules Achats et Diagnostics pour améliorer la lisibilité, la maintenabilité et la testabilité du code.
- Séparation des calculs d'agrégation pour les achats (FRANCE vs CIRCUIT_COURT/LOCAL).
- Amélioration des scripts de remplissage des champs "calculés" dans les diagnostics.
- Ajout de nouveaux querysets pour faciliter le filtrage et l'accès aux données dans les modules Achats et Diagnostics.
- Sanityzation du paramètre 'next' pour renforcer la sécurité.
- Mise à jour des dépendances Wagtail et Django.

### Autres changements
- Ajout d'une page de documentation expliquant les commandes liées à la campagne de télédéclaration.
- Mise à jour des données PAT (Produits d'Agriculture de Territoire) pour le frontend.
- Correction d'un problème d'export Open Data.
- Amélioration des exports brutes pour inclure les WasteMeasurements.
- Suppression d'un script inutilisé (field_gen.py).
- Diverses corrections et améliorations suite à des tests internes.
