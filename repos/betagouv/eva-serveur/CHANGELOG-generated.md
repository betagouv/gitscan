## Changelog : eva-serveur (30 derniers jours, au 24 juin 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives à l'import de questions, à la restitution des évaluations Evapro, et à l'expérience utilisateur globale. Des corrections de bugs ont été implémentées pour éviter des crashes et améliorer la stabilité de l'application. L'interface utilisateur a été modernisée avec l'utilisation de composants DSFR et des améliorations d'accessibilité.

### Évolutions fonctionnelles
- Ajout de la navigation vers la liste des campagnes depuis un compte utilisateur. [#5d8c9ec](https://github.com/betagouv/eva-serveur/commit/5d8c9ec)
- Amélioration de la gestion des réponses multiples lors de la restitution d'une évaluation Evapro. [#542f436](https://github.com/betagouv/eva-serveur/commit/542f436)
- Correction de l'affichage de la durée estimée d'une évaluation Evapro. [#bf30d45](https://github.com/betagouv/eva-serveur/commit/bf30d45)
- Possibilité d'importer des questions avec des noms techniques de choix existants. [#5aeb734](https://github.com/betagouv/eva-serveur/commit/5aeb734)
- Ajout d'accès démos depuis l'accueil. [#1a2e18e](https://github.com/betagouv/eva-serveur/commit/1a2e18e)
- Ajout des URL officielles pour les compétences transversales. [#e3cb723](https://github.com/betagouv/eva-serveur/commit/e3cb723)
- Restauration des fonctions d'autocomplétion pour la recherche de compte et de campagne. [#db01108](https://github.com/betagouv/eva-serveur/commit/db01108), [#12743ab](https://github.com/betagouv/eva-serveur/commit/12743ab)

### Évolutions techniques
- Mise à jour de plusieurs dépendances, incluant Puma en version 7.2 et image_processing en 2.0.2 (nécessitant l'installation de ruby-vips). [#4d8d2b8](https://github.com/betagouv/eva-serveur/commit/4d8d2b8), [#dd0df2c](https://github.com/betagouv/eva-serveur/commit/dd0df2c)
- Refonte des cartes de choix d'usage avec des composants DSFR. [#32fc06d](https://github.com/betagouv/eva-serveur/commit/32fc06d)
- Utilisation de composants DSFR pour le bouton de création de compte et le champ de mot de passe. [#194e21a](https://github.com/betagouv/eva-serveur/commit/194e21a)
- Introduction d'un layout UI Kit pour uniformiser l'interface. [#571c940](https://github.com/betagouv/eva-serveur/commit/571c940)
- Génération du schéma de la base de données au format Mermaid. [#58be733](https://github.com/betagouv/eva-serveur/commit/58be733)
- Suppression du code custom qui empêchait l'accordéon de la numératie de s'ouvrir. [#7dd8952](https://github.com/betagouv/eva-serveur/commit/7dd8952)
- Simplification du code lié au calcul des risques et des coûts. [#dd4b64f](https://github.com/betagouv/eva-serveur/commit/dd4b64f), [#270666a](https://github.com/betagouv/eva-serveur/commit/270666a)

### Autres changements
- Correction de bugs mineurs liés à l'affichage et au comportement de l'interface utilisateur. [#98af57e](https://github.com/betagouv/eva-serveur/commit/98af57e), [#7ed07c1](https://github.com/betagouv/eva-serveur/commit/7ed07c1), [#3cdca00](https://github.com/betagouv/eva-serveur/commit/3cdca00), [#8184777](https://github.com/betagouv/eva-serveur/commit/8184777), [#75a5c08](https://github.com/betagouv/eva-serveur/commit/75a5c08), [#f53b8e2](https://github.com/betagouv/eva-serveur/commit/f53b8e2)
- Amélioration de la documentation et des tests. [#9bd7b00](https://github.com/betagouv/eva-serveur/commit/9bd7b00), [#234ffce](https://github.com/betagouv/eva-serveur/commit/234ffce)
- Suppression de code inutilisé. [#2b4d7b0](https://github.com/betagouv/eva-serveur/commit/2b4d7b0), [#39850c0](https://github.com/betagouv/eva-serveur/commit/39850c0), [#e85ec37](https://github.com/betagouv/eva-serveur/commit/e85ec37)
- Correction de problèmes de race condition à la connexion Pro-Connect. [#5d8c9ec](https://github.com/betagouv/eva-serveur/commit/5d8c9ec)
- Ajout d'une colonne Siret à la table des comptes. [#0955357](https://github.com/betagouv/eva-serveur/commit/0955357)
