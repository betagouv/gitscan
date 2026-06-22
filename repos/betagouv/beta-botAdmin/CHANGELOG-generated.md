## Changelog : beta-botAdmin (30 derniers jours, au 19 juin 2026)

### Résumé
Ce changelog couvre les premières étapes de développement du bot beta-botAdmin. Les modifications récentes se concentrent sur l'ajout de commandes de base, la correction de bugs initiaux et la mise en place d'une infrastructure de CI/CD pour faciliter le développement futur. L'objectif est de fournir un outil fonctionnel pour la gestion des opérations au sein de la communauté beta.gouv.fr.

### Évolutions fonctionnelles
- Ajout de la commande `/help` pour la demande OPS.
- Amélioration de la commande `/espace`.
- Ajout de la possibilité de créer des rooms directement depuis n8n.
- Correction d'un bug empêchant le bot d'être administrateur dans les rooms créés via la commande self. [#3](https://github.com/betagouv/beta-botAdmin/issues/3)
- Ajout de la gestion des noms de domaine : `@beta.gouv.fr`, `@numerique.gouv.fr` et `@modernisation.gouv.fr`.
- Ajout d'ID pour la création de demandes.

### Évolutions techniques
- Mise en place d'une première intégration de CI/CD. [#1](https://github.com/betagouv/beta-botAdmin/issues/1)
- Modifications et tests pour l'intégration avec une partie LLM (Large Language Model).
- Amélioration de la gestion des messages directs depuis n8n.

### Autres changements
- Modifications diverses pour le bon fonctionnement du bot et des tests.
- Ajout de tests initiaux.
- Premiers commits et push du code source.
