## Changelog : vao (30 derniers jours, au 25 juin 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'expérience utilisateur, notamment sur le renouvellement des agréments et la gestion des documents. Des corrections ont été apportées pour améliorer l'accessibilité (RGAA) et la robustesse de l'application, en particulier concernant la gestion des comptes utilisateurs et des OTP (One-Time Password). Des optimisations techniques ont également été réalisées, notamment au niveau de la configuration et des dépendances.

### Évolutions fonctionnelles
- Amélioration de l'accessibilité (RGAA) pour l'hébergement et la page "mon agrément" [#1391](https://github.com/SocialGouv/vao/issues/1391).
- Ajout de la possibilité de filtrer par date de naissance dans la recherche d'organismes [#1433](https://github.com/SocialGouv/vao/issues/1433).
- Implémentation de la limitation de l'envoi d'emails pour les comptes OVA valides [#1444](https://github.com/SocialGouv/vao/issues/1444).
- Amélioration du formulaire de renouvellement d'agrément : correction des messages contradictoires et des problèmes de téléchargement de documents [#1381](https://github.com/SocialGouv/vao/issues/1381), [#1421](https://github.com/SocialGouv/vao/issues/1421).
- Ajout de la possibilité de renvoyer le code OTP et de valider la connexion [#1396](https://github.com/SocialGouv/vao/issues/1396).
- Ajout de la possibilité de modifier la date dans le sélecteur de date dans le back-office pour les EIG [#1441](https://github.com/SocialGouv/vao/issues/1441).
- Ajout de la possibilité de récupérer le schéma de contrôle pour les EIG dans le back-office [#1437](https://github.com/SocialGouv/vao/issues/1437).
- Amélioration de la gestion des comptes Fusager en pré-production [#1445](https://github.com/SocialGouv/vao/issues/1445).
- Ajout de texte de sensibilisation et de CGU pour l'OTP [#1427](https://github.com/SocialGouv/vao/issues/1427).
- Envoi d'email de prise en charge [#1400](https://github.com/SocialGouv/vao/issues/1400).

### Évolutions techniques
- Mise à jour de plusieurs dépendances : `nestjs`, `nodemailer`, `knex`, `ts-jest`, `axios`, `multer`, `nuxt` [#1377](https://github.com/SocialGouv/vao/issues/1377), [#1376](https://github.com/SocialGouv/vao/issues/1376), [#1375](https://github.com/SocialGouv/vao/issues/1375), [#1374](https://github.com/SocialGouv/vao/issues/1374), [#1373](https://github.com/SocialGouv/vao/issues/1373).
- Amélioration de la configuration de Jest et des tests E2E (timeout, filtres) [#1366](https://github.com/SocialGouv/vao/issues/1366), [#1365](https://github.com/SocialGouv/vao/issues/1365), [#1364](https://github.com/SocialGouv/vao/issues/1364).
- Correction de problèmes liés aux ressources PostgreSQL en production et pré-production [#1363](https://github.com/SocialGouv/vao/issues/1363), [#1399](https://github.com/SocialGouv/vao/issues/1399), [#1397](https://github.com/SocialGouv/vao/issues/1397).
- Normalisation des noms de fichiers uploadés pour supprimer les caractères spéciaux [#1389](https://github.com/SocialGouv/vao/issues/1389).
- Ajout d'un feature flag pour l'envoi du code OTP [#1409](https://github.com/SocialGouv/vao/issues/1409).
- Amélioration de la gestion des cookies OTP [#1416](https://github.com/SocialGouv/vao/issues/1416).
- Correction d'un bug empêchant l'activation du bouton dans le cas d'un SIRET identique [#1352](https://github.com/SocialGouv/vao/issues/1352).

### Autres changements
- Correction de divers bugs et améliorations mineures de l'interface utilisateur.
- Mise en place de la release 1.28.0 en pré-production [#1422](https://github.com/SocialGouv/vao/issues/1422).
- Correction de problèmes liés aux CGU et à l'OTP [#1432](https://github.com/SocialGouv/vao/issues/1432).
- Correction d'un problème d'affichage de l'agrément après renouvellement [#1398](https://github.com/SocialGouv/vao/issues/1398).
- Correction d'un problème lié au chargement du SIRET dans le formulaire d'hébergement [#1403](https://github.com/SocialGouv/vao/issues/1403).
