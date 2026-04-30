## Changelog : code-du-travail-numerique (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la recherche, la correction de bugs et l'ajout de nouvelles fonctionnalités comme une page "Quoi de neuf" et une illustration sur les outils. Des efforts ont également été faits pour améliorer la robustesse de l'application et la gestion des données personnelles.

### Évolutions fonctionnelles
- **Recherche :** Amélioration du moteur de recherche avec un boost des contributions dans les résultats [#7229, #7217, #7246].
- **Recherche :** Sauvegarde de l'état de la recherche lors des navigations avant/arrière [#7255].
- **Recherche :** Correction de l'exact match pour les thèmes de recherche [#7247].
- **RGPD :** Ajout d'un avertissement lors de la saisie de données personnelles dans les commentaires [#7244].
- **RGPD :** Mise à jour du bandeau cookie [#7248].
- **Quoi de neuf :** Mise en avant de la page "Quoi de neuf" [#7249].
- **Outils :** Ajout d'une illustration du bulletin de paie sur le préavis de démission [#7210].
- **Contributions :** Redirection automatique vers la convention collective après sauvegarde dans le header [#7203].
- **Indemnité de licenciement :** Correction de la cohérence du message et suppression d'une question inutile [#7236, #7237].

### Évolutions techniques
- **Elasticsearch :** Migration vers une instance interne d'Elasticsearch [#7256].
- **Tests :** Migration des tests e2e de Cypress vers Playwright [#7212].
- **Sentry :** Correction des erreurs remontées par Sentry [#7225].
- **Recherche :** Renommage des labels pour les contributions et autres pages [#7227].
- **Actualités :** Ajout de la page listant les actualités [#7205].
- **Fiche MT :** Gestion des liens d'ancre sans `href` [#7223].
- **Actualités :** Ajout de JSON-LD et mise à jour du plan du site [#7224].

### Autres changements
- Corrections de bugs et améliorations de l'affichage des résultats de recherche [#7219].
- Corrections des tests e2e suite à l'ajout des actualités [#7220].
- Correction d'un mismatch dans la recherche des définitions [#7206].
- Corrections sur les titres, marges et liens de la page actualités [#7218].
- Correction de bugs divers et améliorations de la stabilité.
