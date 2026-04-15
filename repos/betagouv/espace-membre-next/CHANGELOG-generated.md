## Changelog : espace-membre-next (30 derniers jours, au 15 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion du cycle de vie des membres, notamment l'onboarding et l'offboarding, ainsi que sur des corrections de bugs et des optimisations de la plateforme. Des fonctionnalités ont été ajoutées pour faciliter la gestion des membres par les agents des startups et améliorer l'expérience utilisateur globale.

### Évolutions fonctionnelles
- Les agents des startups peuvent désormais modifier les informations des membres. [#1303](https://github.com/betagouv/espace-membre-next/issues/1303)
- Un panneau d'offboarding s'affiche dans le tableau de bord lorsqu'un membre arrive à expiration. [#1289](https://github.com/betagouv/espace-membre-next/issues/1289)
- Les membres expirés sont automatiquement retirés des équipes. [#1277](https://github.com/betagouv/espace-membre-next/issues/1277)
- Une checklist d'offboarding a été ajoutée pour faciliter le processus de départ des membres. [#1231](https://github.com/betagouv/espace-membre-next/issues/1231)
- Amélioration des instructions de départ dans l'email de composition d'équipe. [#1290](https://github.com/betagouv/espace-membre-next/issues/1290)
- Clarification des titres dans la checklist d'offboarding. [#1262](https://github.com/betagouv/espace-membre-next/issues/1262)
- Amélioration de la progression de l'onboarding. [#1264](https://github.com/betagouv/espace-membre-next/issues/1264)
- L'étape d'onboarding est masquée du tableau de bord une fois complétée. [#1266](https://github.com/betagouv/espace-membre-next/issues/1266)

### Évolutions techniques
- Ajout de tests E2E pour le tableau de bord et les processus d'onboarding/offboarding. [#1299](https://github.com/betagouv/espace-membre-next/issues/1299)
- Suppression de l'ancien système de planification de fin de contrat utilisateur (n8n). [#1276](https://github.com/betagouv/espace-membre-next/issues/1276)
- Suppression de la gestion GitHub, remplacée par n8n. [#1274](https://github.com/betagouv/espace-membre-next/issues/1274)
- Suppression des services OVH. [#1275](https://github.com/betagouv/espace-membre-next/issues/1275)
- Suppression des intégrations newsletter, Pad et Mattermost. [#1253](https://github.com/betagouv/espace-membre-next/issues/1253)
- Amélioration de la gestion des logs pour réduire le bruit. [#1302](https://github.com/betagouv/espace-membre-next/issues/1302), [#1300](https://github.com/betagouv/espace-membre-next/issues/1300), [#1256](https://github.com/betagouv/espace-membre-next/issues/1256), [#1255](https://github.com/betagouv/espace-membre-next/issues/1255), [#1254](https://github.com/betagouv/espace-membre-next/issues/1254)

### Autres changements
- Ajout d'une exception pour les URLs de la FAQ Crisp dans la politique de sécurité du contenu (CSP). [#1243](https://github.com/betagouv/espace-membre-next/issues/1243)
- Correction pour utiliser les autres adresses email des utilisateurs ProConnect. [#1240](https://github.com/betagouv/espace-membre-next/issues/1240)
- Correction de l'affichage du statut et de l'employeur des membres. [#1241](https://github.com/betagouv/espace-membre-next/issues/1241)
- Correction pour lier correctement les informations utilisateur Mattermost. [#1239](https://github.com/betagouv/espace-membre-next/issues/1239)
- Suppression d'une entrée de menu admin inutile. [#1265](https://github.com/betagouv/espace-membre-next/issues/1265)
- Correction pour ne plus vérifier les informations OVH. [#1272](https://github.com/betagouv/espace-membre-next/issues/1272)
- Ajout de motifs d'exclusion pour Matomo. [#1273](https://github.com/betagouv/espace-membre-next/issues/1273)
