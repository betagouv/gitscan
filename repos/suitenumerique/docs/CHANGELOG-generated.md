## Changelog : docs (30 derniers jours, au 03 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur avec l'ajout d'un mode présentateur, d'un panneau latéral pour les commentaires, et des corrections de bugs pour une meilleure stabilité. Des améliorations techniques ont également été apportées, notamment la migration vers de nouveaux outils de build et de gestion des dépendances, ainsi que l'ajout de métriques de suivi d'événements pour mieux comprendre l'utilisation de la plateforme.

### Évolutions fonctionnelles
- Ajout du **mode présentateur** pour faciliter la présentation de documents [#2321].
- Implémentation d'un **panneau latéral dédié aux commentaires** pour une meilleure gestion et visibilité [#2379].
- Possibilité de **quitter un document** [#2365].
- Ajout d'une **breadcrumb** dans les résultats de recherche pour une navigation plus intuitive [#2310].
- Amélioration de l'**accessibilité** avec l'alignement des labels ARIA pour le menu mobile [#2377] et l'ajout d'attributs `aria-hidden` aux avatars décoratifs dans la modale de partage [#2324].
- Amélioration de la gestion des **permissions** pour empêcher les administrateurs de modifier les commentaires d'autres utilisateurs [#2323].

### Évolutions techniques
- Migration du système de build de `setuptools` vers `uv_build` pour une meilleure performance et une gestion plus moderne des dépendances [#2274, #2362].
- Migration de la gestion des dépendances de `pip` vers `uv` [#2362].
- Mise à jour de plusieurs dépendances JavaScript, incluant `Blocknote` (0.51.4) et `Next.js` (v16.2.6) [SECURITY] [#2273].
- Intégration de **métriques de suivi d'événements** avec PostHog pour analyser l'utilisation de la plateforme (création/suppression de documents, actions IA, accès, etc.) [#2363].
- Amélioration de la gestion des connexions WebSocket pour éviter les problèmes d'inactivité [#2264].
- Refonte de l'architecture pour séparer la configuration de PostHog [#2378].
- Ajout de support pour le déploiement sur des plateformes PaaS comme Scalingo [#2293].

### Autres changements
- Correction de plusieurs bugs et améliorations de la stabilité, notamment concernant la gestion des erreurs, l'affichage des emojis, et le comportement du menu Blocknote.
- Mise à jour de la documentation et des traductions [#2377].
- Amélioration de la gestion des tests E2E pour réduire les faux positifs [#2373].
- Suppression de code obsolète et nettoyage du code base.
- Correction de problèmes liés à l'importation de fichiers [#1987].
- Ajout de tests unitaires pour le mode présentateur [#2321].
- Correction d'un problème de verrouillage de table lors de la création de documents [#2274].
- Ajout de la validation de l'ID du document [#2323].
- Correction de problèmes de rendu dans le mode d'impression [#2269].
- Amélioration de la gestion des couleurs pour la sécurité [#2210].
- Correction de problèmes de focus et de visibilité dans l'interface utilisateur [#2377].
- Correction de problèmes de chargement des commentaires [#2269].
- Correction de problèmes de positionnement des éléments de l'interface utilisateur [#2379].
- Correction de problèmes de scroll dans la table des matières [#2233].
- Correction de problèmes de compatibilité avec certaines versions de Cunningham et de l'UI Kit [#2273].
