## Changelog : infra-apps (30 derniers jours)

### Résumé
Ce changelog résume les modifications apportées à l'infrastructure au cours des 30 derniers jours. Les principales évolutions concernent l'ajout et la configuration de l'application Charon pour différents environnements (proconnect, egapro, srdt), ainsi que des ajustements et corrections concernant l'instance Metabase, notamment pour l'environnement SRDT et la synchronisation avec Matomo.

### Évolutions fonctionnelles
- Ajout de l'application Charon pour l'environnement proconnecttest SRDT (#36).
- Ajout de l'application Charon pour les environnements proconnect et egapro (#33, #32).
- Synchronisation Matomo ajoutée pour Metabase SRDT (#34, #35).
- Ajout de l'instance Metabase pour SRDT (#296f963).
- Correction d'un problème de rafraîchissement de vue dans Metabase CDTN (#72c4a57, #554f840, #90caac4).

### Évolutions techniques
- Augmentation de la taille du disque pour l'instance Metabase afin d'améliorer sa performance et sa stabilité (#875928f, #588d540).
- Autorisation de l'accès de Metabase SRDT à l'espace de noms SRDT (#f07c6fb).
- Ajout du secret `matomo-key` à Metabase SRDT pour la synchronisation avec Matomo (#0b9ce16).
- Correction du secret Metabase SRDT (#b1fec1e).
- Mise à jour de la version de l'image Charon (#7aff9fe).
- Amélioration de Greenmask (#c926944).
