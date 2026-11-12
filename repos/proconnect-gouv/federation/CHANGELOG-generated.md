## Changelog : federation (30 derniers jours, au 10 novembre 2026)

### Résumé
Ce mois-ci, le projet a franchi des étapes importantes avec le lancement du module de statistiques "Statisticat", l'amélioration de l'expérience d'authentification (demandes multi-appareils et support Entra ID) et une montée de version majeure de l'infrastructure vers Node.js 26. La sécurité et la clarté des messages d'erreur ont également été renforcées.

### Évolutions fonctionnelles
- Lancement du module de statistiques "Statisticat" [#1752](https://github.com/proconnect-gouv/federation/issues/1752)
- Mise en place des demandes d'authentification multi-appareils [#1717](https://github.com/proconnect-gouv/federation/issues/1717)
- Amélioration du mapping MFA pour Entra ID (eidas1-mfa) [#1746](https://github.com/proconnect-gouv/federation/issues/1746)
- Gestion enrichie des demandes XDA (approbation/rejet et interface visuelle) [#1727](https://github.com/proconnect-gouv/federation/issues/1727)
- Affichage de l'ID client sur la page de mise à jour des fournisseurs de services [#1790](https://github.com/proconnect-gouv/federation/issues/1790)
- Clarification des messages d'erreur lors de l'exclusion d'un fournisseur de services [#1848](https://github.com/proconnect-gouv/federation/issues/1848)
- Autorisation des URLs de rappel en `localhost` et `http` pour faciliter les tests de développement [#1753](https://github.com/proconnect-gouv/federation/issues/1753)

### Évolutions techniques
- **Infrastructure & DevOps** :
    - Migration de l'environnement vers Node.js 26 LTS [#1853](https://github.com/proconnect-gouv/federation/issues/1853)
    - Auto-hébergement du gestionnaire de tags Matomo [#1792](https://github.com/proconnect-gouv/federation/issues/1792)
    - Mise à jour des packages internes ProConnect [#1854](https://github.com/proconnect-gouv/federation/issues/1854)
- **Sécurité** :
    - Renforcement de la validation des noms de fournisseurs (SP/IdP) via une regex sécurisée [#1830](https://github.com/proconnect-gouv/federation/issues/1830)
    - Liaison de la session cœur à l'interaction OIDC lors de la vérification [#1828](https://github.com/proconnect-gouv/federation/issues/1828)
    - Suppression des scopes "roles" inutilisés pour les fournisseurs de services [#1687](https://github.com/proconnect-gouv/federation/issues/1687)
- **Architecture & Qualité** :
    - Renommage du composant `csmr-rie` en `hybridge` [#1755](https://github.com/proconnect-gouv/federation/issues/1755)
    - Amélioration de la traçabilité avec l'ajout du claim "roles" dans les logs [#1859](https://github.com/proconnect-gouv/federation/issues/1859)
    - Optimisation du transfert de données CSV pour le module de statistiques
    - Mise à jour de la suite de tests (Cypress et Cucumber) [#1459](https://github.com/proconnect-gouv/federation/issues/1459)

### Autres changements
- **Documentation** :
    - Correction de coquilles dans la documentation cryptographique [#1858](https://github.com/proconnect-gouv/federation/issues/1858)
    - Mise à jour des guides de contribution et des modèles de Pull Request [#1750](https://github.com/proconnect-gouv/federation/issues/1750)
- **Nettoyage** :
    - Suppression de propriétés inutilisées dans la configuration des fournisseurs d'identité (URLs de redirection, etc.) [#1756](https://github.com/proconnect-gouv/federation/issues/1756)
