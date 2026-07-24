## Changelog : espace-membre-next (30 derniers jours, au 22 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des accès et des informations des membres, notamment en intégrant les demandes d'accès aux bureaux Ségur et en mettant à jour les informations relatives à Tchap et Matomo/Sentry. Des corrections ont également été apportées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout d'une fonctionnalité de demande d'accès aux bureaux Ségur. [#1460](https://github.com/betagouv/espace-membre-next/issues/1460)
- Mise à jour de la checklist d'onboarding avec les canaux Tchap. [#1450](https://github.com/betagouv/espace-membre-next/issues/1450)
- Ajout d'informations supplémentaires sur Tchap. [#1437](https://github.com/betagouv/espace-membre-next/issues/1437)
- Possibilité de rechercher les startups par suivi. [#1423](https://github.com/betagouv/espace-membre-next/issues/1423)
- Ajout d'un champ pour le choix de scalingo. [#1434](https://github.com/betagouv/espace-membre-next/issues/1434)
- Modification du formulaire. [#1425](https://github.com/betagouv/espace-membre-next/issues/1425)

### Évolutions techniques
- Mise à jour de l'intégration Sentry et Matomo pour les demandes OPS. [#1436](https://github.com/betagouv/espace-membre-next/issues/1436)
- Correction de l'initialisation du SDK Sentry.
- Correction de l'activation de la boîte aux lettres (dimail) et non de l'alias. [#1449](https://github.com/betagouv/espace-membre-next/issues/1449)
- Correction pour exposer `startSync` pour dimail.
- Correction pour supprimer l'appel direct à `startSync` dans `syncDinumEmails`.
- Mise à jour du statut des emails des membres. [#1447](https://github.com/betagouv/espace-membre-next/issues/1447)
- Correction pour éviter une exception lors de l'affichage des formations sans description. [#1438](https://github.com/betagouv/espace-membre-next/issues/1438)
- Correction pour vérifier également les comptes `.ext` dans Matrix. [#1424](https://github.com/betagouv/espace-membre-next/issues/1424)
- Correction d'un bug Sentry. [#1426](https://github.com/betagouv/espace-membre-next/issues/1426)

### Autres changements
- Masquage des informations obsolètes des comptes Matomo/Sentry. [#1440](https://github.com/betagouv/espace-membre-next/issues/1440)
- Suppression de services inutiles. [#1448](https://github.com/betagouv/espace-membre-next/issues/1448)
- Suppression de code inutile. [#1459](https://github.com/betagouv/espace-membre-next/issues/1459)
- Ajout d'une icône manquante.
