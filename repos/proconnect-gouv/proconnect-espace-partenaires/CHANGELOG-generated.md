## Changelog : proconnect-espace-partenaires (30 derniers jours, au 10 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la documentation pour les partenaires, notamment concernant l'intégration avec eIDAS et les différents niveaux de sécurité. Des corrections et clarifications ont également été apportées concernant les erreurs et les informations relatives aux identifiants. Des mises à jour techniques ont été effectuées pour maintenir la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- **Documentation eIDAS:** Ajout de documentation détaillée concernant les normes eIDAS, les niveaux de sécurité (eidas1-mfa, eidas2) et les erreurs spécifiques (Y030031 redirect_uri mismatch) [#339, #352].
- **Documentation Fournisseurs de Service (FS) et Fournisseurs d'Identité (FI):** Restructuration et clarification des données fournies dans la documentation pour les FS et FI [#317, #355].
- **Documentation Organisation:** Ajout de documentation concernant l'organisation, incluant le label, le SIRET professionnel et les scopes de rôle [#323, #330, #331, #348].
- **Correction d'informations:** Mise à jour d'informations inexactes concernant les identifiants FI test [#346].
- **Clarification MFA Keycloak:** Ajout d'informations concernant l'intégration de l'authentification multi-facteur (MFA) avec Keycloak [#338].

### Évolutions techniques
- **Mise à jour des dépendances:** Mises à jour de plusieurs dépendances, notamment `proconnect-gouv/federation/api-partner`, `Playwright`, `TypeScript`, `nodemailer`, `axios`, `fast-xml-builder`, `picomatch`, `fast-uri`, `postcss` et `next` (les mises à jour de routine sont omises dans ce résumé).
- **Refactorisation MongoDB:** Renommage de la base de données MongoDB en `corev2` et de l'utilisateur en `proconnect-app-api-partner` [#337].
- **Correction E2E:** Correction de la configuration du serveur web UUV dans les tests E2E et résolution d'un problème d'assertion de chargement intermittent [#335].
- **Suppression d'IPs obsolètes:** Suppression d'anciennes adresses IP [#360].

### Autres changements
- **Documentation générale:** Améliorations et corrections mineures de la documentation générale [#353].
- **Linting:** Application du linter pour améliorer la qualité du code [#352].
- **Organisation de la documentation:** Déplacement du contenu eIDAS partagé vers un emplacement dédié dans les ressources [#350].
- **Typo:** Correction de fautes de frappe [#340, #354].
