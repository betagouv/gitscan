## Changelog : proconnect-identite (30 derniers jours, au 24 août 2026)

### Résumé
Ce mois-ci, le projet a connu des améliorations significatives de l'expérience utilisateur, notamment sur la gestion de l'authentification forte (MFA) et la clarté des communications par email. En parallèle, une refonte technique majeure a été opérée pour moderniser l'architecture interne via l'utilisation de "connectors" et optimiser la gestion des données SIREN.

### Évolutions fonctionnelles
- **Amélioration de l'expérience MFA** : ajout d'un assistant (helper) dans les sections de connexion et de compte pour guider l'utilisateur, incluant un bouton de redémarrage pour faciliter la navigation en cas d'erreur [#2044](https://github.com/proconnect-gouv/proconnect-identite/pull/2044).
- **Fluidification de l'authentification** : déclenchement automatique de la passkey si celle-ci est déjà configurée, évitant un clic supplémentaire [#2080](https://github.com/proconnect-gouv/proconnect-identite/pull/2080).
- **Optimisation des communications par email** :
    - Création d'un modèle d'email dédié pour les codes OTP [#2066](https://github.com/proconnect-gouv/proconnect-identite/pull/2066).
    - Notification automatique par email lorsqu'une demande de modération est annulée [#2079](https://github.com/proconnect-gouv/proconnect-identite/pull/2079).
    - Clarification du texte des emails de vérification [#2056](https://github.com/proconnect-gouv/proconnect-identite/pull/2056).
    - Ajout du SIRET et du libellé de l'organisation dans les emails d'échec de jonction [#2073](https://github.com/proconnect-gouv/proconnect-identite/pull/2073).
- **Mise à jour métier** : actualisation de l'algorithme de jonction de commune [#2039](https://github.com/proconnect-gouv/proconnect-identite/pull/2039).

### Évolutions techniques
- **Refonte de l'architecture** : migration massive de divers dépôts (utilisateur, organisation, authentificateur, modération, etc.) vers un modèle de "connectors" pour une meilleure modularité [#2090](https://github.com/proconnect-gouv/proconnect-identite/pull/2090), [#2093](https://github.com/proconnect-gouv/proconnect-identite/pull/2093), [#2094](https://github.com/proconnect-gouv/proconnect-identite/pull/2094), [#2095](https://github.com/proconnect-gouv/proconnect-identite/pull/2095), [#2096](https://github.com/proconnect-gouv/proconnect-identite/pull/2096), [#2097](https://github.com/proconnect-gouv/proconnect-identite/pull/2097).
- **Optimisation des données** : remplacement de l'appel à l'Annuaire des Entreprises par une récupération directe des listes SIREN via Grist pour plus de fiabilité [#2078](https://github.com/proconnect-gouv/proconnect-identite/pull/2078).
- **Refactoring et maintenance** :
    - Consolidation des vues dupliquées pour les paramètres MFA [#2076](https://github.com/proconnect-gouv/proconnect-identite/pull/2076).
    - Suppression du support du scope `organisations` [#2055](https://github.com/proconnect-gouv/proconnect-identite/pull/2055).
    - Refonte de la chaîne de garde pour les exigences de connexion utilisateur (recursive check) [#1769](https://github.com/proconnect-gouv/proconnect-identite/pull/1769).
- **Amélioration de la CI/CD et des tests** :
    - Optimisation du temps de réinitialisation de la base de données lors des tests.
    - Standardisation des commandes de tests E2E [#2068](https://github.com/proconnect-gouv/proconnect-identite/pull/2068).

### Autres changements
- **Nettoyage du code** : suppression de la variable d'environnement inutilisée `ZAMMAD_TOKEN` [#2085](https://github.com/proconnect-gouv/proconnect-identite/pull/2085) et des paramètres de templates d'email obsolètes [#2058](https://github.com/proconnect-gouv/proconnect-identite/pull/2058).
- **Suppression de code legacy** : retrait de l'implémentation obsolète `is_service_public`.
