## Changelog : potentiel (30 derniers jours, au 14 septembre 2026)

### Résumé
Ce mois a été marqué par l'intégration majeure des versions 3.87 et 3.88. Les efforts se sont concentrés sur l'amélioration de la précision des données (notamment sur les dossiers de raccordement et les puissances), le renforcement de la sécurité (chiffrement des identifiants) et l'optimisation de l'expérience utilisateur via des améliorations d'accessibilité et de l'interface visuelle.

### Évolutions fonctionnelles
- **Gestion des projets et données métier** :
    - Amélioration de la gestion des puissances avec l'application de règles sur la puissance maximale par famille et le volume réservé [#4522](https://github.com/MTES-MCT/potentiel/issues/4522).
    - Mise à jour des processus d'importation des coordonnées depuis la DN [#4520](https://github.com/MTES-MCT/potentiel/issues/4520) et des règles CSV d'instruction [#4527](https://github.com/MTES-MCT/potentiel/issues/4527).
    - Ajout de nouveaux fournisseurs "Sol" importables et modifiables [#4564](https://github.com/MTES-MCT/potentiel/issues/4564).
    - Possibilité pour l'administration de corriger l'identifiant d'un projet même en phase d'abandon ou achevé [#4547](https://github.com/MTES-MCT/potentiel/issues/4547).
    - Gestion améliorée de l'historique d'abandon avec une valeur par défaut pour les premières candidatures [#4567](https://github.com/MTES-MCT/potentiel/issues/4567).
- **Interface et Expérience Utilisateur** :
    - Amélioration de l'accessibilité, notamment pour les lecteurs d'écran [#4578](https://github.com/MTES-MCT/potentiel/issues/4578) et correction de l'affichage lors d'un zoom à 200% [#4550](https://github.com/MTES-MCT/potentiel/issues/4550).
    - Ajout de badges visuels pour le raccordement, les lauréats et l'environnement de non-production [#4565](https://github.com/MTES-MCT/potentiel/issues/4565), [#4546](https://github.com/MTES-MCT/potentiel/issues/4546), [#4563](https://github.com/MTES-MCT/potentiel/issues/4563).
    - Optimisation de la recherche et de la navigation (bouton de retour sur les pages lauréats [#4543](https://github.com/MTES-MCT/potentiel/issues/4543)).
- **Statistiques, Documents et Exports** :
    - Mise à jour et ajout de statistiques publiques pour une meilleure visibilité des données [#4575](https://github.com/MTES-MCT/potentiel/issues/4575), [#4512](https://github.com/MTES-MCT/potentiel/issues/4512).
    - Amélioration des exports (affichage "N/A" pour les valeurs non définies) [#4579](https://github.com/MTES-MCT/potentiel/issues/4579).
    - Mise à jour des courriers de désignation [#4585](https://github.com/MTES-MCT/potentiel/issues/4585) et disponibilité de l'attestation d'actionnariat dans les documents projet [#4540](https://github.com/MTES-MCT/potentiel/issues/4540).
- **Permissions et Accès** :
    - Affinement des droits d'accès, notamment pour permettre aux cocontractants de consulter le détail des changements de puissance [#4590](https://github.com/MTES-MCT/potentiel/issues/4590) et de limiter la modification des gestionnaires selon le contexte [#4589](https://github.com/MTES-MCT/potentiel/issues/4589).

### Évolutions techniques
- **Sécurité et Authentification** :
    - Implémentation d'un tag d'authentification pour le chiffrement de l'ID projet [#4588](https://github.com/MTES-MCT/potentiel/issues/4588).
    - Mise à jour de Keycloak (v26.7.2) [#4551](https://github.com/MTES-MCT/potentiel/issues/4551) et correction de vulnérabilités sur plusieurs packages [#4568](https://github.com/MTES-MCT/potentiel/issues/4568), [#4514](https://github.com/MTES-MCT/potentiel/issues/4514).
- **Infrastructure et Déploiement** :
    - Migration vers l'image officielle `quay.io/minio/minio` [#4591](https://github.com/MTES-MCT/potentiel/issues/4591).
    - Optimisations du processus de build et corrections liées au déploiement sur Scalingo [#4535](https://github.com/MTES-MCT/potentiel/issues/4535), [#4533](https://github.com/MTES-MCT/potentiel/issues/4533).
- **Architecture et Refactoring** :
    - Standardisation du type de fournisseur de stockage pour une meilleure cohérence du code [#4594](https://github.com/MTES-MCT/potentiel/issues/4594).
    - Refactoring de la page historique en composants helpers pour faciliter les tests unitaires [#4509](https://github.com/MTES-MCT/potentiel/issues/4509).
    - Intégration continue des releases 3.87 et 3.88.

### Autres changements
- **Design System** : Harmonisation des notifications en utilisant les composants DSFR (Notice au lieu de Alert) [#4513](https://github.com/MTES-MCT/potentiel/issues/4513).
- **Documentation** : Mise à jour du Storybook pour refléter les derniers composants [#4537](https://github.com/MTES-MCT/potentiel/issues/4537).
