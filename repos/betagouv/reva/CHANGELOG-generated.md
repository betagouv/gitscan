## Changelog : reva (30 derniers jours, au 09 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'expérience utilisateur, notamment pour les administrateurs et les candidats. Des fonctionnalités ont été ajoutées pour la gestion des organismes certificateurs, la gestion des compétences, et l'accompagnement des candidatures en voie de dématérialisation. Des corrections et optimisations ont également été apportées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Ajout de la possibilité de visualiser les organismes de France Compétences certificateurs sur la page de structure de certification ([0c4eb03](https://github.com/betagouv/reva/commit/0c4eb03)).
- Amélioration de l'interface utilisateur et de l'expérience utilisateur des pages de candidature pour la dématérialisation autonome (ajout de sections pour les pièces jointes, les prérequis, les compétences, les formations et les expériences) ([bd1b73f](https://github.com/betagouv/reva/commit/bd1b73f), [3bc1440](https://github.com/betagouv/reva/commit/3bc1440), [1cc1e9c](https://github.com/betagouv/reva/commit/1cc1e9c), [77194b2](https://github.com/betagouv/reva/commit/77194b2), [2356557](https://github.com/betagouv/reva/commit/2356557), [33ef046](https://github.com/betagouv/reva/commit/33ef046), [42101e6](https://github.com/betagouv/reva/commit/42101e6)).
- Possibilité de mettre à jour l'organisme certificateur directement depuis la page de résumé de la candidature ([f033a33](https://github.com/betagouv/reva/commit/f033a33), [233ad6c](https://github.com/betagouv/reva/commit/233ad6c)).
- Ajout d'une page de sélection d'organisme certificateur pour faciliter la gestion ([c8a6d55](https://github.com/betagouv/reva/commit/c8a6d55)).
- Amélioration de l'affichage des informations sur les organismes certificateurs dans l'interface administrateur ([46844d1](https://github.com/betagouv/reva/commit/46844d1)).
- Ajout d'un système de vérification par email (OTP) pour la connexion, en alternative à l'authentification à deux facteurs ([220608e](https://github.com/betagouv/reva/commit/220608e), [1d524f4](https://github.com/betagouv/reva/commit/1d524f4), [4b3bfe8](https://github.com/betagouv/reva/commit/4b3bfe8)).
- Mise à jour de l'adresse email de contact sur la page CGU ([0738191](https://github.com/betagouv/reva/commit/0738191)).
- Possibilité d'activer l'inscription par mot de passe ([b346fd7](https://github.com/betagouv/reva/commit/b346fd7)).

### Évolutions techniques
- Refactorisation de composants dans l'interface administrateur pour supprimer des anti-patterns liés à l'utilisation de `setState` dans `useEffect` ([054b9dc](https://github.com/betagouv/reva/commit/054b9dc), [c08ff4e](https://github.com/betagouv/reva/commit/c08ff4e)).
- Suppression de code obsolète lié à l'audit des événements et à la table `audit_event` ([9d8b0ec](https://github.com/betagouv/reva/commit/9d8b0ec), [dd2230c](https://github.com/betagouv/reva/commit/dd2230c)).
- Suppression de l'outil Produkly ([63c391d](https://github.com/betagouv/reva/commit/63c391d)).
- Mise à jour de la version de Keycloak ([7a3e5bb](https://github.com/betagouv/reva/commit/7a3e5bb)).
- Optimisation de la récupération des données des organismes certificateurs ([0dd07d7](https://github.com/betagouv/reva/commit/0dd07d7)).
- Amélioration de la performance de la mise à jour des informations des organismes certificateurs ([9bfed1a](https://github.com/betagouv/reva/commit/9bfed1a)).
- Suppression de la page de sélection d'organisme certificateur dans l'interface administrateur ([9bb8a58](https://github.com/betagouv/reva/commit/9bb8a58)).
- Mise à jour des dépendances (js-yaml, vite, shell-quote, etc.)

### Autres changements
- Ajout de tests unitaires et d'intégration pour améliorer la couverture du code ([2386f0c](https://github.com/betagouv/reva/commit/2386f0c)).
- Correction de bugs mineurs dans l'interface utilisateur et le comportement de certaines fonctionnalités ([3f14e39](https://github.com/betagouv/reva/commit/3f14e39), [98133b0](https://github.com/betagouv/reva/commit/98133b0), [41e7d5e](https://github.com/betagouv/reva/commit/41e7d5e)).
- Amélioration de la gestion des erreurs et des messages d'alerte ([6ce5827](https://github.com/betagouv/reva/commit/6ce5827)).
- Mise à jour de la documentation et des commentaires du code.
- Correction de problèmes liés à la gestion des sessions SSO.
- Amélioration de la gestion des droits d'accès et des rôles.
- Ajout de logs pour faciliter le débogage et le suivi des opérations.
- Correction de problèmes de compatibilité avec certains navigateurs.
