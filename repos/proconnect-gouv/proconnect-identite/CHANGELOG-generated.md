## Changelog : proconnect-identite (30 derniers jours, au 16 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité, la modernisation de l'interface utilisateur pour l'authentification multi-facteurs (MFA), et l'amélioration de la robustesse des tests et de l'infrastructure. Des efforts ont également été faits pour simplifier la publication de certains modules et standardiser les valeurs d'authentification.

### Évolutions fonctionnelles
- **Authentification Multi-Facteurs (MFA):** Nouvelle interface utilisateur pour le choix des méthodes MFA [#2025](https://github.com/proconnect-gouv/proconnect-identite/pulls/2025).
- **Annuaire:** Synchronisation des données de l'annuaire avec l'API réelle pour les tests e2e [#2035](https://github.com/proconnect-gouv/proconnect-identite/pulls/2035).
- **AMR (Authentication Method Reference):** Mise à jour de la définition de l'AMR `mail` et remplacement d'une valeur TOTP non standard [#2012](https://github.com/proconnect-gouv/proconnect-identite/pulls/2012).
- **Authentification Client:** Restriction des méthodes d'authentification au niveau du point de terminaison des tokens [#2003](https://github.com/proconnect-gouv/proconnect-identite/pulls/2003).

### Évolutions techniques
- **Sécurité:** Suppression de `unsafe-inline` de la Content Security Policy pour renforcer la sécurité [#2026](https://github.com/proconnect-gouv/proconnect-identite/pulls/2026).
- **Tests:**
    - Mock de l'API `api-lannuaire.service-public.fr` pour les tests e2e [#2029](https://github.com/proconnect-gouv/proconnect-identite/pulls/2029).
    - Vérification quotidienne de la cohérence des données mockées avec l'API réelle.
    - Correction d'un bug dans la copie anonymisée de la table des authentificateurs [#2027](https://github.com/proconnect-gouv/proconnect-identite/pulls/2027).
- **Infrastructure:**
    - Publication du module `@proconnect-gouv/proconnect.email` en tant que package standalone [#2017](https://github.com/proconnect-gouv/proconnect-identite/pulls/2017).
    - Mise à jour de l'image `proconnect-test-client` et utilisation des variables d'environnement par défaut [#2011](https://github.com/proconnect-gouv/proconnect-identite/pulls/2011).
- **Refactoring:** Suppression du widget de chat Crisp [#2014](https://github.com/proconnect-gouv/proconnect-identite/pulls/2014).

### Autres changements
- Correction d'un bug lié à la clé de correspondance pour la vérification du `given_name` [#2015](https://github.com/proconnect-gouv/proconnect-identite/pulls/2015).
- Mise à jour de la page FranceConnect [#2013](https://github.com/proconnect-gouv/proconnect-identite/pulls/2013).
- Revert d'une mise à jour Vite qui causait des problèmes [#2024](https://github.com/proconnect-gouv/proconnect-identite/pulls/2024).
- Revert d'un commit accidentellement poussé sur `main` [#2026](https://github.com/proconnect-gouv/proconnect-identite/pulls/2026).
- Amélioration de la lisibilité du code (prettify) [#2026](https://github.com/proconnect-gouv/proconnect-identite/pulls/2026).
