## Changelog : federation (30 derniers jours, au 10 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité et de la gestion des rôles et des autorisations, ainsi que sur la modernisation de l'infrastructure et des dépendances. Des corrections ont également été apportées pour améliorer l'expérience utilisateur, notamment au niveau de l'autocomplétion des mots de passe et de l'affichage des informations d'organisation.

### Évolutions fonctionnelles
- Amélioration de l'affichage des informations d'organisation dans les messages d'erreur Y500015 [#1231](https://github.com/proconnect-gouv/federation/issues/1231).
- Amélioration de l'autocomplétion des mots de passe avec Bitwarden, corrigeant un problème de remplissage [#1231](https://github.com/proconnect-gouv/federation/issues/1231).
- Ajout de l'étiquette d'organisation par défaut lors de la création d'un prestataire de services [#1181](https://github.com/proconnect-gouv/federation/issues/1181).
- Alignement de la classification des services publics avec la définition légale actualisée [#1215](https://github.com/proconnect-gouv/federation/issues/1215).
- Ajout de rôles par défaut dans l'interface d'administration [#1161](https://github.com/proconnect-gouv/federation/issues/1161) et [#1200](https://github.com/proconnect-gouv/federation/issues/1200).
- Utilisation des valeurs de rôles pour restreindre l'accès aux prestataires de services aux utilisateurs non publics [#1158](https://github.com/proconnect-gouv/federation/issues/1158).
- Mise à jour de l'utilisation du flag de fonctionnalité de validation d'email [#1160](https://github.com/proconnect-gouv/federation/issues/1160).

### Évolutions techniques
- Mise à jour de l'infrastructure pour utiliser Node 24.16 dans l'application d'administration [#1186](https://github.com/proconnect-gouv/federation/issues/1186) et [#1222](https://github.com/proconnect-gouv/federation/issues/1222).
- Suppression de l'application BridgeHttpProxyRie [#1198](https://github.com/proconnect-gouv/federation/issues/1198).
- Suppression des rôles de base de données dans l'administration [#1184](https://github.com/proconnect-gouv/federation/issues/1184).
- Publication de l'image core-fca-low-migrator sur GHCR [#1195](https://github.com/proconnect-gouv/federation/issues/1195).
- Remplacement de `resolveMx` par une requête DNS-over-HTTPS `fetch` dans le validateur d'email [#1159](https://github.com/proconnect-gouv/federation/issues/1159).
- Mise à jour des packages ProConnect Identité [#1214](https://github.com/proconnect-gouv/federation/issues/1214).
- Suppression du healthcheck_live de la configuration de build Docker [#1194](https://github.com/proconnect-gouv/federation/issues/1194).

### Autres changements
- Mise à jour de plusieurs dépendances (axe-core, jest, @nestjs/testing, ruff, ejs, commander, tsx, prettier, otplib, helmet, etc.)
- Corrections et améliorations diverses de la configuration et du code.
- Ajout de logs pour le débogage des divergences entre les anciennes et nouvelles méthodes de calcul des services publics [#1199](https://github.com/proconnect-gouv/federation/issues/1199).
- Changement de branding de FranceConnect à ProConnect dans l'interface d'administration [#1228](https://github.com/proconnect-gouv/federation/issues/1228).
