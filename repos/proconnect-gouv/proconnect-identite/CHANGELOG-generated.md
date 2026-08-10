## Changelog : proconnect-identite (30 derniers jours, au 06/08/2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de l'expérience utilisateur lors de l'authentification multi-facteurs (MFA) et la clarification des communications par email. Le projet a également bénéficié d'un nettoyage technique important, incluant la suppression de fonctionnalités obsolètes et un renforcement de la sécurité.

### Évolutions fonctionnelles
- **Amélioration du parcours MFA** : Ajout d'un assistant dédié dans les sections de connexion et de gestion du compte, incluant un bouton de redémarrage du processus pour faciliter la navigation en cas d'erreur [#2044](https://github.com/proconnect-gouv/proconnect-identite/pull/2044).
- **Optimisation des emails de sécurité** : Création d'un modèle d'email dédié pour les codes de validation (OTP) [#2066](https://github.com/proconnect-gouv/proconnect-identite/pull/2066) et corrections de la syntaxe et de la formulation sur les pages et modèles de vérification d'adresse email [#2045](https://github.com/proconnect-gouv/proconnect-identite/issues/2045) [#2048](https://github.com/proconnect-gouv/proconnect-identite/pull/2048) [#2056](https://github.com/proconnect-gouv/proconnect-identite/issues/2056).
- **Nettoyage des contacts** : Suppression de l'adresse email `moncomptepro` qui n'est plus utilisée.

### Évolutions techniques
- **Sécurité et architecture** : Renforcement de la politique de sécurité par la suppression de `unsafe-inline` [#2026](https://github.com/proconnect-gouv/proconnect-identite/pull/2026) et refactorisation de la gestion des droits d'accès via une chaîne récursive pour le garde de connexion (`userSignInRequirementsGuard`) [#2059](https://github.com/proconnect-gouv/proconnect-identite/pull/2059).
- **Maintenance de l'API et des données** : Suppression du support du scope `organisations` [#2055](https://github.com/proconnect-gouv/proconnect-identite/pull/2055), mise à jour de l'algorithme de jointure des communes [#2039](https://github.com/proconnect-gouv/proconnect-identite/pull/2039) et synchronisation des données de test (fixtures) avec l'API réelle [#2035](https://github.com/proconnect-gouv/proconnect-identite/issues/2035).
- **Optimisations diverses** : Correction d'un bug sur la table des authentificateurs anonymisés [#2027](https://github.com/proconnect-gouv/proconnect-identite/issues/2027) et suppression de paramètres inutilisés dans les modèles d'emails [#2057](https://github.com/proconnect-gouv/proconnect-identite/pull/2057).
