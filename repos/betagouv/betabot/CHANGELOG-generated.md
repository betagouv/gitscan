## Changelog : betabot (30 derniers jours, au 8 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives à Betabot, notamment l'ajout de nouvelles sources de données (offres d'emploi de choisirleservicepublic, documentation Tchap) et des fonctionnalités (outil de feedback). Des corrections ont également été apportées pour améliorer la précision des réponses et la gestion du calendrier.

### Évolutions fonctionnelles
- Ajout de la recherche d'offres d'emploi de [choisirleservicepublic](https://github.com/betagouv/betabot/pull/8).
- Ajout de la documentation Tchap aux sources de recherche [#4](https://github.com/betagouv/betabot/issues/4).
- Amélioration de la recherche pour inclure la documentation Tchap.
- Ajout d'un outil de feedback [#6](https://github.com/betagouv/betabot/issues/6).
- Correction de l'affichage du calendrier, qui utilise maintenant l'heure de Paris [#7](https://github.com/betagouv/betabot/issues/7).

### Évolutions techniques
- Mise à jour de Next.js.
- Mise en cache des embeddings pour améliorer les performances.
- Utilisation du nouveau calendrier public.
- Ajout de timeouts pour améliorer la robustesse.
- Correction de la configuration du Dockerfile.
- Ajout de contexte temporel pour améliorer la pertinence des réponses.

### Autres changements
- Corrections diverses et améliorations de la stabilité (plusieurs commits de correction).
- Ajout de tests d'évaluation (evals) [#3](https://github.com/betagouv/betabot/issues/3).
- Correction d'un fichier manquant.
- Ajout de la documentation messagerie [#2](https://github.com/betagouv/betabot/issues/2).
