## Changelog : meet (30 derniers jours, au 4 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à la sécurité, notamment des mises à jour de dépendances pour corriger des vulnérabilités.  De nouvelles fonctionnalités sont également introduites, comme la gestion des utilisateurs en doublon et l'amélioration de l'attribution des intervenants dans les résumés de réunion. L'expérience utilisateur est améliorée avec l'ajout de fonctionnalités PiP (Picture-in-Picture) et des améliorations de l'accessibilité. Des optimisations de performance sont également apportées, notamment au niveau du chargement des ressources frontend.

### Évolutions fonctionnelles
- Ajout d'une commande de gestion pour fusionner les utilisateurs en doublon [#1387].
- Amélioration de l'attribution des intervenants dans les résumés de réunion.
- Ajout d'une fonctionnalité Picture-in-Picture (PiP) avec contrôle de la connexion, menu d'options et barre de contrôle basique.
- Ajout d'un sélecteur de police dans les paramètres d'accessibilité pour améliorer la lisibilité.
- Support étendu des formats vidéo/audio pour les résumés.
- Possibilité de configurer l'accès et le niveau de configuration des salles via l'API externe [#1260].
- Possibilité de définir si tous les participants peuvent couper le son des autres.
- Ajout d'un administrateur spécifique pour la gestion des fichiers.

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité (idna, urllib3, aiohttp, core-js, webpack-dev-server, django).
- Refactorisation du code frontend pour améliorer le code splitting et réduire la taille des bundles JavaScript.
- Utilisation de `uv` pour la gestion des dépendances dans les agents.
- Amélioration de la robustesse du processus de suppression de fichiers côté backend.
- Amélioration de la synchronisation de la configuration des salles.
- Utilisation de variables d'environnement plus cohérentes pour la configuration backend.
- Suppression de dépendances inutiles côté frontend.
- Amélioration de la gestion des erreurs et des conditions de concurrence.
- Ajout de tests pour certaines fonctionnalités.

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements d'API.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Amélioration des logs pour faciliter le débogage.
- Correction de problèmes de positionnement de l'interface utilisateur.
- Correction de problèmes de compatibilité avec certains navigateurs.
- Mise à jour des chartes Helm.
- Amélioration de la configuration de l'environnement de développement.
- Correction de liens dans les emails de notification.
- Amélioration de la gestion des erreurs dans les tests.
- Suppression de configurations inutiles.
- Correction de problèmes de build.
