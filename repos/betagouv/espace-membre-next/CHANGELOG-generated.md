## Changelog : espace-membre-next (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur et la gestion des startups. Des correctifs ont été apportés pour améliorer la robustesse de l'application, notamment concernant la création d'emails et la gestion des variables d'environnement. De nouvelles fonctionnalités permettent aux agents des startups de modifier les membres et affichent un panneau de désinscription pour les membres dont l'accès expire bientôt.

### Évolutions fonctionnelles
- Ajout d'une recherche par startup dans l'interface de recherche. [#1324](https://github.com/betagouv/espace-membre-next/issues/1324)
- Les agents des startups peuvent désormais modifier les informations des membres. [#1303](https://github.com/betagouv/espace-membre-next/issues/1303)
- Un panneau de désinscription s'affiche pour les membres dont l'accès est sur le point d'expirer. [#1289](https://github.com/betagouv/espace-membre-next/issues/1289)
- Amélioration de l'email envoyé lors des changements de composition d'équipe, avec des instructions de départ. [#1290](https://github.com/betagouv/espace-membre-next/issues/1290)
- Suppression de la création d'email pour les attributaires lors de l'onboarding. [#1305](https://github.com/betagouv/espace-membre-next/issues/1305)

### Évolutions techniques
- Simplification du routage et utilisation accrue du rendu côté serveur (SSR). [#1326](https://github.com/betagouv/espace-membre-next/issues/1326)
- Correction de problèmes liés à l'exportation de l'email secondaire. [#1327](https://github.com/betagouv/espace-membre-next/issues/1327)
- Correction de problèmes liés à l'environnement de production (ESM). [#1337](https://github.com/betagouv/espace-membre-next/issues/1337)
- Suppression des variables d'environnement inutiles. [#1329](https://github.com/betagouv/espace-membre-next/issues/1329)
- Suppression des éléments liés à Mattermost. [#1325](https://github.com/betagouv/espace-membre-next/issues/1325)
- Suppression des fonctionnalités de suppression de compte Matomo/Sentry. [#1322](https://github.com/betagouv/espace-membre-next/issues/1322)
- Amélioration de la journalisation (logging). [#1300](https://github.com/betagouv/espace-membre-next/issues/1300) et [#1302](https://github.com/betagouv/espace-membre-next/issues/1302)
- Correction de la création d'email lorsque aucun email principal n'est défini. [#1342](https://github.com/betagouv/espace-membre-next/issues/1342)
- Correction de divers bugs. [#1338](https://github.com/betagouv/espace-membre-next/issues/1338), [#1340](https://github.com/betagouv/espace-membre-next/issues/1340)

### Autres changements
- Ajout de tests E2E pour le tableau de bord et les processus d'onboarding/offboarding. [#1299](https://github.com/betagouv/espace-membre-next/issues/1299)
- Mise à jour de certaines dépendances. [#1331](https://github.com/betagouv/espace-membre-next/issues/1331)
