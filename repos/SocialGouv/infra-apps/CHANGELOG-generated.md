## Changelog : infra-apps (30 derniers jours)

### Résumé
Ce changelog résume les modifications apportées à l'infrastructure d'applications au cours du dernier mois. Les mises à jour concernent principalement l'application Metabase, avec des corrections de rafraîchissement de vues et d'augmentation de la taille du disque. Des modifications ont également été apportées pour intégrer et configurer l'application Charon pour différents environnements (proconnect, srdt).

### Évolutions fonctionnelles
- Ajout de la configuration Charon pour l'environnement proconnecttest pour srdt (#36).
- Intégration de l'application Charon pour l'environnement proconnect (#33, #32).
- Mise à jour de la version de l'image Charon (#35, #34).
- Accès de Metabase (srdt) à l'espace de noms srdt autorisé (#f07c6fb).
- Ajout du secret `matomo-key` à Metabase (srdt) (#0b9ce16).
- Correction du rafraîchissement des vues dans Metabase (cdtn) (#72c4a57, #554f840).
- Correction d'un problème de rafraîchissement concurrent des vues dans Metabase (cdtn) (#427dfb5).

### Évolutions techniques
- Augmentation de la taille du disque alloué à Metabase (#875928f, #588d540).
- Correction d'un problème et restauration d'une configuration précédente pour Metabase (cdtn) (#90caac4).

### Autres changements
- Nettoyage du code (#c854179).
- Mise à jour de l'application Greenmask (#c926944).
