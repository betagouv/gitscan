## Changelog : oots-france (30 derniers jours, au 13 août 2026)

### Résumé
Le projet a franchi une étape majeure avec une réécriture complète de son architecture vers Ruby on Rails. Cette transition améliore la robustesse du système, simplifie grandement l'installation pour les développeurs et introduit une interface d'administration conforme au design système de l'État (DSFR). Les capacités de test ont également été renforcées pour garantir une meilleure conformité aux standards européens.

### Évolutions fonctionnelles
- **Nouvel espace d'administration** : Mise en place d'une interface pour le suivi des échanges et des tâches de fond (jobs) [#77](https://github.com/numerique-gouv/oots-france/pull/77).
- **Interface utilisateur modernisée** : Intégration du Design System de l'État (DSFR) pour l'ensemble des rendus de l'application.
- **Conformité accrue** : Renforcement de la validation des messages via des règles Schematron basées sur les TDD v2.0.
- **Interopérabilité** : Introduction de la capacité à utiliser des plugins REST pour les échanges.

### Évolutions techniques
- **Migration architecturale** : Transition majeure de l'application vers un framework Ruby on Rails.
- **Expérience développeur (DevEx)** : 
    - Simplification de l'installation locale via une commande unique `make setup` [#73](https://github.com/numerique-gouv/oots-france/pull/73).
    - Amélioration de la gestion des environnements de travail avec le support des *worktrees* et des ports paramétrables [#72](https://github.com/numerique-gouv/oots-france/pull/72).
- **Tests et Qualité** :
    - Mise en place de tests de bout en bout (E2E) utilisant une instance réelle de Domibus et les services communs réels.
    - Automatisation des tests E2E au sein de la chaîne d'intégration continue.
- **Infrastructure et Dépendances** :
    - Mise à jour majeure de Domibus vers la version 5.2.
    - Montée de version de l'environnement Node.js.

### Autres changements
- **Documentation** : Refonte complète de la documentation technique, du guide d'onboarding et du README.
- **Glossaire** : Création d'un glossaire unique pour centraliser et clarifier le vocabulaire spécifique à OOTS [#76](https://github.com/numerique-gouv/oots-france/pull/76).
- **Standardisation** : Renommage des scripts de développement en anglais pour une meilleure cohérence.
