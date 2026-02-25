## Changelog : communs-de-la-transition-ecologique-des-collectivites (30 derniers jours)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'espace "Ressources" avec l'ajout d'une page vocabulaire métier et d'une cartographie, ainsi que sur la correction de problèmes liés au proxy et à la conformité CNIL pour le suivi Matomo. Des corrections ont également été apportées au dashboard statistiques et à la gestion des chemins d'assets.

### Évolutions fonctionnelles
- Ajout d'une page "Vocabulaire métier" dans l'espace Ressources, remplaçant l'ancien iframe Notion par du contenu statique (#378).
- Ajout d'une cartographie dans l'espace Ressources, accessible via un proxy (#372).
- Amélioration de la page d'accueil et du proxy cartographie dans l'espace Ressources (#372).
- Correction d'une erreur CORS sur la page des statistiques (#379).
- Exclusion des catégories de test du dashboard statistiques pour une meilleure pertinence des données.
- Conformité CNIL pour le suivi Matomo, sans nécessiter de bannière de consentement (#377).

### Évolutions techniques
- Mise en place d'un proxy pour les analyses-convergence (#373).
- Correction de la réécriture des chemins dans le proxy pour les fichiers JavaScript (#373).
- Amélioration de la gestion des attributs HTML avec guillemets simples dans le proxy.
- Déplacement de `openapi-fetch` vers les dépendances pour corriger un problème de build (#376).
- Correction du script `prepare` pour le déploiement sur Scalingo (#375).
- Ajout du tracking Matomo sur toutes les pages statiques (#374).
- Réécriture des chemins d'assets dans le HTML proxié pour assurer le bon fonctionnement des ressources (#368).

### Autres changements
- Correction de l'URL d'embed Notion (#370).
- Affichage d'un indicateur de chargement pendant le chargement de l'iframe (#371).
- Plusieurs releases de version (0.1.8 à 0.1.20) pour intégrer les changements.
