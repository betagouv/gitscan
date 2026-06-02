## Changelog : proconnect-espace-partenaires (30 derniers jours, au 29 mai 2026)

### Résumé
Ce mois-ci, les mises à jour se sont concentrées sur l'amélioration de la documentation pour les partenaires, notamment concernant l'intégration avec des solutions d'authentification comme Keycloak et LemonLDAP::NG, ainsi que la clarification des erreurs et des données échangées. Des ajustements techniques ont également été effectués pour optimiser la configuration de l'environnement de test et la gestion des bases de données.

### Évolutions fonctionnelles
- Clarification de la différence entre les configurations EIDAS1-MFA et EIDAS2 dans la documentation. [#349](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/349)
- Ajout d'une page dédiée dans la documentation pour l'erreur `redirect_uri mismatch` (Y030031). [#339](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/339)
- Mise à jour des informations incorrectes concernant les tests d'identifiants FI. [#346](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/346)
- Ajout de précisions concernant l'utilisation des ACrs (Authentication Contexts) avec Entra ID. [#323](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/323)
- Ajout d'une mention concernant l'organisation et le SIRET professionnel. [#330](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/330)
- Ajout de documentation sur les scopes et les rôles. [#331](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/331)
- Clarification que les claims utilisateur sont retournés via l'endpoint `/user-info`. [#322](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/322)
- Ajout d'une section sur la configuration MFA (Multi-Factor Authentication) pour LemonLDAP::NG. [#316](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/316)

### Évolutions techniques
- Renommage de la base de données MongoDB en `corev2` et de l'utilisateur en `proconnect-app-api-partner`. [#337](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/337)
- Correction de la configuration du serveur web UUV dans les tests E2E et résolution d'un problème d'assertion de chargement intermittent.
- Retour en arrière d'une mise à jour de `nodemailer` qui causait des problèmes. [#335](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/335)
- Regroupement des données additionnelles et complémentaires. [#347](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/347)
- Restructuration de la documentation des données fournies pour clarifier leur origine. [#317](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/317)

### Autres changements
- Correction d'une faute de frappe. [#340](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/340)
- Mise à jour de la documentation concernant l'intégration Keycloak MFA. [#338](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/338)
