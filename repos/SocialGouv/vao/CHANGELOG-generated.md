## Changelog : vao (30 derniers jours, au 03 Juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives en matière d'accessibilité (RGAA) et de correction de bugs, notamment concernant le processus d'agrément et la gestion des documents. Des fonctionnalités liées à la sécurité (OTP) et à l'expérience utilisateur ont également été améliorées, ainsi que des optimisations techniques et des mises à jour de dépendances.

### Évolutions fonctionnelles
- Amélioration de l'accessibilité (RGAA) sur plusieurs pages : création de compte, mon agrément, étape de renouvellement, page d'hébergement. [#1258](https://github.com/SocialGouv/vao/issues/1258), [#1440](https://github.com/SocialGouv/vao/issues/1440), [#1428](https://github.com/SocialGouv/vao/issues/1428)
- Ajout de la possibilité de renvoyer le code OTP et validation de la connexion. [#1396](https://github.com/SocialGouv/vao/issues/1396)
- Amélioration du processus d'agrément avec la première étape du fusager. [#1463](https://github.com/SocialGouv/vao/issues/1463)
- Amélioration de la gestion des documents joints et des messages affichés lors du dépôt de fichiers. [#1406](https://github.com/SocialGouv/vao/issues/1406), [#1407](https://github.com/SocialGouv/vao/issues/1407)
- Ajout de la possibilité de modifier la date de l'EIG dans le back-office. [#1441](https://github.com/SocialGouv/vao/issues/1441)
- Amélioration de la gestion des informations relatives aux personnes physiques. [#1388](https://github.com/SocialGouv/vao/issues/1388)
- Ajout de la possibilité de supprimer des documents lors du renouvellement. [#1451](https://github.com/SocialGouv/vao/issues/1451)
- Correction de l'affichage des dates invalides dans le processus OTP. [#1450](https://github.com/SocialGouv/vao/issues/1450)
- Amélioration de la gestion des mails liés au workflow d'agrément. [#1423](https://github.com/SocialGouv/vao/issues/1423)

### Évolutions techniques
- Mise en place d'un feature flag pour l'insertion de l'OTP. [#1409](https://github.com/SocialGouv/vao/issues/1409)
- Amélioration de la gestion des ressources PostgreSQL en préproduction (CPU et mémoire). [#1362](https://github.com/SocialGouv/vao/issues/1362), [#1363](https://github.com/SocialGouv/vao/issues/1363)
- Correction d'un problème de validation du schéma de route DS. [#1458](https://github.com/SocialGouv/vao/issues/1458)
- Normalisation des noms de fichiers uploadés pour supprimer les caractères spéciaux. [#1389](https://github.com/SocialGouv/vao/issues/1389)
- Correction d'un bug empêchant l'activation du bouton dans le fusager lorsque le SIRET est correct. [#1352](https://github.com/SocialGouv/vao/issues/1352)
- Mise à jour de plusieurs dépendances : eslint, knex, nodemailer, nestjs. [#1379](https://github.com/SocialGouv/vao/issues/1379), [#1392](https://github.com/SocialGouv/vao/issues/1392), [#1393](https://github.com/SocialGouv/vao/issues/1393), [#1394](https://github.com/SocialGouv/vao/issues/1394)

### Autres changements
- Ajout de tests pour l'extension de visibilité de l'EIG. [#1452](https://github.com/SocialGouv/vao/issues/1452)
- Correction de la date interne des messages. [#1460](https://github.com/SocialGouv/vao/issues/1460)
- Ajout de texte de sensibilisation pour l'EIG. [#1411](https://github.com/SocialGouv/vao/issues/1411)
- Ajout des CGU et du texte associé. [#1417](https://github.com/SocialGouv/vao/issues/1417), [#1427](https://github.com/SocialGouv/vao/issues/1427)
- Mise en place de routes TypeScript. [#1380](https://github.com/SocialGouv/vao/issues/1380)
- Publication de la version 1.28.0 en préproduction et 1.28.1 en production. [#1422](https://github.com/SocialGouv/vao/issues/1422), [#1462](https://github.com/SocialGouv/vao/issues/1462)
