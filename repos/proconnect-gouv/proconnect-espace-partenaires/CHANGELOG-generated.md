## Changelog : proconnect-espace-partenaires (30 derniers jours, au 21 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la documentation, la correction de problèmes liés à l'authentification et à l'infrastructure, ainsi que des mises à jour techniques pour maintenir la sécurité et la performance de l'application. L'ajout de la gestion de l'authentification multi-facteur (MFA) avec Keycloak est une avancée significative.

### Évolutions fonctionnelles
- Amélioration de la documentation concernant les erreurs `redirect_uri mismatch` dans l'espace partenaire ([#339](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/339)).
- Ajout de la gestion de l'authentification multi-facteur (MFA) avec Keycloak ([#338](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/338)).
- Précision de la gestion des ACrs (Authentication Context Reference) pour l'eIDAS1 lorsque ceux-ci ne sont pas gérés ([a037e8b](https://github.com/proconnect-gouv/proconnect-espace-partenaires/commit/a037e8b)).
- Ajout de documentation sur les scopes des rôles ([#331](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/331)).
- Mention de l'organisation et du SIRET professionnel ajoutée ([#330](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/330)).
- Clarification dans la documentation que les claims utilisateur sont retournés via l'endpoint `/user-info` ([#322](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/322)).
- Ajout d'une section de configuration MFA pour le guide LemonLDAP::NG ([#316](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/316)).

### Évolutions techniques
- Renommage de la base de données MongoDB en `corev2` et de l'utilisateur en `proconnect-app-api-partner` ([#337](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/337)).
- Correction d'un problème de configuration du serveur web UUV dans les tests E2E et résolution d'un problème d'assertion de chargement instable ([f2c4440](https://github.com/proconnect-gouv/proconnect-espace-partenaires/commit/f2c4440)).
- Rétrogradation d'une mise à jour de `nodemailer` qui causait des problèmes ([#335](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/335)).

### Autres changements
- Correction d'une faute de frappe ([#340](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/340)).
- Mises à jour de dépendances (axios, fast-xml-builder, typescript, next, postcss, uuv/playwright) ont été effectuées.
