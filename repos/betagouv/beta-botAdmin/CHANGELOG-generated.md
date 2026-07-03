## Changelog : beta-botAdmin (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, le bot a bénéficié d'une série d'améliorations axées sur la gestion des espaces, des demandes OPS et l'intégration avec d'autres outils comme n8n. Des corrections ont également été apportées pour assurer le bon fonctionnement du bot lors de la création d'espaces et pour la gestion des permissions.

### Évolutions fonctionnelles
- Ajout d'une commande `/help` pour les demandes OPS.
- Amélioration de la commande `/espace` pour une meilleure gestion des espaces.
- Correction d'un bug qui empêchait le bot de conserver son rôle d'administrateur lors de la création d'espaces via la commande auto-hébergée. [#3](https://github.com/betagouv/beta-botAdmin/pull/3)
- Possibilité de recevoir des messages directement depuis n8n.
- Ajout de la gestion des noms de domaine suivants : `@beta.gouv.fr`, `@numerique.gouv.fr` et `@modernisation.gouv.fr`. [#9](https://github.com/betagouv/beta-botAdmin/pull/9)
- Ajout d'identifiants pour la création d'éléments. [#5](https://github.com/betagouv/beta-botAdmin/pull/5)

### Évolutions techniques
- Mise en place d'une intégration continue (CI) pour automatiser les tests et le déploiement. [#1](https://github.com/betagouv/beta-botAdmin/pull/1)
- Modifications pour faciliter l'intégration avec la CI. [#6](https://github.com/betagouv/beta-botAdmin/pull/6)
- Suppression de la partie liée à un modèle de langage (LLM). [#10](https://github.com/betagouv/beta-botAdmin/pull/10)
- Modifications diverses pour améliorer la clarté du code et faciliter la maintenance.

### Autres changements
- Corrections mineures et tests.
- Modifications pour colifi. [#2](https://github.com/betagouv/beta-botAdmin/pull/2)
- Ajustements pour la compatibilité avec les messages directs. [#7](https://github.com/betagouv/beta-botAdmin/pull/7)
