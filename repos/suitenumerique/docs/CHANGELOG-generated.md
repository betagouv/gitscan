## Changelog : docs (30 derniers jours, au 20 juillet 2026)

### Résumé
Les 30 derniers jours ont été marqués par des améliorations significatives de l'interface utilisateur, notamment une refonte de l'en-tête avec une barre flottante, l'ajout d'un menu utilisateur et des corrections d'accessibilité. Des améliorations ont également été apportées au backend, notamment la gestion des connexions de collaboration et la documentation sur la configuration de l'environnement.

### Évolutions fonctionnelles
- Ajout d'un menu utilisateur pour une meilleure gestion du profil et des paramètres [#2463].
- Refonte de l'en-tête avec une barre flottante pour une navigation plus intuitive [#2471].
- Possibilité de réinitialiser un document via une commande de gestion dédiée [#1882].
- Amélioration de la recherche de documents en utilisant l'ID plutôt que le chemin [#2501].
- Ajout d'un bouton pour créer des sous-documents [#2423].
- Ajout de liens "mailto" dans le menu d'aide pour faciliter le contact [#2416].
- Restauration du lien "skip to content" après la refonte de l'en-tête [#2510].
- Ajout d'un badge DPG au README pour une meilleure visibilité [#2450].

### Évolutions techniques
- Refactorisation du composant de présentation des diapositives pour une meilleure réutilisabilité.
- Optimisation de la gestion des connexions de collaboration pour une meilleure performance.
- Mise à jour de la documentation pour expliquer la configuration de l'utilisation de S3 et des mécanismes de sécurité de la collaboration [#2481].
- Amélioration de la performance de l'arbre de navigation [#2498].
- Suppression d'un backend d'authentification inutilisé [#2480].
- Amélioration de la gestion des erreurs dans le fournisseur Yjs, avec envoi des erreurs à Sentry [#2456].
- Correction de problèmes de performance liés aux requêtes N+1 lors de la sérialisation des commentaires [#2415].

### Autres changements
- Mise à jour des chaînes de traduction [#2420].
- Correction de typos dans le guide de contribution [#2459].
- Mise à jour des dépendances JavaScript [#2454].
- Amélioration de l'accessibilité de divers éléments de l'interface utilisateur, notamment les liens dans la table des matières, les titres, les champs de formulaire et les menus [#2449, #2421, #2450, #2380, #2390, #2383].
- Ajout d'un badge Snyk au README pour la sécurité [#2406].
- Suppression de Crisp du projet [#2416].
