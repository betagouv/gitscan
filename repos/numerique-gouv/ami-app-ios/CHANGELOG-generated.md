## Changelog : ami-app-ios (30 derniers jours, au 26 août 2026)

### Résumé
Ce mois a été marqué par un renforcement significatif de la sécurité et de la stabilité de l'application. Les efforts se sont concentrés sur la sécurisation du stockage des données locales (via la biométrie et le chiffrement), l'amélioration de l'expérience d'authentification avec le support des Passkeys dans les vues web, et une refonte profonde de la structure de test et de configuration du projet pour garantir une meilleure qualité de code.

### Évolutions fonctionnelles
- **Support des Passkeys :** Configuration des WebViews pour permettre l'utilisation des Passkeys, facilitant ainsi l'authentification sécurisée ([#150](https://github.com/numerique-gouv/ami-app-ios/pull/150)).
- **Sécurité biométrique :** Introduction de l'authentification par FaceID pour protéger l'accès aux données sensibles stockées sur l'appareil.
- **Identification de l'appareil :** Mise en place d'un identifiant de terminal (Device ID) stable pour améliorer la reconnaissance du dispositif.
- **Gestion fine de la confidentialité :** Implémentation de différents niveaux de sécurité pour le stockage local (privé, chiffré et authentifié).

### Évolutions techniques
- **Architecture de stockage :** Implémentation d'une nouvelle couche de données (`LocalStorage`) utilisant le Keychain et UserDefaults, avec une gestion asynchrone et une meilleure gestion des erreurs.
- **Optimisation des WebViews :** Refonte du mécanisme de chargement des pages initiales et de l'injection de scripts natifs pour une communication plus fluide entre l'application et le contenu web.
- **Intégration du Design System :** Mise à jour vers la version 0.2 de l'**Ami Design System** pour l'utilisation des couleurs officielles et des composants de boutons (DsfrButtonStyle).
- **Qualité et Tests :** 
    - Refonte de la stratégie de tests unitaires en supprimant la dépendance à Sourcery au profit de tests plus simples et directs.
    - Correction de nombreux avertissements de compilation et de linter.
- **Gestion de la configuration et des secrets :** 
    - Automatisation de la génération des secrets via un nouveau build phase `generate-secrets`.
    - Amélioration de la gestion du projet via XcodeGen ([#148](https://github.com/numerique-gouv/ami-app-ios/pull/148)) et nettoyage des fichiers d'entitlements.

### Autres changements
- **Documentation :** Mise à jour de la documentation technique, notamment sur l'utilisation des fichiers d'environnement (`.env.example`) et le fonctionnement du stockage local.
- **Nettoyage du projet :** Suppression de composants inutilisés (Tile), de ressources en double (AppIcon) et optimisation des fichiers `.gitignore`.
