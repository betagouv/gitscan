## Changelog : docs (30 derniers jours, au 5 juin 2026)

### Résumé
Les dernières mises à jour apportent des améliorations à la stabilité et aux performances de l'application, notamment au niveau du backend et de la gestion des documents. L'interface utilisateur a également été améliorée avec l'ajout d'un panneau latéral pour les commentaires et un mode présentateur, ainsi que des corrections de bugs pour une meilleure expérience utilisateur. L'intégration de PostHog a été étendue pour un suivi plus précis des événements.

### Évolutions fonctionnelles
- Ajout d'un mode présentateur pour faciliter les présentations de documents [#2321].
- Ajout d'un panneau latéral dédié aux commentaires pour une meilleure organisation et accessibilité [#2379].
- Possibilité de quitter un document [#2365].
- Amélioration de la recherche avec l'ajout de breadcrumbs dans les résultats [#2310].
- Possibilité de créer un sous-document à partir d'un fichier [#1987].
- Ajout d'une fonctionnalité permettant de capturer des événements pour l'analyse avec PostHog (création/suppression de documents, actions IA, etc.) [#2363, #2364, #2366, #2367, #2368, #2369, #2370, #2371].
- Amélioration du support de l'importation de documents.

### Évolutions techniques
- Mise à jour de Blocknote vers la version 0.51.4 [#2374].
- Refonte de l'architecture pour déplacer les actions sur les documents (partage, commentaires) vers une barre flottante [#2374].
- Amélioration de la gestion des connexions de base de données pour éviter les erreurs lors des tests [#2385].
- Optimisation du streaming du contenu des documents côté backend [#2381].
- Utilisation d'uv pour la gestion des dépendances au lieu de pip.
- Ajout de support pour le déploiement sur PaaS (Scalingo) [#2293].
- Mise en place d'un service dédié pour la conversion Yjs avec Helm et Compose [#2358, #2305].
- Mise à jour de Next.js vers la version 16.2.6 (correction de sécurité) [#2329].

### Autres changements
- Corrections de bugs concernant l'affichage des titres longs dans la table des matières [#2399].
- Corrections de bugs d'interface utilisateur (crashs, affichage des icônes, comportement du focus, etc.) [#2395, #2372, #2373, #2375].
- Améliorations de l'accessibilité (aria-label, gestion du focus) [#2377, #2324].
- Mise à jour des traductions [#2396, #2377].
- Ajout de tests E2E pour le mode présentateur [#2322].
- Suppression de code obsolète et nettoyage du code [#2378, #2382].
- Ajout de configuration pour PostHog dans les environnements de développement et de fonctionnalités [#2378].
- Correction de problèmes de sécurité liés à la validation des ID de documents [#2323].
- Ajout de la possibilité de configurer l'endpoint utilisateur OIDC [#2306].
- Correction de problèmes liés à l'exportation des liens inter-documents en mode impression [#2269].
- Amélioration de la gestion des erreurs et des avertissements.
- Mise à jour des dépendances JavaScript [#2329, #2374].
