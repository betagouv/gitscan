## Changelog : infra-apps (30 derniers jours, au 2026-07-13)

### Résumé
Ce changelog couvre les 30 derniers jours et met en évidence des améliorations significatives apportées à l'infrastructure, notamment autour de l'outil Iterion (amélioration des performances, ajout de fonctionnalités d'autoscaling et de sécurité) et de l'intégration de Buildkit (renforcement de la sécurité et amélioration de la gestion des environnements de production). Des corrections et des mises à jour ont également été apportées à divers composants pour améliorer la stabilité et la fonctionnalité globale.

### Évolutions fonctionnelles
- **Iterion:** Activation du mode "sandbox" pour les runners Kubernetes, renforçant ainsi la sécurité et l'isolation des exécutions. [#40, #41, #42, #43, #45]
- **Iterion:** Ajout de l'authentification via GitHub SSO sur les environnements preprod et prod, permettant une gestion des accès plus sécurisée et simplifiée. [#40, #41, #43]
- **Buildkit:** Ajout d'un fournisseur OIDC Forgejo pour l'authentification, améliorant la sécurité d'accès. [#48]
- **Buildkit:** Configuration de l'environnement de production (ovh-prod) avec des mesures de sécurité renforcées (TLS Ingress, hard-pin, limitation du gateway). [#47]
- **Charon:** Autorisation du `redirect_uri` pour l'environnement preprod egapro Atlas v2.

### Évolutions techniques
- **Iterion:** Amélioration des performances et de la stabilité en augmentant les limites de mémoire pour les runners et en ajustant la concurrence.
- **Iterion:** Implémentation de l'autoscaling KEDA pour les runners, permettant une gestion dynamique des ressources en fonction de la charge.
- **Iterion:** Mise à jour du chart Iterion vers les versions 0.37.2, 0.35.0, 0.34.0, 0.33.0, 0.32.0, 0.23.2, 0.23.0, 0.22.0, 0.21.0, 0.17.2, 0.17.1 et 0.16.1 avec diverses corrections et améliorations.
- **Buildkit:** Mise à jour de l'opérateur Buildkit vers les versions v0.12.0, v0.10.0 et v0.9.0.
- **Buildkit:** Configuration de l'accès S3 pour le cache "cold" en production.
- **Buildkit:** Correction de la capture de la configuration du gateway en production.
- **Kata:** Déploiement de Kata dans l'espace de noms `buildkit-system` et activation de `virtiofsd xattr` pour améliorer la compatibilité avec Buildkit.
- Suppression d'une configuration temporaire pour les tests E2E.

### Autres changements
- Documentation mise à jour et configurations ajustées pour améliorer la gestion des environnements de production et de preproduction.
- Nettoyage et refactoring du code pour améliorer la lisibilité et la maintenabilité.
- Ajustements de configuration pour améliorer la surveillance et la gestion des ressources.
- Correction de bugs mineurs et améliorations de la stabilité générale.
