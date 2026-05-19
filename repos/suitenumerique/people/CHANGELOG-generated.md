## Changelog : people (30 derniers jours, au 13 mai 2026)

### Résumé
Les dernières mises à jour de l'application People se concentrent sur la correction de bugs liés à l'importation et à l'utilisation de la fonctionnalité DiMail, ainsi que sur des améliorations de sécurité et des mises à jour de dépendances. Une nouvelle version a été publiée avec ces corrections et améliorations.

### Évolutions fonctionnelles
- Correction d'un bug empêchant DiMail de suivre les redirections, améliorant ainsi la fiabilité de l'importation de boîtes aux lettres.
- Correction d'un problème où le code de connexion était envoyé à une URL DiMail incorrecte.
- Correction d'un bug concernant un slash final incorrect dans l'endpoint de vérification DiMail.
- Utilisation de mailboxes v2 pour l'importation, améliorant la compatibilité et la stabilité.
- Envoi de liens de connexion au lieu de mots de passe pour les boîtes aux lettres, renforçant la sécurité.

### Évolutions techniques
- Mise à jour de la dépendance `urllib3` vers la version 2.7.0 pour corriger une vulnérabilité de sécurité.
- Mise à jour de la dépendance `next` vers la version 15.5.18 pour corriger une vulnérabilité de sécurité.
- Mise à jour de la dépendance `django` vers la version 6.0.5 pour corriger une vulnérabilité de sécurité.
- Mise à jour de la dépendance `dimail` vers la version 0.6.7 et 0.6.5.

### Autres changements
- Mise à jour des chaînes de caractères traduits pour l'internationalisation (i18n).
- Publication des versions 1.25.4, 1.25.3, 1.25.2, 1.25.1 et 1.25.0.
- Correction d'un problème potentiel de dépassement de privilèges lors de l'invitation d'utilisateurs [#1061](https://github.com/suitenumerique/people/issues/1061).
- Documentation mise à jour concernant DiMail.
