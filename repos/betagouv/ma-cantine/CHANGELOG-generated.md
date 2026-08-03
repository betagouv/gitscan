## Changelog : ma-cantine (30 derniers jours, au 29 juillet 2026)

### Résumé
Les dernières évolutions de ma-cantine se concentrent sur l'enrichissement de l'API, notamment pour la gestion des logos et des images des cantines. Des améliorations ont également été apportées à la gestion des achats et à la correction de bugs sur le formulaire des acteurs de l'écosystème et les imports d'achats.

### Évolutions fonctionnelles
- Ajout d'endpoints API pour la gestion des logos des cantines : récupération, ajout, modification et suppression.
- Ajout d'endpoints API pour la gestion des images des cantines : récupération de la liste des images, ajout, suppression et récupération d'une image spécifique.
- Ajout d'un endpoint API `/check` pour vérifier l'état de remplissage et la présence d'erreurs dans les données d'une cantine.
- Amélioration de la distinction visuelle des libellés et des valeurs dans l'interface d'import des achats.
- Correction du bug empêchant l'envoi du formulaire pour les acteurs de l'écosystème [#6895](https://github.com/betagouv/ma-cantine/issues/6895).
- Correction de la colonne "definition_local_km" dans les nouveaux imports d'achats [#6896](https://github.com/betagouv/ma-cantine/issues/6896).
- Correction du lien vers l'ancienne page d'import des achats SIRET [#6884](https://github.com/betagouv/ma-cantine/issues/6884).
- Ajout d'un bandeau de service réduit sur la page contact [#6889](https://github.com/betagouv/ma-cantine/issues/6889).
- Renommage de la catégorie "Boulangerie / Pâtisserie fraîches et surgelées" en "Boulangerie / Pâtisserie fraîches" [#6890](https://github.com/betagouv/ma-cantine/issues/6890).

### Évolutions techniques
- Refactor de la logique de gestion des gestionnaires de cantines dans un nouveau fichier `canteen_managers.py` [#6915](https://github.com/betagouv/ma-cantine/issues/6915).
- Simplification des serializers pour les factures des achats [#6949](https://github.com/betagouv/ma-cantine/issues/6949).
- Ajout d'une propriété "logo" pour les cantines et affichage dans l'admin [#6932](https://github.com/betagouv/ma-cantine/issues/6932).
- Amélioration des URLs pour les endpoints liés aux achats et aux équipes [#6912](https://github.com/betagouv/ma-cantine/issues/6912), [#6913](https://github.com/betagouv/ma-cantine/issues/6913).
- Refactor pour permettre d'ignorer les validations lors de la suppression ou de la sauvegarde d'achats [#6936](https://github.com/betagouv/ma-cantine/issues/6936), [#6937](https://github.com/betagouv/ma-cantine/issues/6937).
- Ajout d'un nouveau queryset `has_invalid_reason` pour exclure facilement les demandes de télédeclaration non valides [#6957](https://github.com/betagouv/ma-cantine/issues/6957).
- Regroupement des endpoints API par lots fonctionnels [#6886](https://github.com/betagouv/ma-cantine/issues/6886).
- Correction des warnings affichés dans la console Swagger [#6891](https://github.com/betagouv/ma-cantine/issues/6891).
- Mise à jour de la configuration pour pointer vers l'application OAuth2 définie dans les settings [#6928](https://github.com/betagouv/ma-cantine/issues/6928).

### Autres changements
- Amélioration de la remontée du bloc de facture dans l'interface d'import des achats [#6888](https://github.com/betagouv/ma-cantine/issues/6888).
- Permettre de passer un prix HT avec un séparateur virgule lors des imports d'achats [#6892](https://github.com/betagouv/ma-cantine/issues/6892).
- Publication des versions 2026.40.0, 2026.40.1, 2026.40.2 et 2026.41.0.
