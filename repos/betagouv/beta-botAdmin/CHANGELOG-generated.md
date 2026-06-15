## Changelog : beta-botAdmin (30 derniers jours, au 12 juin 2026)

### Résumé
Ce changelog présente les premières évolutions du bot beta-botAdmin. Les modifications se concentrent sur l'amélioration de la gestion des salles, l'intégration avec des outils externes comme n8n et la configuration initiale de la CI/CD. Des ajustements ont également été apportés pour supporter différents domaines d'email et la partie LLM.

### Évolutions fonctionnelles
- Correction : Le bot admin est maintenant correctement maintenu dans les salles créées via la commande d'auto-gestion. [#3](https://github.com/betagouv/beta-botAdmin/pull/3)
- Amélioration : Prise en charge des messages directs depuis n8n, permettant une intégration plus fluide avec cet outil d'automatisation.
- Amélioration : Ajout de la prise en charge des modifications de nom de domaine : `@beta.gouv.fr`, `@numerique.gouv.fr`, `@modernisation.gouv.fr`. [#2](https://github.com/betagouv/beta-botAdmin/pull/2)
- Amélioration : Ajustements de la partie LLM (Large Language Model). [#1](https://github.com/betagouv/beta-botAdmin/pull/1)

### Évolutions techniques
- CI/CD : Mise en place d'une première chaîne d'intégration continue (CI) pour automatiser les tests et la construction du projet. [#1](https://github.com/betagouv/beta-botAdmin/pull/1)
- Initialisation : Premier push du code source et configuration initiale du dépôt.

### Autres changements
- Tests : Modifications et ajustements des tests unitaires.
- Configuration : Diverses modifications de configuration pour assurer le bon fonctionnement du bot.
