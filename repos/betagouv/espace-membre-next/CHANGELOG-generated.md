## Changelog : espace-membre-next (30 derniers jours, au 20 juillet 2026)

### Résumé
Les dernières mises à jour de l'espace membre se concentrent sur l'amélioration de la gestion des emails, l'intégration de nouveaux outils de monitoring (Sentry et Matomo) et l'ajout de fonctionnalités de recherche et d'information pour les startups et les membres. Des corrections de bugs ont également été apportées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout de la possibilité de rechercher des startups par leur statut de suivi [#1423](https://github.com/betagouv/espace-membre-next/issues/1423).
- Amélioration des informations affichées concernant les canaux Tchap pour l'onboarding [#1450](https://github.com/betagouv/espace-membre-next/issues/1450) et ajout d'informations supplémentaires sur Tchap [#1437](https://github.com/betagouv/espace-membre-next/issues/1437).
- Ajout d'un champ pour le choix de scalingo [#1434](https://github.com/betagouv/espace-membre-next/issues/1434).
- Ajout d'un événement "EIG" pour les startups.
- Mise à jour du statut des comptes (passage à "Outils" et suppression des emails en bounce) [#1421](https://github.com/betagouv/espace-membre-next/issues/1421).
- Correction d'une exception lors de l'affichage des formations sans description [#1438](https://github.com/betagouv/espace-membre-next/issues/1438).
- Correction pour la vérification des comptes Matrix, incluant les comptes `.ext` [#1424](https://github.com/betagouv/espace-membre-next/issues/1424).

### Évolutions techniques
- Intégration et configuration de Sentry et Matomo pour le monitoring des performances et des erreurs, en passant par les demandes OPS [#1436](https://github.com/betagouv/espace-membre-next/issues/1436) et [#1426](https://github.com/betagouv/espace-membre-next/issues/1426).
- Correction de l'initialisation du SDK Sentry.
- Amélioration de la synchronisation des emails (correction d'appels directs à `startSync` et mise à jour du statut des emails) [#1447](https://github.com/betagouv/espace-membre-next/issues/1447).
- Suppression de services inutilisés [#1448](https://github.com/betagouv/espace-membre-next/issues/1448).
- Correction de l'activation de la boîte aux lettres DiMail [#1449](https://github.com/betagouv/espace-membre-next/issues/1449).
- Masquage des informations obsolètes concernant les comptes Matomo/Sentry [#1440](https://github.com/betagouv/espace-membre-next/issues/1440).

### Autres changements
- Correction d'une icône manquante [#1437](https://github.com/betagouv/espace-membre-next/issues/1437).
- Modifications du formulaire [#1425](https://github.com/betagouv/espace-membre-next/issues/1425).
