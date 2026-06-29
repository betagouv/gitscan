## Changelog : deno-buildpack (30 derniers jours, au 27 juin 2026)

### Résumé
Cette mise à jour permet désormais d'exécuter une tâche de construction (build) si elle est définie dans votre application Deno. Cela offre une plus grande flexibilité pour préparer votre application avant le déploiement sur Scalingo, notamment pour la compilation ou la génération de ressources statiques.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exécuter une tâche de construction définie dans le fichier `deno.json` ou via une variable d'environnement. [#1](https://github.com/betagouv/deno-buildpack/pull/1)

### Évolutions techniques
- Implémentation de la logique d'exécution de la tâche de construction en utilisant la commande `deno task`.
- Amélioration de la gestion des erreurs lors de l'exécution de la tâche de construction.

### Autres changements
- Aucune autre modification significative.
