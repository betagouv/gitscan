## Changelog : docs (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilité et l'expérience utilisateur, avec des corrections de bugs concernant la gestion des documents, l'interface utilisateur et les tests. Des améliorations significatives ont été apportées à la gestion des événements pour le suivi analytique, ainsi qu'à l'infrastructure de construction et de déploiement. Une nouvelle fonctionnalité de mode présentateur a été ajoutée.

### Évolutions fonctionnelles
- Ajout du mode présentateur pour faciliter les présentations de documents [#2321].
- Possibilité de quitter un document [#2365].
- Amélioration de la recherche avec l'ajout de breadcrumbs dans les résultats [#2310].
- Prise en charge de la création de sous-documents à partir de fichiers [#1987].
- Ajout d'un utilitaire pour capturer des événements avec PostHog pour un meilleur suivi analytique.
- Ajout d'une option pour activer/désactiver l'accès à tous les documents via un paramètre de configuration [#2378].

### Évolutions techniques
- Migration de l'outil de gestion des dépendances de `pip` à `uv` pour améliorer la performance et la fiabilité de la construction [#2363].
- Refonte de l'infrastructure de construction avec l'utilisation de `uv_build` comme backend de construction.
- Amélioration de la gestion des connexions de base de données pour éviter les erreurs de verrouillage.
- Utilisation de runners ARM64 pour la construction d'images pour l'architecture ARM64.
- Mise à jour de Next.js vers la version 16.2.6 (correction de sécurité) [#2386].
- Amélioration de la gestion des erreurs et des conditions de concurrence dans le backend.
- Mise à jour de Blocknote vers la version 0.51.4 [#2399].

### Autres changements
- Corrections de bugs concernant l'affichage du titre dans la table des matières [#2399].
- Correction de problèmes de crash liés aux threads orphelins [#2395].
- Amélioration de l'accessibilité de l'interface utilisateur, notamment pour le menu mobile et les avatars décoratifs [#2324, #2377].
- Ajout de tests E2E pour le mode présentateur [#2377].
- Mise à jour des traductions [#2396].
- Suppression de code inutilisé et nettoyage du code.
- Ajout de la prise en charge du déploiement sur PaaS (Scalingo) [#2293].
- Amélioration de la gestion des événements lors de la création, suppression, duplication et importation de documents.
- Correction de problèmes d'affichage et de comportement de l'interface utilisateur (barre flottante, panneaux latéraux).
- Correction de problèmes liés à l'impression des documents (commentaires).
- Ajout de la configuration de PostHog dans l'environnement Helm.
- Correction de problèmes de verrouillage lors de la création de documents.
- Amélioration de la gestion des erreurs lors de la migration de la base de données.
- Correction de problèmes de compatibilité avec GTranslate.
- Correction de problèmes d'exportation des liens lors de l'impression.
