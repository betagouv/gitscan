## Changelog : espace-membre-next (30 derniers jours, au 17 juillet 2026)

### Résumé
Les dernières mises à jour apportent des améliorations à la gestion des emails, des informations sur les startups et des outils d'administration. Des corrections ont été apportées pour améliorer la stabilité et l'expérience utilisateur, notamment concernant l'affichage des formations et la gestion des comptes. L'intégration avec les services OPS a également été améliorée.

### Évolutions fonctionnelles
- Possibilité de rechercher les startups par suivi [#1423](https://github.com/betagouv/espace-membre-next/issues/1423).
- Ajout d'informations Tchap plus détaillées pour les membres [#1437](https://github.com/betagouv/espace-membre-next/issues/1437).
- Affichage de l'identifiant Matrix des membres [#1411](https://github.com/betagouv/espace-membre-next/issues/1411).
- Ajout des champs `contact_dinum` et `contact_incubator` pour les startups [#1410](https://github.com/betagouv/espace-membre-next/issues/1410).
- Mise à jour du statut des comptes pour les outils et suppression des emails en bounce [#1421](https://github.com/betagouv/espace-membre-next/issues/1421).
- Ajout d'un champ pour le choix de scalingo [#1434](https://github.com/betagouv/espace-membre-next/issues/1434).
- Ajout d'un événement "EIG" pour les startups [#805085e](https://github.com/betagouv/espace-membre-next/commit/805085e).
- Mise à jour du statut des emails des membres [#1447](https://github.com/betagouv/espace-membre-next/issues/1447).

### Évolutions techniques
- Migration de Sentry et Matomo vers les demandes OPS [#1436](https://github.com/betagouv/espace-membre-next/issues/1436).
- Correction de l'initialisation du SDK Sentry [#80f1901](https://github.com/betagouv/espace-membre-next/commit/80f1901).
- Correction pour éviter une exception lors de l'affichage des formations sans description [#1438](https://github.com/betagouv/espace-membre-next/issues/1438).
- Correction pour la vérification des comptes Matrix (prise en compte des comptes `.ext`) [#1424](https://github.com/betagouv/espace-membre-next/issues/1424).
- Suppression du code obsolète lié à `unblockEmailsThatAreActive` [#1412](https://github.com/betagouv/espace-membre-next/issues/1412).
- Suppression du champ `tjm` des utilisateurs [#1403](https://github.com/betagouv/espace-membre-next/issues/1403).
- Correction pour réactiver la mailbox et non l'alias dans dimail [#1449](https://github.com/betagouv/espace-membre-next/issues/1449).
- Correction pour exposer `startSync` pour dimail [#785cf49](https://github.com/betagouv/espace-membre-next/commit/785cf49).
- Correction pour éviter l'appel direct à `startSync` dans `syncDinumEmails` [#265f6c3](https://github.com/betagouv/espace-membre-next/commit/265f6c3).
- Correction d'un bug Sentry [#1426](https://github.com/betagouv/espace-membre-next/issues/1426).

### Autres changements
- Masquage des informations obsolètes concernant les comptes Matomo/Sentry [#1440](https://github.com/betagouv/espace-membre-next/issues/1440).
- Modification du formulaire [#1425](https://github.com/betagouv/espace-membre-next/issues/1425).
- Ajout d'un formulaire pour les demandes d'OPS vers Grist [#1406](https://github.com/betagouv/espace-membre-next/issues/1406).
- Correction d'une icône manquante [#37fb2cf](https://github.com/betagouv/espace-membre-next/commit/37fb2cf).
