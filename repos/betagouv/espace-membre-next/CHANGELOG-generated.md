## Changelog : espace-membre-next (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'expérience de gestion des membres, notamment en introduisant une checklist de départ et en affichant des informations sur l'expiration des comptes. Des améliorations ont également été apportées aux logs et à la gestion des outils tiers.

### Évolutions fonctionnelles
- Les agents des startups peuvent désormais modifier les informations des membres [#1303](https://github.com/betagouv/espace-membre-next/issues/1303).
- Une nouvelle checklist de départ a été ajoutée pour faciliter la transition lors du départ d'un membre [#1231](https://github.com/betagouv/espace-membre-next/issues/1231).
- Un panneau d'offboarding s'affiche désormais sur le tableau de bord lorsque l'expiration d'un compte approche [#1289](https://github.com/betagouv/espace-membre-next/issues/1289).
- Les membres expirés sont automatiquement retirés des équipes [#1277](https://github.com/betagouv/espace-membre-next/issues/1277).
- Amélioration du mail de composition d'équipe avec des instructions de départ [#1290](https://github.com/betagouv/espace-membre-next/issues/1290).
- Clarification des titres de la checklist de départ [#1262](https://github.com/betagouv/espace-membre-next/issues/1262).
- Amélioration de la progression de l'onboarding [#1264](https://github.com/betagouv/espace-membre-next/issues/1264).
- L'étape d'onboarding est masquée sur le tableau de bord une fois terminée [#1266](https://github.com/betagouv/espace-membre-next/issues/1266).
- Ajout d'une option pour ne pas créer d'email pour les attributaires lors de l'onboarding [#1305](https://github.com/betagouv/espace-membre-next/issues/1305).

### Évolutions techniques
- Ajout de tests E2E pour le tableau de bord et l'onboarding/offboarding [#1299](https://github.com/betagouv/espace-membre-next/issues/1299).
- Suppression de l'utilisation d'OVH et migration vers n8n pour la gestion de GitHub [#1275](https://github.com/betagouv/espace-membre-next/issues/1275), [#1274](https://github.com/betagouv/espace-membre-next/issues/1274), [#1276](https://github.com/betagouv/espace-membre-next/issues/1276).
- Suppression de composants inutilisés : newsletter, pad, mattermost [#1253](https://github.com/betagouv/espace-membre-next/issues/1253).
- Amélioration de la gestion des logs pour réduire le bruit et améliorer la lisibilité [#1302](https://github.com/betagouv/espace-membre-next/issues/1302), [#1300](https://github.com/betagouv/espace-membre-next/issues/1300), [#1256](https://github.com/betagouv/espace-membre-next/issues/1256), [#1255](https://github.com/betagouv/espace-membre-next/issues/1255), [#1254](https://github.com/betagouv/espace-membre-next/issues/1254).
- Correction de la politique de sécurité du contenu (CSP) pour inclure l'URL de la FAQ Crisp [#1243](https://github.com/betagouv/espace-membre-next/issues/1243).

### Autres changements
- Correction pour utiliser d'autres emails d'utilisateurs ProConnect [#1240](https://github.com/betagouv/espace-membre-next/issues/1240).
- Correction pour lier correctement les informations des utilisateurs Mattermost [#1239](https://github.com/betagouv/espace-membre-next/issues/1239).
- Correction pour ne pas vérifier les informations OVH [#1272](https://github.com/betagouv/espace-membre-next/issues/1272).
- Suppression d'une entrée de menu admin inutile [#1265](https://github.com/betagouv/espace-membre-next/issues/1265).
- Ajout de motifs d'exclusion d'URL pour Matomo [#1273](https://github.com/betagouv/espace-membre-next/issues/1273).
