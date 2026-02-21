## Changelog : decoupage-administratif-gem (30 derniers jours)

### Résumé
Cette nouvelle version de la gem apporte le support des codes postaux pour les communes, permettant ainsi des recherches plus précises. Des améliorations ont également été apportées à la gestion des erreurs et à la logique de correspondance des données. La version passe en 0.4.0 avec une documentation mise à jour.

### Évolutions fonctionnelles
- Ajout de l'attribut `codes_postaux` à la classe `Commune` pour exposer les codes postaux associés à chaque commune (ex: `commune.codes_postaux # => ["72110"]`) (#12)
- Amélioration de la méthode `where` pour supporter le filtrage sur des attributs de type tableau, comme les codes postaux (ex: `Commune.where(codes_postaux: ["72110", "72600"])`) (#12)
- Les messages d'erreur `NotFoundError` sont maintenant localisés en français.

### Évolutions techniques
- Ajout d'un attribut `code` à l'erreur `NotFoundError` pour faciliter l'identification de la cause de l'erreur.
- Refactorisation de la gestion des messages d'erreur dans la classe `BaseModel`.

### Autres changements
- Mise à jour de la version de la gem à 0.4.0 et mise à jour de la documentation `CHANGELOG.md`.
