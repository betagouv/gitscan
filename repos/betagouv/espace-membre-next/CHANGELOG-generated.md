## Changelog : espace-membre-next (30 derniers jours, au 22 juillet 2026)

### Résumé
Cette version apporte des améliorations à la gestion des accès aux bureaux Ségur, à la synchronisation des emails, et à l'intégration des outils de monitoring (Sentry et Matomo). Des corrections ont également été apportées pour améliorer la stabilité et l'expérience utilisateur, notamment au niveau de l'onboarding et de l'affichage des formations.

### Évolutions fonctionnelles
- Ajout d'une fonctionnalité de demande d'accès aux bureaux Ségur. [#1460](https://github.com/betagouv/espace-membre-next/issues/1460)
- Mise à jour de la checklist d'onboarding avec les canaux Tchap. [#1450](https://github.com/betagouv/espace-membre-next/issues/1450)
- Amélioration de l'affichage des informations Tchap. [#1437](https://github.com/betagouv/espace-membre-next/issues/1437)
- Mise à jour du statut des emails des membres. [#1447](https://github.com/betagouv/espace-membre-next/issues/1447)

### Évolutions techniques
- Refonte de l'intégration de Sentry et Matomo pour les demandes OPS. [#1436](https://github.com/betagouv/espace-membre-next/issues/1436)
- Correction de l'initialisation du SDK Sentry.
- Correction de la synchronisation des emails (dimail) : réactivation de la mailbox et suppression d'appels directs à `startSync`. [#1449](https://github.com/betagouv/espace-membre-next/issues/1449)
- Correction d'une exception potentielle lors de l'affichage des formations si la description est manquante. [#1438](https://github.com/betagouv/espace-membre-next/issues/1438)
- Correction d'un bug Sentry. [#1426](https://github.com/betagouv/espace-membre-next/issues/1426)

### Autres changements
- Masquage des informations obsolètes concernant les comptes Matomo et Sentry. [#1440](https://github.com/betagouv/espace-membre-next/issues/1440)
- Suppression de code inutile. [#1459](https://github.com/betagouv/espace-membre-next/issues/1459)
- Suppression de services inutiles. [#1448](https://github.com/betagouv/espace-membre-next/issues/1448)
- Ajout d'une icône manquante. [#1437](https://github.com/betagouv/espace-membre-next/issues/1437)
