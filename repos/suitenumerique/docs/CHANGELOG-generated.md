## Changelog : docs (30 derniers jours)

### Résumé
Les 30 derniers jours ont été marqués par des améliorations significatives de l'expérience utilisateur, notamment l'ajout d'un modal d'onboarding pour les nouveaux utilisateurs, des corrections de bugs liés à l'accessibilité et à l'interface, ainsi que des optimisations techniques pour améliorer la performance et la sécurité. L'intégration de nouvelles fonctionnalités, comme le déplacement de documents et l'intégration de l'IA, a également été au cœur des développements.

### Évolutions fonctionnelles
- Ajout d'un modal d'onboarding pour guider les nouveaux utilisateurs et leur présenter les fonctionnalités clés [#1868].
- Possibilité de déplacer des documents [#1886].
- Intégration de la fonctionnalité Blocknote AI, avec des indicateurs de statut et des options de configuration [#1847, #1922].
- Ajout de paramètres UTM aux liens de partage de documents pour un meilleur suivi analytique [#1896].
- Possibilité de dupliquer des sous-pages [#1893].
- Ajout d'une barre flottante avec un bouton pour réduire le panneau latéral [#1876].

### Évolutions techniques
- Mise à jour de Next.js vers la version 16 [#1980].
- Remplacement de `next lint` par `eslint` pour le linting du code [#1980].
- Amélioration de la taille des bundles frontend [#1980].
- Utilisation de `uvicorn` pour servir le backend, améliorant les performances [#1910].
- Ajout du support de la plateforme ARM64 pour les builds Docker [#1901].
- Refactorisation du code pour améliorer la flexibilité et la maintenabilité (HorizontalSeparator, gestion des modals).
- Amélioration de la gestion des erreurs et des conditions de course dans le backend (création de documents sandbox, accès aux documents onboarding).
- Mise à jour des dépendances Python et JavaScript.
- Amélioration de la configuration des jobs CI/CD (Docker Hub, builds multi-architecture).

### Autres changements
- Amélioration de la documentation et ajout d'un hub de documentation [#1870].
- Corrections de bugs d'accessibilité (navigation au clavier, focus, labels ARIA).
- Corrections de bugs d'interface utilisateur (flickering, positionnement des éléments).
- Ajout de tests E2E pour l'onboarding modal [#1989].
- Ajout de traductions pour les nouvelles fonctionnalités.
- Corrections de vulnérabilités de sécurité (CVE).
- Ajout d'un fichier `.trivyignore` pour ignorer certaines vulnérabilités connues.
- Amélioration de la gestion des flags de fonctionnalités (AI).
- Optimisation de la gestion des requêtes d'accès.
- Suppression de code obsolète (rust dans le back-builder).
