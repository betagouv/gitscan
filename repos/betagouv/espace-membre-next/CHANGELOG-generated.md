## Changelog : espace-membre-next (30 derniers jours, au 22 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience de gestion des membres, notamment au niveau de l'onboarding et de l'offboarding. Des corrections ont été apportées pour simplifier les processus et améliorer la clarté des informations. Des outils et services tiers ont été revus et simplifiés.

### Évolutions fonctionnelles
- Les agents des startups peuvent désormais modifier les informations des membres. [#1303](https://github.com/betagouv/espace-membre-next/issues/1303)
- Une section d'offboarding est maintenant affichée sur le tableau de bord lorsqu'un membre arrive à expiration. [#1289](https://github.com/betagouv/espace-membre-next/issues/1289)
- Les membres expirés sont automatiquement retirés des équipes. [#1277](https://github.com/betagouv/espace-membre-next/issues/1277)
- Une checklist d'offboarding a été ajoutée pour faciliter le processus de départ. [#1231](https://github.com/betagouv/espace-membre-next/issues/1231)
- Amélioration du mail de composition d'équipe avec des instructions de départ. [#1290](https://github.com/betagouv/espace-membre-next/issues/1290)
- Clarification des titres de la checklist de départ. [#1262](https://github.com/betagouv/espace-membre-next/issues/1262)
- Amélioration de la progression de l'onboarding. [#1264](https://github.com/betagouv/espace-membre-next/issues/1264)
- L'étape d'onboarding ne crée plus d'email pour les attributaires. [#1305](https://github.com/betagouv/espace-membre-next/issues/1305)
- L'onboarding est masqué du tableau de bord une fois terminé. [#1266](https://github.com/betagouv/espace-membre-next/issues/1266)

### Évolutions techniques
- Ajout de tests E2E pour le tableau de bord et les processus d'onboarding/offboarding. [#1299](https://github.com/betagouv/espace-membre-next/issues/1299)
- Amélioration de la journalisation (logging) pour faciliter le débogage. [#1300](https://github.com/betagouv/espace-membre-next/issues/1300) et [#1302](https://github.com/betagouv/espace-membre-next/issues/1302)
- Suppression de la gestion GitHub, remplacée par n8n. [#1274](https://github.com/betagouv/espace-membre-next/issues/1274)
- Suppression de l'utilisation d'OVH. [#1275](https://github.com/betagouv/espace-membre-next/issues/1275)
- Suppression du scheduler de fin de contrat utilisateur (n8n). [#1276](https://github.com/betagouv/espace-membre-next/issues/1276)
- Suppression de Matomo et Sentry. [#1322](https://github.com/betagouv/espace-membre-next/issues/1322)
- Suppression des outils newsletter, pad et mattermost. [#1253](https://github.com/betagouv/espace-membre-next/issues/1253)

### Autres changements
- Correction de la configuration de Matomo pour exclure certaines URLs. [#1273](https://github.com/betagouv/espace-membre-next/issues/1273)
- Correction pour ne plus vérifier les informations OVH. [#1272](https://github.com/betagouv/espace-membre-next/issues/1272)
- Suppression d'une entrée de menu admin inutile. [#1265](https://github.com/betagouv/espace-membre-next/issues/1265)
- Mise à jour du mail de rappel de départ. [#1260](https://github.com/betagouv/espace-membre-next/issues/1260)
