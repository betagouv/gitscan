## Changelog : espace-membre-next (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur la simplification de l'application, la suppression de fonctionnalités obsolètes ou peu utilisées, et l'amélioration de l'expérience utilisateur notamment au niveau de l'onboarding et du tableau de bord. Des corrections ont également été apportées pour affiner le comportement de certaines fonctionnalités existantes.

### Évolutions fonctionnelles
- Les agents des startups peuvent désormais modifier les informations des membres. [#1303](https://github.com/betagouv/espace-membre-next/issues/1303)
- Un panneau d'offboarding s'affiche sur le tableau de bord lorsque l'expiration d'un membre approche. [#1289](https://github.com/betagouv/espace-membre-next/issues/1289)
- Les membres expirés sont automatiquement retirés des équipes. [#1277](https://github.com/betagouv/espace-membre-next/issues/1277)
- Amélioration du mail envoyé lors du départ d'un membre avec des instructions claires. [#1290](https://github.com/betagouv/espace-membre-next/issues/1290)
- Amélioration de la progression de l'onboarding. [#1264](https://github.com/betagouv/espace-membre-next/issues/1264)
- L'étape d'onboarding n'est plus affichée sur le tableau de bord une fois complétée. [#1266](https://github.com/betagouv/espace-membre-next/issues/1266)
- Clarification des titres de la checklist d'offboarding. [#1262](https://github.com/betagouv/espace-membre-next/issues/1262)
- Suppression de la création d'email pour les attributaires lors de l'onboarding. [#1305](https://github.com/betagouv/espace-membre-next/issues/1305)

### Évolutions techniques
- Simplification du routage et utilisation accrue du rendu côté serveur (SSR). [#1326](https://github.com/betagouv/espace-membre-next/issues/1326)
- Ajout de tests E2E pour le tableau de bord et le processus d'onboarding/offboarding. [#1299](https://github.com/betagouv/espace-membre-next/issues/1299)
- Amélioration de la journalisation (logging) de l'application. [#1302](https://github.com/betagouv/espace-membre-next/issues/1302) et [#1300](https://github.com/betagouv/espace-membre-next/issues/1300)

### Autres changements
- Suppression de variables d'environnement inutiles. [#1329](https://github.com/betagouv/espace-membre-next/issues/1329)
- Suppression des éléments liés à Mattermost. [#1325](https://github.com/betagouv/espace-membre-next/issues/1325)
- Suppression de la gestion des comptes Matomo et Sentry. [#1322](https://github.com/betagouv/espace-membre-next/issues/1322)
- Suppression des services OVH et de la gestion GitHub (remplacée par n8n). [#1275](https://github.com/betagouv/espace-membre-next/issues/1275) et [#1274](https://github.com/betagouv/espace-membre-next/issues/1274)
- Suppression de l'ordonnanceur de fin de contrat utilisateur (n8n). [#1276](https://github.com/betagouv/espace-membre-next/issues/1276)
- Suppression des fonctionnalités newsletter, pad et Mattermost. [#1253](https://github.com/betagouv/espace-membre-next/issues/1253)
- Suppression d'une entrée de menu admin. [#1265](https://github.com/betagouv/espace-membre-next/issues/1265)
- Correction pour ne plus vérifier les informations OVH. [#1272](https://github.com/betagouv/espace-membre-next/issues/1272)
- Ajout de motifs d'exclusion pour Matomo. [#1273](https://github.com/betagouv/espace-membre-next/issues/1273)
- Suppression de l'export de l'adresse email secondaire. [#1327](https://github.com/betagouv/espace-membre-next/issues/1327)
