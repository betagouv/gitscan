## Changelog : domifa (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, les évolutions de DomiFa se concentrent sur l'amélioration de la sécurité, la correction de bugs et l'optimisation des performances. Des validations de données plus strictes ont été ajoutées côté backend, ainsi qu'un système de limitation de requêtes (throttling) pour protéger l'application. Des corrections ont également été apportées à l'interface utilisateur et aux tests.

### Évolutions fonctionnelles
- Ajout d'une bannière DSFR à l'interface utilisateur frontend.
- Ajout d'un fichier `claude.md` (contenu inconnu).

### Évolutions techniques
- Implémentation d'un système de limitation de requêtes (throttling) pour améliorer la stabilité et la performance du backend.
- Désactivation du throttling pour les requêtes de vérification de l'état de santé (health check).
- Ajout de logs pour faciliter le débogage du throttling.
- Renforcement des règles de sécurité côté backend.
- Amélioration de la validation des données (DTO) côté backend : ajout de contraintes de longueur maximale et application stricte des DTO pour les contacts et les référents.
- Correction d'un problème dans les tests unitaires.
- Ajout de logs au backend.

### Autres changements
- Amélioration de la configuration du workflow de release pour inclure une branche dédiée aux corrections de sécurité.
- Corrections de la documentation du changelog.
- Ajout de `[skip ci]` à certains commits pour éviter des exécutions CI inutiles.
