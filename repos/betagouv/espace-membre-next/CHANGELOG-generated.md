## Changelog : espace-membre-next (30 derniers jours)

### Résumé
Les dernières mises à jour de l'espace membre se concentrent sur l'amélioration de l'expérience d'onboarding des nouveaux utilisateurs, en particulier pour ceux venant d'OVH. Des corrections ont également été apportées pour gérer correctement les invitations par email (dimail) et l'affichage des informations pour les membres existants. Enfin, la documentation a été enrichie avec un diagramme de flux pour clarifier le processus.

### Évolutions fonctionnelles
- Amélioration de l'onboarding pour les utilisateurs de la suite numérique OVH (#1192)
- Correction de l'affichage de l'onboarding pour les membres existants (#1218)
- Correction de l'affichage des invitations par email (dimail) pour les membres dont l'adresse email a été supprimée (#1214, #1215, #1216)
- Simplification des instructions de création d'email (#1223)
- Masquage de l'onboarding sur le tableau de bord pour les anciens membres (#1222)

### Évolutions techniques
- Utilisation d'UUID au lieu du nom d'utilisateur pour les invitations par email (dimail) (#1199)
- Correction du format de cron (#1213)
- Mise à jour de l'URL du webmail pour le plan EMAIL_OPI (#1200)

### Autres changements
- Ajout d'un diagramme de flux à la documentation (#1211)
- Mise à jour du fichier checklist.yml (#1221)
- Correction de la page AccountVerifyClientPage (#1219)
