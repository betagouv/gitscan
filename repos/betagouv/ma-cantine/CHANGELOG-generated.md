## Changelog : ma-cantine (30 derniers jours, au 21 juillet 2026)

### Résumé
Les dernières mises à jour de ma-cantine se concentrent sur l'amélioration de la gestion des achats, notamment avec l'ajout de nouvelles informations (origine, circuit court, distance locale) et une refonte de l'API pour faciliter l'intégration et l'utilisation. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées.

### Évolutions fonctionnelles
- Les achats permettent désormais de spécifier si un produit est d'origine locale, avec la possibilité de renseigner la distance en kilomètres.
- L'interface d'import des achats a été améliorée pour une meilleure expérience utilisateur.
- La page de contact affiche désormais un bandeau de service réduit.
- Les libellés des champs et leurs valeurs sont mieux distingués dans l'interface des achats.
- Le bloc de facture est maintenant remonté dans l'interface des achats.

### Évolutions techniques
- Une nouvelle API a été développée pour la création, la lecture, la modification et la suppression des achats, avec des caractéristiques divisées en quatre catégories.
- L'API a été améliorée pour permettre aux éditeurs (utilisateurs authentifiés via OAuth2) d'accéder uniquement à leurs propres achats.
- Refactor de la logique de gestion des cantines dans un nouveau fichier dédié.
- Amélioration des URLs de certains endpoints de l'API (cantines, achats).
- Ajout d'un nouveau champ `history_source_api_oauth2_application` pour suivre l'application ayant modifié un objet.
- Suppression du champ `groupe_snapshot` de l'historisation des diagnostics.
- Amélioration de la documentation de l'API (Swagger) et suppression du champ `creation_source`.
- Les signaux d'historisation ont été déplacés directement dans les modèles.

### Autres changements
- Correction d'un bug empêchant l'envoi du formulaire pour les acteurs de l'écosystème.
- Correction de la colonne "definition_local_km" dans les imports d'achats.
- Correction d'un bug lié à l'ancienne page d'import des achats SIRET.
- Correction d'un warning affiché dans la console Swagger.
- Renommage d'une catégorie de produits ("Boulangerie / Pâtisserie fraîches et surgelées" -> "Boulangerie / Pâtisserie fraîches").
- Ajout d'un endpoint `/check` pour vérifier l'état de remplissage et détecter les erreurs.
- Permettre de passer un prix HT avec un séparateur virgule lors de l'import d'achats.
