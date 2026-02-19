## Changelog : espace-membre-next (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à l'espace membre au cours des 30 derniers jours. Les modifications se concentrent principalement sur la gestion des emails, l'onboarding des nouveaux membres et la synchronisation des données avec les services externes. Plusieurs corrections de bugs ont également été implémentées pour améliorer l'expérience utilisateur.

### Évolutions fonctionnelles
- Amélioration de l'onboarding pour les utilisateurs venant d'OVH, intégrant la suite numérique. (#1192)
- Affichage des instructions de création d'email simplifié. (#1223)
- L'onboarding est maintenant affiché pour tous les membres, y compris les anciens. (#1218)
- Correction de l'affichage de l'état de l'email principal pour les membres. (#1190)
- Ajout de la prise en charge des emails `francetravail.fr` et `justice.fr` pour les emails publics. (#1184)
- Correction de l'affichage des invitations dimail. (#1215, #1214)
- Correction d'un bug empêchant l'affichage correct des invitations dimail pour les emails supprimés. (#1216)
- Masquage de l'onboarding sur le tableau de bord pour les anciens membres. (#1222)

### Évolutions techniques
- Utilisation d'UUID au lieu du nom d'utilisateur pour les emails dimail. (#1199)
- Ajout d'un script npm `sync-dimail` pour synchroniser les données dimail. (#1186)
- Synchronisation de la table `dinum_emails`. (#1168)
- Réduction de la limite de tentatives de `pgboos`. (#1191)
- Correction du format du cron. (#1213)
- Mise à jour de l'URL du webmail pour `EMAIL_PLAN_OPI`. (#1200)
- Correction pour éviter de modifier les comptes dimail existants lors de la recréation des utilisateurs. (#1189)
- Correction de la page `AccountVerifyClientPage`. (#1219)

### Autres changements
- Ajout d'un diagramme de flux pour la documentation. (#1211)
- Mise à jour du fichier `checklist.yml`. (#1221)
