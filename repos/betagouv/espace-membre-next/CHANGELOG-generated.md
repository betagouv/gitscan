## Changelog : espace-membre-next (30 derniers jours, au 22 juillet 2026)

### Résumé
Cette version apporte des améliorations à la gestion des accès, notamment pour les demandes d'accès aux bureaux Ségur, et des corrections concernant l'intégration de Sentry et Matomo. Des ajustements ont également été faits pour améliorer l'expérience utilisateur, comme la mise à jour de la checklist d'onboarding et l'affichage des informations sur les formations.

### Évolutions fonctionnelles
- Ajout d'une fonctionnalité de demande d'accès aux bureaux Ségur. [#1460](https://github.com/betagouv/espace-membre-next/issues/1460)
- Mise à jour de la checklist d'onboarding avec les canaux Tchap. [#1450](https://github.com/betagouv/espace-membre-next/issues/1450)
- Ajout d'informations supplémentaires sur Tchap. [#1437](https://github.com/betagouv/espace-membre-next/issues/1437)
- Ajout d'un champ pour le choix de scalingo. [#1434](https://github.com/betagouv/espace-membre-next/issues/1434)
- Mise à jour du statut des emails des membres. [#1447](https://github.com/betagouv/espace-membre-next/issues/1447)

### Évolutions techniques
- Intégration de Sentry et Matomo dans les demandes OPS. [#1436](https://github.com/betagouv/espace-membre-next/issues/1436)
- Correction de l'initialisation du SDK Sentry. [#1426](https://github.com/betagouv/espace-membre-next/issues/1426)
- Correction de l'activation de la mailbox (et non de l'alias) pour dimail. [#1449](https://github.com/betagouv/espace-membre-next/issues/1449)
- Suppression d'appels directs à `startSync` dans `syncDinumEmails`.
- Exposition de `startSync` pour dimail.
- Correction d'une exception lors de l'affichage des formations sans description. [#1438](https://github.com/betagouv/espace-membre-next/issues/1438)

### Autres changements
- Masquage des informations obsolètes concernant les comptes Matomo et Sentry. [#1440](https://github.com/betagouv/espace-membre-next/issues/1440)
- Suppression de services inutiles. [#1448](https://github.com/betagouv/espace-membre-next/issues/1448)
- Suppression de code inutile. [#1459](https://github.com/betagouv/espace-membre-next/issues/1459)
- Ajout d'une icône manquante.
