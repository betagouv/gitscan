## Changelog : hub (30 derniers jours, au 4 juin 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur le développement de la fonctionnalité de chat, en mettant en place l'interface utilisateur, les fonctionnalités de base comme l'envoi de messages, les réactions, les threads et la gestion de plusieurs comptes. Des améliorations ont également été apportées à l'infrastructure et aux outils de développement.

### Évolutions fonctionnelles
- **Chat :** Ajout d'une interface utilisateur complète pour le chat, incluant la composition de messages, l'affichage des conversations, la gestion des threads et des réactions avec emojis. [#1234 (lien fictif)]
- **Chat multi-comptes :** Possibilité de gérer et d'afficher plusieurs comptes dans l'interface de chat.
- **Documents :** Ajout d'un panneau "Documents" permettant de visualiser des fichiers (PDF, images, vidéos, audio).
- **Notifications :** Implémentation de notifications toast pour informer l'utilisateur des événements importants (par exemple, échec d'envoi de message).
- **Comptes :** Ajout d'un sélecteur de comptes pour basculer entre différents utilisateurs.

### Évolutions techniques
- **Frontend :** Refonte complète du frontend avec Next.js et TypeScript, remplacement de l'ancien codebase.
- **Tests E2E :** Mise à jour et refactorisation des tests end-to-end (Playwright) pour couvrir les nouvelles fonctionnalités.
- **Infrastructure :** Consolidation de la configuration Docker Compose et de la base de données utilisée pour les tests E2E.
- **CI/CD :** Mise à jour des workflows CI/CD pour intégrer le nouveau frontend et les tests E2E.
- **Architecture :** Introduction d'une architecture basée sur des "drivers" pour faciliter l'intégration de différents services de chat (Matrix, etc.).
- **I18n :** Mise à jour de la configuration d'internationalisation et des dépendances.

### Autres changements
- **Documentation :** Ajout de documentation sur l'architecture multi-comptes du chat.
- **Architecture Decision Records:** Introduction de l'utilisation d'Architecture Decision Records pour documenter les choix d'architecture.
- **Linting & Formatting:** Configuration de Prettier pour le formatage du code et réactivation du linting lors de la construction du projet.
- **Nettoyage de code :** Suppression de code legacy et de dépendances inutilisées.
- **Configuration :** Ajustement de la configuration Nginx pour le bon fonctionnement des assets statiques.
