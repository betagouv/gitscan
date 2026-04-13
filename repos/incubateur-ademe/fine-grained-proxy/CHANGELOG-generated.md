## Changelog : fine-grained-proxy (30 derniers jours, au 11 avril 2026)

### Résumé
Le projet a connu une refonte majeure au cours des dernières semaines, avec une attention particulière portée à l'expérience utilisateur et à la qualité du code. L'interface a été complètement repensée pour une meilleure ergonomie, notamment avec l'ajout de filtres de corps de requête et une disposition plus claire. Des améliorations significatives ont également été apportées à la documentation, aux tests et à l'infrastructure de déploiement.

### Évolutions fonctionnelles
- **Filtres de corps de requête :** Ajout de la possibilité de filtrer le corps des requêtes en fonction de différents critères (type de données, exclusion, etc.) [#60cfba5](https://github.com/incubateur-ademe/fine-grained-proxy/commit/60cfba5).
- **Interface utilisateur améliorée :** Refonte de l'interface utilisateur avec une disposition divisée en deux parties (formulaire et documentation contextuelle) pour une meilleure clarté et une expérience utilisateur plus intuitive [#770905c](https://github.com/incubateur-ademe/fine-grained-proxy/commit/770905c).
- **Scopes :** Prise en charge de glob multi-segments dans les scopes [#0f6ee18](https://github.com/incubateur-ademe/fine-grained-proxy/commit/0f6ee18).
- **Presets :** Amélioration de l'UX des presets (label et hint) et mise à jour du guide de déploiement Deno Deploy [#0c084df](https://github.com/incubateur-ademe/fine-grained-proxy/commit/0c084df).
- **Compatibilité Tailscale :** Ajout de la compatibilité avec Tailscale [#ba17ad6](https://github.com/incubateur-ademe/fine-grained-proxy/commit/ba17ad6).
- **Documentation :** Ajout de guides de déploiement et amélioration de la documentation existante [#c965ca7](https://github.com/incubateur-ademe/fine-grained-proxy/commit/c965ca7).

### Évolutions techniques
- **Refactoring du client :** Refactorisation majeure du code client, passant d'un fichier monolithique à une architecture modulaire avec 10 modules TypeScript [#74d4446](https://github.com/incubateur-ademe/fine-grained-proxy/commit/74d4446).
- **TypeScript et esbuild :** Migration vers TypeScript et utilisation d'esbuild pour le build [#d1d8ee1](https://github.com/incubateur-ademe/fine-grained-proxy/commit/d1d8ee1).
- **Tests :** Amélioration de la suite de tests avec des tests nommés par Acceptation Criteria (AC), une matrice de couverture et une intégration CI/CD [#d5e7eca](https://github.com/incubateur-ademe/fine-grained-proxy/commit/d5e7eca).
- **Deno Deploy :** Ajout de la configuration de déploiement dans `deno.json` et une recette e2e complète pour Deno Deploy [#424f7ba](https://github.com/incubateur-ademe/fine-grained-proxy/commit/424f7ba).
- **OpenAPI :** Génération automatique de la documentation OpenAPI à partir des schémas Zod [#89ef62e](https://github.com/incubateur-ademe/fine-grained-proxy/commit/89ef62e).
- **Tailwind :** Utilisation de Tailwind avec build-time configuration [#c9ca824](https://github.com/incubateur-ademe/fine-grained-proxy/commit/c9ca824).

### Autres changements
- **Netlify Edge Functions :** Adaptation pour le déploiement sur Netlify Edge Functions [#22fd8da](https://github.com/incubateur-ademe/fine-grained-proxy/commit/22fd8da).
- **Suppression de code obsolète :** Suppression du tracking du skills marketplace du git [#deccd78](https://github.com/incubateur-ademe/fine-grained-proxy/commit/deccd78).
- **Améliorations diverses :** Corrections de bugs, améliorations de l'accessibilité (a11y), ajustements de l'UI et mises à jour de la documentation [#f6385e8](https://github.com/incubateur-ademe/fine-grained-proxy/commit/f6385e8).
- **Mise à jour des dépendances :** Mise à jour de Zod et @hono/zod-openapi [#39befae](https://github.com/incubateur-ademe/fine-grained-proxy/commit/39befae).
