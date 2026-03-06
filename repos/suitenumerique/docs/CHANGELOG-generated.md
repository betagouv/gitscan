## Changelog : docs (30 derniers jours)

### Résumé
Les 30 derniers jours ont été marqués par des améliorations significatives de l'expérience utilisateur, notamment l'ajout de la fonctionnalité de déplacement de documents, des améliorations de l'accessibilité et des corrections de bugs. Des efforts ont également été déployés pour améliorer la sécurité et l'infrastructure du projet, ainsi que pour intégrer de nouvelles fonctionnalités d'IA.

### Évolutions fonctionnelles
- Ajout de la fonctionnalité de déplacement de documents avec confirmation et gestion des demandes d'accès [#1886].
- Intégration de la nouvelle fonctionnalité Blocknote AI, contrôlée par des flags de fonctionnalité [#1847].
- Possibilité d'imprimer un document directement depuis le navigateur [#1832].
- Ajout de paramètres UTM aux liens de partage de documents pour un meilleur suivi [#1896].
- Barre flottante avec bouton de réduction du panneau latéral [#1876].
- Gestion des demandes de réconciliation pour les comptes utilisateurs [#1878].
- Possibilité de dupliquer des sous-pages [#1893].
- Ajout de documentation pour les nouveaux utilisateurs [#1891].
- Ajout d'un ensemble d'icônes UI [#1943].

### Évolutions techniques
- Amélioration de l'infrastructure CI/CD avec l'ajout d'un workflow GHCR pour les forks [#1851].
- Optimisation du workflow Docker Hub [#1919].
- Mise à jour des dépendances frontend pour la compatibilité avec ESLint v10 [#1919].
- Utilisation de `uvicorn` pour servir le backend, améliorant potentiellement les performances [#1922].
- Refactorisation du composant `HorizontalSeparator` pour plus de flexibilité [#1943].
- Utilisation de pydantic AI pour gérer le protocole de flux de données Vercel [#1922].
- Extraction de la construction Docker dans une tâche dédiée pour une personnalisation plus facile [#1905].
- Réutilisation de l'architecture amd64 pour construire les images arm64 lorsque possible [#1905].
- Ajout de support pour la plateforme arm64 dans les builds d'images Docker [#1901].
- Amélioration de la configuration de l'AI pour le frontend [#1948].

### Autres changements
- Amélioration de la documentation README et ajout d'un hub de documentation [#1870].
- Corrections de bugs mineurs d'UX/UI [#1948].
- Ajout de tests E2E pour améliorer la stabilité [#1948].
- Ajout de fichiers `.trivyignore` et correction de vulnérabilités de sécurité (CVE) [#1915, #1906].
- Mise à jour des chaînes de traduction [#1948].
- Suppression de code obsolète lié aux templates [#1780].
- Amélioration de l'accessibilité avec la gestion du focus sur les modales et les dates [#1855, #1948].
- Correction de problèmes d'espacement dans les blocs de citation pour les anciens navigateurs [#1914].
- Suppression de logs de console inutiles [#1906].
- Amélioration de l'alignement des couleurs avec le thème Figma [#1869].
- Correction de bugs liés à l'export PDF [#1913].
- Mise à jour de la version de `pycrdt` à 0.12.47 [#1905].
- Suppression de la configuration `AI_STREAM` du backend [#1922].
- Suppression de code lié à l'ancien système de templates [#1780].
