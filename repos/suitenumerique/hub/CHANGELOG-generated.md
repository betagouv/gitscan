## Changelog : hub (30 derniers jours, au 10 juillet 2026)

### Résumé
Ce mois-ci, le projet Hub a connu une avancée significative dans l'intégration de la messagerie Matrix. Les utilisateurs peuvent désormais initier des conversations Matrix, envoyer et recevoir des messages en temps réel, gérer les invitations et réagir aux messages. L'interface utilisateur a été enrichie avec des indicateurs de lecture, des favoris et des threads de conversation.

### Évolutions fonctionnelles
- Intégration de la messagerie Matrix : possibilité de démarrer de nouvelles conversations Matrix directement depuis la recherche de chat. [#2345](https://github.com/suitenumerique/hub/issues/2345)
- Envoi et réception de messages Matrix en temps réel.
- Gestion des invitations Matrix : acceptation et refus des invitations.
- Ajout de réactions aux messages dans les conversations et les threads Matrix.
- Affichage des indicateurs de lecture et des accusés de réception pour les messages Matrix.
- Gestion des threads de conversation Matrix : lecture, réponse et création de threads.
- Possibilité d'ajouter des conversations aux favoris.
- Affichage des membres de la conversation.
- Indicateurs de saisie (typing indicators) pour une meilleure expérience utilisateur.
- Coloration des messages de l'utilisateur courant avec la couleur de la marque.

### Évolutions techniques
- Refonte de la couche de mapping du driver Matrix pour une meilleure modularité.
- Lazy loading du client SDK Matrix pour optimiser les performances.
- Configuration de l'authentification OIDC Matrix avec Keycloak.
- Utilisation d'un stack Docker local pour le développement avec Matrix et Keycloak.
- Optimisation du déduplication des guards du driver Matrix et du hachage des avatars.
- Simplification de l'auto-défilement des conversations.

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités.
- Ajustement de la mise en forme du changelog pour une meilleure lisibilité.
