## Changelog : ma-cantine (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration du suivi de la création des données (cantines, diagnostics, achats) avec l'ajout de champs "creation_user". Des améliorations ont également été apportées aux achats, notamment au niveau du formulaire et des caractéristiques des produits. Enfin, des corrections et optimisations ont été réalisées sur les exports de données et les calculs.

### Évolutions fonctionnelles
- Ajout d'un champ "creation_user" pour suivre l'utilisateur ayant créé une cantine.
- Ajout d'un champ "creation_user" pour suivre l'utilisateur ayant créé un bilan (diagnostic).
- Ajout d'un champ "creation_user" pour suivre l'utilisateur ayant créé un achat.
- Amélioration du formulaire de création/modification d'achat avec une division des caractéristiques en 4 sections.
- Ajout de la définition "PAT" comme produit local.
- Mise à jour du texte explicatif du bandeau de démonstration.
- Ajout des livrables GT sanitaire et médico-social dans les ressources.
- Correction de l'URL des CGU (Conditions Générales d'Utilisation) vers le frontend.

### Évolutions techniques
- Amélioration des scripts de remplissage des champs "calculés" dans les diagnostics, incluant le nouveau champ `cout_repas`.
- Refactor de la logique de calcul des champs agrégés et des pourcentages dans les diagnostics, calculés à la sauvegarde plutôt qu'à la demande.
- Ajout de nouveaux querysets pour faciliter le filtrage des raisons d'alerte dans les diagnostics.
- Amélioration des tests pour la création de cantines via OAuth2.
- Optimisation des exports de données (Open Data et Metabase) pour les cantines et les télédéclarations.
- Correction d'un bug dans l'export Open Data.
- Amélioration des performances des calculs de statistiques pour les utilisateurs, en excluant les cantines supprimées.
- Refactor de l'API de validation des données.
- Sanitize du paramètre 'next' pour des raisons de sécurité.
- Suppression de code obsolète (script `field_gen.py`).
- Mise à jour des données de référence PAT.
- Suppression des tâches asynchrones liées à la récupération des données géographiques.

### Autres changements
- Documentation : Ajout d'une page expliquant les commandes liées à une campagne de télédéclaration.
- Correction de la dernière migration pour éviter un conflit.
- Diverses corrections suite à un recettage interne des achats.
- Remplacement de la vidéo explicative des achats par un lien vers la documentation.
- Mise à jour des dépendances Wagtail et Django.
