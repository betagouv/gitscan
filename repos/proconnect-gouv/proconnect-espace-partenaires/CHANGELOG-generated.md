## Changelog : proconnect-espace-partenaires (30 derniers jours, au 8 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent principalement sur l'amélioration de la documentation pour les partenaires, notamment concernant l'intégration avec eIDAS et les différents niveaux d'authentification. Des corrections et clarifications ont également été apportées concernant les erreurs et les données fournies. Des mises à jour techniques et de dépendances ont été effectuées pour maintenir la sécurité et la stabilité de la plateforme.

### Évolutions fonctionnelles
- Amélioration de la documentation concernant les erreurs liées au `redirect_uri` (Y030031) pour les fournisseurs de service. [#339](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/339)
- Clarification de la documentation concernant les niveaux d'authentification eIDAS pour les fournisseurs de service, notamment la distinction entre eIDAS1-MFA et eIDAS2. [#349](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/349)
- Ajout de documentation sur l'utilisation des scopes `roles`. [#331](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/331)
- Ajout de documentation sur l'utilisation de l'organisation et du numéro SIRET professionnel. [#330](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/330)
- Ajout de documentation sur les ACrs d'Entra ID. [#323](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/323)
- Correction d'informations inexactes dans les tests d'identifiants FI. [#346](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/346)

### Évolutions techniques
- Renommage de la base de données MongoDB en `corev2` et de l'utilisateur en `proconnect-app-api-partner`. [#337](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/337)
- Mise à jour de la configuration du serveur UUV pour corriger un problème de chargement intermittent dans les tests E2E.
- Restructuration de la documentation des données fournies pour clarifier leur origine. [#317](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/317)
- Suppression d'une exigence d'autorisation obsolète pour le scope `roles`. [#353](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/353)
- Ajout d'une mention de la table des matières de l'organisation dans la documentation. [#351](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/351)
- Ajout de la ressource `norme_eidas` partagée à la documentation FS et FI. [#352](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/352)
- Déplacement du contenu eIDAS partagé vers le dossier `ressources/`. [#350](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/350)

### Autres changements
- Mise à jour de la documentation pour clarifier la gestion de MFA avec Keycloak. [#338](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/338)
- Correction d'une faute de frappe dans la documentation. [#354](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/354)
- Plusieurs mises à jour de dépendances ont été effectuées pour maintenir la sécurité et la stabilité du projet. (Ces mises à jour sont omises dans ce changelog.)
