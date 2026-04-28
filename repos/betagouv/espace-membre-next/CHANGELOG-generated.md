## Changelog : espace-membre-next (30 derniers jours, au 27 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la simplification de l'infrastructure, l'amélioration de l'expérience utilisateur pour les startups et les administrateurs, et la correction de plusieurs bugs. Des tests E2E ont été ajoutés pour renforcer la qualité de l'application.

### Évolutions fonctionnelles
- Les agents des startups peuvent désormais modifier les informations des membres. [#1303](https://github.com/betagouv/espace-membre-next/issues/1303)
- Un panneau d'offboarding s'affiche sur le tableau de bord lorsqu'un membre arrive à expiration. [#1289](https://github.com/betagouv/espace-membre-next/issues/1289)
- Les membres expirés sont automatiquement retirés des équipes. [#1277](https://github.com/betagouv/espace-membre-next/issues/1277)
- Amélioration de l'email envoyé lors d'un départ d'équipe, avec des instructions claires. [#1290](https://github.com/betagouv/espace-membre-next/issues/1290)
- Suppression de la création d'email pour les attributaires lors de l'onboarding. [#1305](https://github.com/betagouv/espace-membre-next/issues/1305)
- L'étape d'onboarding est masquée sur le tableau de bord une fois complétée. [#1266](https://github.com/betagouv/espace-membre-next/issues/1266)

### Évolutions techniques
- Simplification du routage et utilisation accrue du rendu côté serveur (SSR). [#1326](https://github.com/betagouv/espace-membre-next/issues/1326)
- Suppression de l'utilisation de variables d'environnement inutiles et du fichier `.dotenv`. [#1339](https://github.com/betagouv/espace-membre-next/issues/1339)
- Suppression des composants liés à Mattermost. [#1325](https://github.com/betagouv/espace-membre-next/issues/1325)
- Suppression des services OVH et de la gestion GitHub, remplacés par n8n. [#1275](https://github.com/betagouv/espace-membre-next/issues/1275) [#1274](https://github.com/betagouv/espace-membre-next/issues/1274) [#1276](https://github.com/betagouv/espace-membre-next/issues/1276)
- Amélioration de la journalisation (logging) de l'application. [#1302](https://github.com/betagouv/espace-membre-next/issues/1302) [#1300](https://github.com/betagouv/espace-membre-next/issues/1300)
- Ajout de tests E2E pour le tableau de bord et le processus d'onboarding/offboarding. [#1299](https://github.com/betagouv/espace-membre-next/issues/1299)
- Correction d'un problème lié à l'exportation de l'adresse email secondaire. [#1327](https://github.com/betagouv/espace-membre-next/issues/1327)
- Correction d'un problème lié à la vérification des informations OVH. [#1272](https://github.com/betagouv/espace-membre-next/issues/1272)
- Correction d'un problème d'affichage d'une entrée de menu admin. [#1265](https://github.com/betagouv/espace-membre-next/issues/1265)
- Ajout de motifs d'exclusion pour Matomo. [#1273](https://github.com/betagouv/espace-membre-next/issues/1273)

### Autres changements
- Suppression de la suppression des comptes Matomo et Sentry. [#1322](https://github.com/betagouv/espace-membre-next/issues/1322)
- Diverses mises à jour de dépendances. [#1331](https://github.com/betagouv/espace-membre-next/issues/1331)
