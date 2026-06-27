## Changelog : maestro (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, les évolutions de Maestro se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans la gestion des documents, des analyses et des laboratoires. Des corrections de bugs et des améliorations de la sécurité ont également été apportées. L'intégration avec des services externes comme Inovalys et Brevo a été optimisée.

### Évolutions fonctionnelles
- **Laboratoires :** Amélioration de la recherche de laboratoires grâce à une autocomplétion. [#1136](https://github.com/betagouv/maestro/issues/1136)
- **Prélèvements :** Possibilité de modifier un prélèvement même si l'utilisateur n'est pas le préleveur initial, sous confirmation volontaire. [#1090](https://github.com/betagouv/maestro/issues/1090)
- **Labcam :** Correction des droits d'accès aux données du Labcam pour le bureau des laboratoires. [#1135](https://github.com/betagouv/maestro/issues/1135)
- **Documents :** Les utilisateurs du "Suivi national" peuvent maintenant supprimer des documents. [#1114](https://github.com/betagouv/maestro/issues/1114)
- **DAI :** Possibilité de remettre en erreur des DAI pour les relancer. [#1063](https://github.com/betagouv/maestro/issues/1063)
- **Sacha :** Amélioration de la gestion des destinataires et de l'envoi d'emails. [#1047](https://github.com/betagouv/maestro/issues/1047) et [#1062](https://github.com/betagouv/maestro/issues/1062)
- **LMR :** Gestion améliorée des LMR optionnelles et des alertes associées. [#1085](https://github.com/betagouv/maestro/issues/1085) et [#1092](https://github.com/betagouv/maestro/issues/1092)
- **Interface utilisateur :** Implémentation d'un nouveau header. [#1127](https://github.com/betagouv/maestro/issues/1127)
- **Plans :** Refonte de la gestion des plans avec introduction de "sous-plans". [#1007](https://github.com/betagouv/maestro/issues/1007)
- **SEVES :** Ajout d'un bandeau d'alerte SEVES pour les dépassements de LMR. [#1074](https://github.com/betagouv/maestro/issues/1074)

### Évolutions techniques
- **Refactoring :** Utilisation d'un outil de génération d'URL pour l'export dans le module Labcam. [#1128](https://github.com/betagouv/maestro/issues/1128)
- **Refactoring :** Séparation des routes des documents de prélèvements et des documents ressources. [#1123](https://github.com/betagouv/maestro/issues/1123)
- **API :** Ajout d'une API pour SEVES. [#900](https://github.com/betagouv/maestro/issues/900)
- **Typage :** Amélioration du typage des réponses API. [#1006](https://github.com/betagouv/maestro/issues/1006)
- **Nodemailer :** Utilisation du relai SMTP Brevo pour l'envoi d'emails. [#991](https://github.com/betagouv/maestro/issues/991)
- **GPG :** Importation dynamique de la clé GPG si elle est mise à jour. [#1129](https://github.com/betagouv/maestro/issues/1129)
- **Tests :** Ajout d'un tri par défaut pour corriger un test intermittent. [#1121](https://github.com/betagouv/maestro/issues/1121)

### Autres changements
- **Documentation :** Mises à jour et améliorations de la documentation.
- **Dépendances :** Mises à jour de plusieurs dépendances (React Router, Faker, Fast XML Parser, Actions Checkout, etc.). Ces mises à jour sont gérées par Dependabot et ne sont pas listées en détail ici.
- **Configuration :** Diverses modifications de configuration et nettoyage de code.
- **Sentry :** Capture correcte des erreurs console.error. (revert d'un commit précédent)
- **Étiquettes :** Correction de la génération des anciennes étiquettes. [#1065](https://github.com/betagouv/maestro/issues/1065)
- **Dashboard :** Correction de l'affichage des actions prioritaires. [#1054](https://github.com/betagouv/maestro/issues/1054)
