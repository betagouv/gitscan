## Changelog : ma-cantine (30 derniers jours, au 29 juillet 2026)

### Résumé
Les dernières mises à jour de ma-cantine se concentrent sur l'amélioration de la gestion des images et des logos des cantines, ainsi que sur l'ajout de nouveaux endpoints API pour faciliter l'accès et la manipulation de ces données. Des corrections et améliorations diverses ont également été apportées à l'interface et aux fonctionnalités existantes.

### Évolutions fonctionnelles
- Ajout de nouveaux endpoints API pour la gestion des images des cantines : récupération de la liste des images, ajout, suppression et modification d'images individuelles.
- Possibilité de récupérer des informations sur le remplissage et les erreurs d'une cantine via un nouvel endpoint API.
- Amélioration de la distinction visuelle des libellés et des valeurs dans la section "Achats".
- Ajout d'un bandeau de service réduit sur la page "Contact".
- Correction du lien vers l'ancienne page d'import des achats SIRET.

### Évolutions techniques
- Refactor de la logique de gestion des gestionnaires de cantines dans un nouveau fichier dédié.
- Simplification du serializer des factures dans la section "Achats".
- Ajout d'une nouvelle propriété pour le logo des cantines et affichage dans l'admin.
- Amélioration de l'URL de l'endpoint `teamJoin`.
- Amélioration des URLs des endpoints `summary` et `purchaseSummary`.
- Regroupement des endpoints API par lots fonctionnels pour une meilleure organisation.
- Ajout d'un champ de dates de création et de modification pour les images des cantines.
- Implémentation de `skip_validations` pour ignorer les validations lors de la suppression ou de la sauvegarde d'achats.
- Utilisation d'un nouveau queryset `has_invalid_reason` pour exclure facilement les TDs non valides.
- Correction d'un bug d'envoi du formulaire "Acteurs de l'écosystème".
- Correction de la colonne "definition_local_km" dans les nouveaux imports d'achats.
- Correction d'un bug lié à la duplication avec le nouveau format attendu pour les achats.
- Correction des warnings affichés dans la console Swagger.

### Autres changements
- Correction d'un bug dans la catégorie "Boulangerie / Pâtisserie fraîches" (suppression de "et surgelées").
- Permettre de passer un prix HT avec un séparateur virgule lors des imports d'achats.
