## Changelog : zacharie (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, l'application Zacharie a bénéficié d'une série d'améliorations axées sur l'expérience utilisateur, notamment dans les flux de création et de consultation des fiches, ainsi que sur la sécurité et la gestion des accès. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et la performance de l'application. L'authentification via token a été implémentée pour les appels API.

### Évolutions fonctionnelles
- Ajout d'une liste de lésions pour une meilleure description des animaux. [#331](https://github.com/betagouv/zacharie/issues/331)
- Implémentation d'un token bearer pour l'authentification des appels API. [#336](https://github.com/betagouv/zacharie/issues/336)
- Amélioration de l'interface utilisateur pour la consultation des carcasses, même avec un seul groupe. [#287](https://github.com/betagouv/zacharie/issues/287)
- Ajout d'en-têtes spécifiques pour les interfaces SVI et FEI. [#323](https://github.com/betagouv/zacharie/issues/323), [#319](https://github.com/betagouv/zacharie/issues/319)
- Amélioration du flux de création de fiches. [#281](https://github.com/betagouv/zacharie/issues/281)
- Ajout d'un bouton de connexion pour les utilisateurs administrateurs.
- Ajout de la possibilité de se connecter en tant qu'utilisateur SVI. [#296](https://github.com/betagouv/zacharie/issues/296)
- Amélioration de l'interface utilisateur pour l'affichage des fiches envoyées et des erreurs d'examinateur. [#306](https://github.com/betagouv/zacharie/issues/306), [#305](https://github.com/betagouv/zacharie/issues/305), [#301](https://github.com/betagouv/zacharie/issues/301)
- Correction de l'affichage de la barre latérale pour les chasseurs. [#324](https://github.com/betagouv/zacharie/issues/324)
- Correction du calcul du BPH. [#326](https://github.com/betagouv/zacharie/issues/326)
- Correction du score BPH. [#318](https://github.com/betagouv/zacharie/issues/318)

### Évolutions techniques
- Refonte des routeurs pour les chasseurs et l'administration, incluant la connexion.
- Mise en place d'un nouveau routeur collecteur.
- Amélioration de la gestion des erreurs et des codes de statut HTTP (correction de 404 et 500). [#316](https://github.com/betagouv/zacharie/issues/316)
- Optimisation des images.
- Ajout de tests E2E. [#315](https://github.com/betagouv/zacharie/issues/315)
- Mise à jour des dépendances pour corriger des vulnérabilités de sécurité. [#280](https://github.com/betagouv/zacharie/issues/280)
- Amélioration du script de build. [#300](https://github.com/betagouv/zacharie/issues/300)
- Refactoring des routeurs. [#295](https://github.com/betagouv/zacharie/issues/295)
- Utilisation de `npm ci` pour une installation plus fiable des dépendances. [#285](https://github.com/betagouv/zacharie/issues/285)
- Ajout de `prettier` pour formater le code. [#320](https://github.com/betagouv/zacharie/issues/320)

### Autres changements
- Correction de divers problèmes d'interface utilisateur (UI) et d'expérience utilisateur (UX).
- Correction de bugs mineurs et améliorations de la qualité du code.
- Suppression d'une image volumineuse.
- Désactivation de Claude.
- Correction du chemin initial pour l'application Expo.
- Ajout d'un fix pour le chemin initial.
- Ajout d'un fix pour l'URL initiale d'Expo.
- Correction d'un problème d'enum BPH.
- Ajout d'un fix pour le scroll-to-top de la navbar.
- Correction du wording.
- Correction de la modification de la raison sociale.
- Ajout de security headers. [#278](https://github.com/betagouv/zacharie/issues/278)
- Correction du filtre multiselect. [#292](https://github.com/betagouv/zacharie/issues/292)
- Correction du filtre responsive. [#289](https://github.com/betagouv/zacharie/issues/289)
- Correction du flow d'ajout de carcasse. [#284](https://github.com/betagouv/zacharie/issues/284)
- Correction de l'invitation. [#309](https://github.com/betagouv/zacharie/issues/309)
- Ajout de logs plus clairs.
- Correction du chemin vers /fei-carcasse.
