## Changelog : federation (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a déployé une nouvelle interface utilisateur pour améliorer l'expérience utilisateur. Des corrections de bugs ont également été apportées, notamment pour l'affichage responsive et la gestion des erreurs. Des mises à jour de sécurité et des améliorations de l'infrastructure ont également été réalisées.

### Évolutions fonctionnelles
- Nouvelle interface utilisateur déployée [#802](https://github.com/proconnect-gouv/federation/pull/802).
- Amélioration de l'affichage responsive de l'interface utilisateur [#868](https://github.com/proconnect-gouv/federation/pull/868).
- Correction d'un bug empêchant le bouton de se désactiver correctement après une action [#962](https://github.com/proconnect-gouv/federation/issues/962).
- Suppression du message d'information concernant la nouvelle interface utilisateur, maintenant intégrée [#872](https://github.com/proconnect-gouv/federation/pull/872).
- Possibilité d'utiliser la complétion automatique sur les formulaires d'administration [#900](https://github.com/proconnect-gouv/federation/pull/900).

### Évolutions techniques
- Mise à jour de plusieurs dépendances : `ioredis`, `pg`, `express`, `mongoose`, `uuid`, `pino`, `jest-extended`, `eslint-plugin-prettier`, `systeminformation`, `dotenv`, `cryptography`, `ajv`, `jquery`, `prettier`, `typescript-eslint`, `eslint-plugin-eslint-comments`, `multiple-cucumber-html-reporter`, `commander`, `otpauth`, `docker/build-push-action`, `docker/setup-compose-action`, `actions/upload-artifact`, `actions/attest-build-provenance`, `actions/download-artifact`.
- Simplification de la configuration des assets et ajout de la favicon [#986](https://github.com/proconnect-gouv/federation/pull/986).
- Utilisation de la configuration par défaut de Prettier dans le projet `admin` [#974](https://github.com/proconnect-gouv/federation/pull/974).
- Mise à jour de la librairie `otplib` pour améliorer la sécurité [#911](https://github.com/proconnect-gouv/federation/pull/911).
- Mise à jour de la politique de sécurité et ajout d'un rapport de vulnérabilité [#884](https://github.com/proconnect-gouv/federation/pull/884).
- Passage au module ESNext [#855](https://github.com/proconnect-gouv/federation/pull/855).
- Ajout de tests Cypress pour l'environnement Kubernetes [#924](https://github.com/proconnect-gouv/federation/pull/924), [#963](https://github.com/proconnect-gouv/federation/pull/963).
- Correction d'un problème de crash du core en cas d'échec du proxy [#786](https://github.com/proconnect-gouv/federation/pull/786).

### Autres changements
- Ajout de tests unitaires pour Kubernetes.
- Mise à jour de la documentation de qualité.
- Nettoyage du code et suppression de fichiers inutiles.
- Correction d'un problème avec la configuration de Dependabot.
- Mise à jour de la configuration de CI/CD.
- Correction d'un warning du compilateur.
- Suppression du manifest web.
- Ajout de tests de réconciliation PCI pour Kubernetes.
- Suppression de directives Crisp inutiles.
- Mise à jour de la configuration pip pour pcdbapi.
- Déduplication du `yarn.lock` dans le projet `quality`.
- Ajout de tests pour l'exploitation en environnement k8s.
- Suppression de tests obsolètes.
