## Changelog : ma-cantine (30 derniers jours, au 27 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des diagnostics et des achats, avec l'ajout de nouveaux champs pour un suivi plus précis et des corrections suite à des phases de recette. Des améliorations techniques ont également été apportées pour optimiser les requêtes et la gestion des données, notamment concernant les données géographiques et les exports.

### Évolutions fonctionnelles
- Ajout d'un champ `creation_user` pour identifier l'utilisateur ayant créé un achat, facilitant le suivi et l'audit.
- Ajout d'un champ `creation_user` pour identifier l'utilisateur ayant créé un diagnostic, améliorant la traçabilité.
- Introduction d'un nouveau champ `warning_reason_list` dans les diagnostics pour stocker des informations non bloquantes, permettant un signalement plus nuancé.
- Ajout de la définition "PAT" comme produit local dans la gestion des achats.
- Mise à jour de la documentation des achats avec un lien vers la documentation complète.
- Ajout d'un script permettant de remplir le nouveau champ `warning_reason_list` pour les diagnostics.
- Mise à jour du bandeau d'information concernant la campagne de correction.
- Ajout de livrables GT sanitaire et médico-social dans les ressources.

### Évolutions techniques
- Amélioration du script de remplissage du champ `warning_reason_list` dans les diagnostics (renommage de "gt" en "sup", ajout d'annotations).
- Création de nouveaux querysets pour faciliter le filtrage des `warning_reason_list` dans les diagnostics.
- Optimisation des querysets pour les diagnostics avec l'ajout de `with_label_sum` et `with_family_sum`.
- Refactoring de l'API des achats : nettoyage des champs renvoyés par l'endpoint `canteenPurchasesPercentageSummary`.
- Refactoring des tests de l'endpoint `createDiagnosticsFromPurchases` dans la gestion des achats.
- Nettoyage du code de l'administration des achats (lecture seule).
- Suppression du script `field_gen.py` car non utilisé.
- Amélioration de la gestion des données géographiques (PAT) avec une mise à jour du fichier de référence.
- Mise à jour des exports bruts (dbt) pour inclure les `WasteMeasurements`.
- Amélioration de la commande `diagnostic_fill_invalid_reason_list` pour une meilleure performance et un récapitulatif des statistiques.
- Correction de l'export Open Data suite à un problème de paramètre.
- Réparation des tests liés à la télédéclaration suite à des modifications récentes.
- Amélioration de la sécurité en sanitizant le paramètre 'next'.
- Refactoring de l'API de recherche d'entreprises pour éviter l'utilisation de camelCase dans les résultats.
- Mise à jour des dépendances Wagtail et Django.

### Autres changements
- Ajout d'une page de documentation expliquant les commandes liées à une campagne de télédéclaration.
- Correction d'un lien vers les CGU du frontend.
- Mise à jour du texte explicatif du bandeau de démonstration.
- Correction d'un problème de caractères spéciaux dans les données géographiques PAT.
- Suppression des tâches asynchrones liées à la récupération des données géographiques.
- Réactivation des exports cantines (Open Data & Metabase) à une fréquence journalière.
- Désactivation des exports de télédéclaration vers Metabase.
