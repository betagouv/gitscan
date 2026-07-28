## Changelog : espace-membre-next (30 derniers jours, au 22 juillet 2026)

### Résumé
Cette version apporte des améliorations à la gestion des accès aux bureaux Ségur, des corrections concernant la synchronisation des emails et l'affichage des informations, ainsi que des ajustements pour l'intégration de nouveaux outils de monitoring (Sentry, Matomo) et de communication (Tchap).

### Évolutions fonctionnelles
- Ajout d'une fonctionnalité de demande d'accès aux bureaux Ségur. [#1460](https://github.com/betagouv/espace-membre-next/issues/1460)
- Mise à jour de la checklist d'onboarding avec les chaînes Tchap. [#1450](https://github.com/betagouv/espace-membre-next/issues/1450)
- Ajout d'informations supplémentaires concernant Tchap. [#1437](https://github.com/betagouv/espace-membre-next/issues/1437)
- Ajout d'un champ pour le choix de scalingo. [#1434](https://github.com/betagouv/espace-membre-next/issues/1434)
- Mise à jour du statut des emails des membres. [#1447](https://github.com/betagouv/espace-membre-next/issues/1447)

### Évolutions techniques
- Migration de Sentry et Matomo vers les demandes OPS. [#1436](https://github.com/betagouv/espace-membre-next/issues/1436)
- Correction de l'initialisation du SDK Sentry. [#1426](https://github.com/betagouv/espace-membre-next/issues/1426)
- Correction de la gestion de la synchronisation des emails (dimail) : réactivation de la mailbox et suppression d'appels directs à `startSync`. [#1449](https://github.com/betagouv/espace-membre-next/issues/1449)
- Correction d'une exception potentielle lors de l'affichage des formations sans description. [#1438](https://github.com/betagouv/espace-membre-next/issues/1438)

### Autres changements
- Masquage des informations obsolètes concernant les comptes Matomo/Sentry. [#1440](https://github.com/betagouv/espace-membre-next/issues/1440)
- Suppression de code inutile et de services obsolètes. [#1459](https://github.com/betagouv/espace-membre-next/issues/1459), [#1448](https://github.com/betagouv/espace-membre-next/issues/1448)
- Ajout d'une icône manquante. [#1436](https://github.com/betagouv/espace-membre-next/issues/1436)
