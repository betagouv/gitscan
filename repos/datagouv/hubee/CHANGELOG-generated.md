## Changelog : hubee (30 derniers jours, au 07/08/2026)

### Résumé
Cette période a été marquée par une refonte majeure du système d'authentification pour intégrer nativement le protocole OIDC avec ProConnect. Le projet introduit également une gestion plus fine des profils d'agents et de leur rattachement aux organisations, tout en renforçant la sécurité des sessions et la clarté des messages d'erreur pour les utilisateurs.

### Évolutions fonctionnelles
- **Authentification et sécurité :**
    - Prise en charge de la double authentification (MFA) imposée par le fournisseur d'identité.
    - Exigence systématique d'un second facteur pour les comptes à privilèges.
    - Gestion des sessions par durée d'inactivité et durée absolue.
    - Amélioration de la clarté des erreurs : messages d'expiration, motifs d'erreur ProConnect et possibilité de proposer un recours en cas d'échec.
    - Possibilité de retenter une connexion avec un autre compte après un refus.
- **Gestion des agents et des organisations :**
    - Enrichissement des profils agents (rôle, fonction, civilité, téléphone au format international).
    - Nouveau mécanisme de rattachement des agents à une organisation avec validation du SIRET.
    - Affichage des informations d'organisation et de l'adresse lors des processus d'élévation de niveau.
- **Expérience utilisateur (Portail) :**
    - Refonte de l'en-tête pour inclure l'identité et la déconnexion.
    - Amélioration de la lisibilité des pages de refus et de déconnexion.

### Évolutions techniques
- **Refonte de l'authentification :**
    - Migration de la stratégie ProConnect vers une implémentation native OIDC (sortie d'OmniAuth).
    - Introduction des modèles `Agent` et `ProviderSession` pour une gestion robuste des identités et des sessions en base de données.
    - Chiffrement des jetons ProConnect au repos.
    - Mise en place d'un système de traçabilité et de rétention des décisions d'accès.
- **Sécurité et robustesse :**
    - Durcissement de la découverte OIDC avec mise en cache des clés (JWKS).
    - Amélioration de la résilience face aux indisponibilités du fournisseur d'identité.
    - Limitation du débit (rate limiting) sur les retours d'authentification.
    - Mise en conformité des logs au format `logfmt` pour le CSIRT.
- **Tests et CI/CD :**
    - Introduction de tests de bout en bout (E2E) dans de véritables navigateurs.
    - Renforcement de la couverture de tests sur le flux d'authentification.
    - Restriction de la CI GitHub aux analyses statiques et de sécurité.

### Autres changements
- Mise à jour de la documentation technique (couche d'authentification).
- Traduction en français des messages du framework.
- Filtrage des données sensibles dans les logs (codes d'autorisation, identifiants).
