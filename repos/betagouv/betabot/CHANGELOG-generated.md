## Changelog : betabot (30 derniers jours, au 23 juin 2026)

### Résumé
Ce mois-ci, Betabot a bénéficié d'améliorations significatives concernant la détection d'entités, l'intégration de nouvelles sources de documentation (DSFR, FranceConnect, Proconnect, ruche_numerique), et la gestion des conversations via Matrix (threads). Des corrections de bugs et des optimisations de performance ont également été apportées pour améliorer la stabilité et la réactivité du bot.

### Évolutions fonctionnelles
- Ajout de la détection initiale d'entités pour améliorer la compréhension des requêtes.
- Intégration de la documentation DSFR, FranceConnect et Proconnect pour enrichir les réponses du bot.
- Ajout d'une commande curl pour récupérer le flux vidéo de ruche_numerique.
- Réactivation des threads dans Matrix pour une meilleure organisation des conversations [#2](https://github.com/betagouv/betabot/issues/2).
- Ajout d'un calendrier public mis à jour.
- Ajout d'un contexte temporel pour améliorer la pertinence des réponses.
- Ajout de changelogs pour les startups.
- Ajout d'une base de données SQLite pour les requêtes d'agrégation.
- Ajout de l'incubateur à la base de données.
- Ajout du champ `created_at` à la base de données.

### Évolutions techniques
- Mise à jour de Next.js.
- Amélioration de la gestion des embeddings (calcul uniquement lorsque nécessaire, mise en cache).
- Correction de problèmes liés à Docker (plusieurs commits).
- Ajout de tests d'évaluation pour le routage des outils.
- Ajout de tests de détection d'entités.
- Correction de bugs liés à l'utilisation des threads dans Matrix (correction d'un bug empêchant l'utilisation des threads en conversation privée).
- Correction d'une erreur lors du traitement de textes longs pour les embeddings.
- Amélioration des schémas de la base de données.
- Ajout d'instructions pour l'utilisation du bot.

### Autres changements
- Mise à jour de la documentation et des spécifications des données.
- Corrections de liens et d'URLs dans la documentation.
- Nettoyage du code.
- Passage à Node.js 24.
- Ajout de timeout pour améliorer la robustesse.
