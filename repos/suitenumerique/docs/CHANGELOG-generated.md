## Changelog : docs (30 derniers jours, au 6 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur avec une refonte de l'interface (nouveau header, menu utilisateur, recherche), l'accessibilité (améliorations pour les lecteurs d'écran et la navigation au clavier) et des corrections de bugs pour une meilleure stabilité et fluidité. Des améliorations techniques ont également été apportées, notamment au niveau de la gestion des utilisateurs et de la performance.

### Évolutions fonctionnelles
- Ajout d'un menu utilisateur pour une meilleure gestion du profil et des préférences [#2463](https://github.com/suitenumerique/docs/issues/2463).
- Refonte du header avec un affichage flottant pour une navigation plus intuitive [#2471](https://github.com/suitenumerique/docs/issues/2471).
- Possibilité de quitter un document.
- Amélioration de la recherche : les utilisateurs non authentifiés peuvent désormais effectuer des recherches [#2407](https://github.com/suitenumerique/docs/issues/2407). La recherche inclut désormais le document parent.
- Ajout d'un bouton pour créer des sous-documents [#2423](https://github.com/suitenumerique/docs/issues/2423).
- Ajout d'une limite au nombre de réactions par commentaire.
- Ajout d'une commande de gestion pour réinitialiser un document [#1882](https://github.com/suitenumerique/docs/issues/1882).
- Possibilité d'ajouter des liens `mailto:` dans le menu d'aide.
- Ajout d'un badge DPG au README.

### Évolutions techniques
- Refactorisation de la suppression d'utilisateur pour une meilleure gestion des relations [#2437](https://github.com/suitenumerique/docs/issues/2437).
- Optimisation des requêtes pour la récupération des commentaires d'un fil de discussion [#2415](https://github.com/suitenumerique/docs/issues/2415).
- Amélioration de la gestion des connexions à la base de données pour les tests.
- Suppression de l'authentification par défaut non utilisée.
- Mise à jour de la dépendance PyJWT pour corriger une vulnérabilité de sécurité [#2481](https://github.com/suitenumerique/docs/issues/2481).
- Correction de problèmes liés au service worker causant des rechargements intempestifs.
- Amélioration de la performance de l'arbre de navigation.
- Correction de bugs liés à la gestion des documents supprimés.
- Mise à jour des dépendances JavaScript et correction de problèmes de sécurité.
- Amélioration de la gestion des conversions HTML/Markdown (préservation des éléments de formatage).

### Autres changements
- Amélioration de la documentation : explication de la configuration du format de conversion et de l'utilisation de S3.
- Correction de fautes de frappe dans le guide de contribution.
- Ajout de la configuration du `cacert` personnalisé dans le déploiement yprovider.
- Améliorations de l'accessibilité : liens de la table des matières, focus, annonces pour les lecteurs d'écran, etc.
- Suppression de Crisp.
- Correction de problèmes de positionnement de l'interface utilisateur.
- Suppression d'un job CI inutile.
- Ajout d'un badge Snyk au README.
- Correction de typos dans les paramètres.
