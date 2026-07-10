## Changelog : docs (30 derniers jours, au 09 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment une refonte de l'interface utilisateur avec un nouveau menu utilisateur, une barre flottante et des améliorations de l'accessibilité. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des améliorations de la recherche et de la gestion des documents.

### Évolutions fonctionnelles
- Ajout d'un menu utilisateur pour une meilleure gestion du profil et des paramètres [#2463](https://github.com/suitenumerique/docs/issues/2463).
- Nouvelle barre flottante pour une navigation plus intuitive et un accès rapide aux fonctionnalités [#2471](https://github.com/suitenumerique/docs/issues/2471).
- Les utilisateurs non authentifiés peuvent désormais effectuer des recherches dans les documents [#2407](https://github.com/suitenumerique/docs/issues/2407).
- Possibilité de quitter un document [#2410](https://github.com/suitenumerique/docs/issues/2410).
- Ajout d'un bouton pour créer des sous-documents [#2423](https://github.com/suitenumerique/docs/issues/2423).
- Amélioration de la recherche pour inclure le document parent [#1952](https://github.com/suitenumerique/docs/issues/1952).
- Ajout d'une limite au nombre de réactions distinctes par commentaire [#1978](https://github.com/suitenumerique/docs/issues/1978).
- Ajout d'une commande de gestion pour réinitialiser un document [#1882](https://github.com/suitenumerique/docs/issues/1882).

### Évolutions techniques
- Refonte de la gestion de la suppression des utilisateurs pour une meilleure cohérence [#2480](https://github.com/suitenumerique/docs/issues/2480).
- Optimisation de la récupération des commentaires pour éviter les requêtes N+1 [#2415](https://github.com/suitenumerique/docs/issues/2415).
- Mise à jour de la dépendance PyJWT pour corriger une vulnérabilité de sécurité [#2480](https://github.com/suitenumerique/docs/issues/2480).
- Amélioration de la configuration du logging pour une meilleure traçabilité [#2507](https://github.com/suitenumerique/docs/issues/2507).
- Correction d'une erreur de pointeur nul dans la configuration Helm [#9551ea6](https://github.com/suitenumerique/docs/commit/9551ea6).
- Amélioration de la gestion de la connexion de collaboration pour une meilleure fiabilité [#d35b81a](https://github.com/suitenumerique/docs/commit/d35b81a).

### Autres changements
- Mise à jour de la documentation pour expliquer la configuration du format de conversion et l'utilisation de S3 [#9c9daff](https://github.com/suitenumerique/docs/commit/9c9daff).
- Mise à jour des modèles de formulaires pour les issues [#2207](https://github.com/suitenumerique/docs/issues/2207).
- Ajout d'un badge DPG au README [#5843d5a](https://github.com/suitenumerique/docs/commit/5843d5a).
- Ajout d'un badge Snyk au README [#3382e67](https://github.com/suitenumerique/docs/commit/3382e67).
- Améliorations de l'accessibilité (ARIA, focus management, liens d'ancrage) sur divers composants de l'interface utilisateur [#2459](https://github.com/suitenumerique/docs/issues/2459), [#2422](https://github.com/suitenumerique/docs/issues/2422), [#2390](https://github.com/suitenumerique/docs/issues/2390), [#2383](https://github.com/suitenumerique/docs/issues/2383).
- Mise à jour des chaînes de traduction [#11f3dcb](https://github.com/suitenumerique/docs/commit/11f3dcb).
- Correction de typos dans le guide de contribution [#c8e44dd](https://github.com/suitenumerique/docs/commit/c8e44dd).
- Suppression de Crisp du projet [#b9e4df7](https://github.com/suitenumerique/docs/commit/b9e4df7).
