## Changelog : vao (30 derniers jours, au 26 juin 2026)

### Résumé
Cette période a été marquée par des corrections de bugs et des améliorations de l'expérience utilisateur, notamment concernant le renouvellement des agréments, la gestion des documents, la sécurité (OTP) et l'accessibilité (RGAA). Des optimisations techniques ont également été apportées, ainsi que des mises à jour de dépendances.

### Évolutions fonctionnelles
- **Renouvellement d'agrément :** Amélioration du bouton de suppression lors de l'étape 4 du renouvellement [#1451](https://github.com/SocialGouv/vao/issues/1451).
- **Documents :** Normalisation des noms de fichiers uploadés en supprimant les caractères spéciaux [#1389](https://github.com/SocialGouv/vao/issues/1389). Correction de problèmes liés aux documents joints lors du renouvellement [#1420](https://github.com/SocialGouv/vao/issues/1420).
- **Authentification :** Implémentation de la validation du code OTP par email, avec gestion des tentatives et possibilité de renvoi [#1396](https://github.com/SocialGouv/vao/issues/1396), [#1408](https://github.com/SocialGouv/vao/issues/1408), [#1416](https://github.com/SocialGouv/vao/issues/1416). Ajout de la persistance du code OTP avec l'option "se souvenir de moi" [#1408](https://github.com/SocialGouv/vao/issues/1408).
- **RGAA :** Améliorations de l'accessibilité sur la page "Mon agrément" [#1391](https://github.com/SocialGouv/vao/issues/1391) et pour l'hébergement [#1436](https://github.com/SocialGouv/vao/issues/1436). Correction d'une date invalide provenant de l'environnement de pré-production [#1450](https://github.com/SocialGouv/vao/issues/1450).
- **EIG :** Ajout d'un validateur pour le schéma EIG dans le back-office [#1437](https://github.com/SocialGouv/vao/issues/1437). Modification du datePicker dans le back-office EIG [#1441](https://github.com/SocialGouv/vao/issues/1441). Ajout de texte de sensibilisation et des CGUs pour l'EIG [#1417](https://github.com/SocialGouv/vao/issues/1417), [#1418](https://github.com/SocialGouv/vao/issues/1418).
- **Fusager :** Correction de l'accès aux comptes Fusager en provenance de la pré-production [#1445](https://github.com/SocialGouv/vao/issues/1445). Correction d'un problème d'activation du bouton dans le brouillon lorsque le SIRET est correct [#1352](https://github.com/SocialGouv/vao/issues/1352), [#1390](https://github.com/SocialGouv/vao/issues/1390).
- **Autres :** Correction d'un problème lié aux informations de la personne physique [#1388](https://github.com/SocialGouv/vao/issues/1388).

### Évolutions techniques
- **Antivirus :** Configuration de l'antivirus pour qu'il échoue en mode fermé, améliorant la sécurité [#1413](https://github.com/SocialGouv/vao/issues/1413).
- **Infrastructure :** Augmentation des ressources CPU et mémoire pour la base de données CNPG en production [#1362](https://github.com/SocialGouv/vao/issues/1362), [#1363](https://github.com/SocialGouv/vao/issues/1363).
- **CI/CD :** Publication de la version 1.28.0 en pré-production [#1422](https://github.com/SocialGouv/vao/issues/1422).
- **Typescript :** Migration vers des routes Typescript [#1380](https://github.com/SocialGouv/vao/issues/1380).

### Autres changements
- **Documentation :** Mise à jour de la documentation.
- **Dépendances :** Mises à jour de plusieurs dépendances (NestJS, Nodemailer, Knex, ts-jest, axios, multer, nuxt) pour bénéficier des dernières corrections et améliorations.
- **Tests :** Amélioration de la configuration des tests.
- **Nettoyage de code :** Suppression de code inutile et amélioration de la lisibilité du code.
