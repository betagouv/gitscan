## Changelog : proconnect-espace-partenaires (30 derniers jours, au 01/10/2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur le renforcement de la sécurité des accès et l'amélioration de l'accompagnement des partenaires via une mise à jour majeure de la documentation technique et métier.

### Évolutions fonctionnelles
- Amélioration de la sécurité des comptes avec la gestion du MFA et l'envoi de codes OTP par e-mail [#470](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/470).

### Évolutions techniques
- Optimisation des mécanismes d'authentification via Keycloak [#444](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/444) et Entra ID [#448](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/448).
- Amélioration de la fiabilité des tests avec l'intégration d'un fournisseur ProConnect simulé (mock) pour la suite de tests de bout en bout (E2E) [#453](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/453).

### Autres changements
- **Documentation technique et métier** :
    - Ajout de sections dédiées à la sécurité, aux aspects métier [#469](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/469) et aux exceptions RIE pour les fournisseurs de services (FS) [#452](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/452).
    - Harmonisation des pages eIDAS (FI/FS) [#471](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/471) et clarification de la conformité MFA [#473](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/473).
    - Documentation des messages d'erreur liés aux rôles [#464](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/464).
- **Support et navigation** :
    - Mise à jour des informations de contact (e-mail de support [#467](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/467) et canal Tchap [#466](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/466)).
    - Nettoyage de l'interface documentaire (retrait de la sidebar [#468](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/468)) et correction de liens (DSFR [#462](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/462), référentiel IP).
