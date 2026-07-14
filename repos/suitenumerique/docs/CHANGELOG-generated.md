## Changelog : docs (30 derniers jours, au 2026-07-13)

### Résumé
Cette version apporte des améliorations à l'interface utilisateur, notamment une refonte de l'en-tête et du panneau latéral, ainsi que des corrections de bugs pour une meilleure expérience utilisateur. Des améliorations techniques ont également été apportées, notamment au niveau de la gestion des collaborations, de la recherche de documents et de la sécurité. La documentation a été enrichie avec des informations sur la configuration de la conversion de format et l'utilisation de S3.

### Évolutions fonctionnelles
- Ajout d'un menu utilisateur pour accéder aux paramètres et options du compte [#2463](https://github.com/suitenumerique/docs/issues/2463).
- Refonte de l'en-tête et harmonisation de la réactivité de l'interface [#2471](https://github.com/suitenumerique/docs/issues/2471).
- Ajout d'un bouton pour créer des sous-documents [#2423](https://github.com/suitenumerique/docs/issues/2423).
- Amélioration de la recherche de documents en utilisant l'ID au lieu du chemin [#2501](https://github.com/suitenumerique/docs/issues/2501).
- Ajout d'une commande de gestion pour réinitialiser un document [#1882](https://github.com/suitenumerique/docs/issues/1882).
- Possibilité de quitter un document [#2410](https://github.com/suitenumerique/docs/issues/2410).
- Amélioration de la recherche pour les utilisateurs non authentifiés [#2407](https://github.com/suitenumerique/docs/issues/2407).
- Limitation du nombre de réactions distinctes par commentaire [#1978](https://github.com/suitenumerique/docs/issues/1978).

### Évolutions techniques
- Correction d'une erreur de pointeur nul dans la configuration Helm pour les listes de tâches en arrière-plan [#2507](https://github.com/suitenumerique/docs/issues/2507).
- Amélioration de la gestion des connexions de collaboration pour une meilleure cascade de suppression [#2507](https://github.com/suitenumerique/docs/issues/2507).
- Configuration de la journalisation avec la propagation activée pour une meilleure traçabilité [#2507](https://github.com/suitenumerique/docs/issues/2507).
- Capture des erreurs de gestionnaire de conversion Yjs dans Sentry pour une meilleure surveillance [#2507](https://github.com/suitenumerique/docs/issues/2507).
- Suppression de l'authentification par défaut non utilisée [#2480](https://github.com/suitenumerique/docs/issues/2480).
- Mise à jour de la bibliothèque PyJWT pour corriger une faille de sécurité [#2480](https://github.com/suitenumerique/docs/issues/2480).
- Amélioration des performances de l'arbre de navigation [#2498](https://github.com/suitenumerique/docs/issues/2498).
- Correction de requêtes N+1 lors de la sérialisation des commentaires de discussion [#2415](https://github.com/suitenumerique/docs/issues/2415).

### Autres changements
- Mise à jour de la documentation pour expliquer la configuration du format de conversion et l'utilisation de S3 [#2481](https://github.com/suitenumerique/docs/issues/2481).
- Ajout d'un badge DPG au fichier README [#2459](https://github.com/suitenumerique/docs/issues/2459).
- Mise à jour des modèles de formulaires pour les issues [#2207](https://github.com/suitenumerique/docs/issues/2207).
- Correction de fautes de frappe dans le guide de contribution [#2459](https://github.com/suitenumerique/docs/issues/2459).
- Mise à jour des chaînes de traduction [#2516](https://github.com/suitenumerique/docs/issues/2516).
- Ajout d'un badge Snyk au fichier README [#2516](https://github.com/suitenumerique/docs/issues/2516).
- Suppression de Crisp du projet [#2416](https://github.com/suitenumerique/docs/issues/2416).
- Correction de problèmes d'accessibilité (aria-label, liens de table des matières, focus, etc.) [#2459](https://github.com/suitenumerique/docs/issues/2459), [#2449](https://github.com/suitenumerique/docs/issues/2449), [#2450](https://github.com/suitenumerique/docs/issues/2450), [#2421](https://github.com/suitenumerique/docs/issues/2421), [#2380](https://github.com/suitenumerique/docs/issues/2380), [#2390](https://github.com/suitenumerique/docs/issues/2390), [#2383](https://github.com/suitenumerique/docs/issues/2383), [#2384](https://github.com/suitenumerique/docs/issues/2384).
