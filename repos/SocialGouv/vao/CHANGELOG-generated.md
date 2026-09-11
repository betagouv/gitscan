## Changelog : vao (30 derniers jours, au 10 septembre 2026)

### Résumé
Ce mois a été marqué par une modernisation majeure de l'infrastructure technique et l'avancement du nouveau module dédié à l'hébergement. Les utilisateurs bénéficieront d'une gestion des agréments plus fiable grâce à de nombreuses corrections sur les processus de validation, de renouvellement et de communication par email.

### Évolutions fonctionnelles
- **Module Hébergement** : Migration du module [#1521](https://github.com/SocialGouv/vao/issues/1521) et intégration de la création d'hébergements dans le tunnel de saisie [#1535](https://github.com/SocialGouv/vao/issues/1535).
- **Gestion des agréments** : 
    - Corrections sur la validation DREETS pour les RGAA [#1526](https://github.com/SocialGouv/vao/issues/1526) et la création d'organismes [#1512](https://github.com/SocialGouv/vao/issues/1512).
    - Amélioration du processus de renouvellement pour les OVA secondaires [#1520](https://github.com/SocialGouv/vao/issues/1520).
    - Fiabilisation des données : exclusion des agréments supprimés lors des récupérations [#1530](https://github.com/SocialGouv/vao/issues/1530) et correction des contrôles d'âge et de déficience [#1514](https://github.com/SocialGouv/vao/issues/1514).
    - Ajout de la possibilité de supprimer un agrément directement depuis le formulaire d'organisme [#1507](https://github.com/SocialGouv/vao/issues/1507).
- **Expérience utilisateur et communication** :
    - Correction de la visibilité des comptes OVA dans le back-office [#1513](https://github.com/SocialGouv/vao/issues/1513).
    - Amélioration des emails : correction des liens et de la formulation des messages de refus [#1523](https://github.com/SocialGouv/vao/issues/1523).
    - Correction de la gestion des bilans de séjour (suppression et modification) [#1516](https://github.com/SocialGouv/vao/issues/1516).

### Évolutions techniques
- **Framework et Architecture** : 
    - Migration majeure vers Nuxt v4 [#1544](https://github.com/SocialGouv/vao/issues/1544).
    - Refonte de l'architecture des compétences IA [#1534](https://github.com/SocialGouv/vao/issues/1534).
    - Mise en place de *feature flags* pour le déploiement progressif du module hébergement [#1533](https://github.com/SocialGouv/vao/issues/1533).
- **Infrastructure et Maintenance** :
    - Mise à jour de l'environnement vers Node 24 [#1549](https://github.com/SocialGouv/vao/issues/1549).
    - Mise à jour de la bibliothèque cartographique MapLibre-GL en version 5.
    - Amélioration de la stabilité via la correction des tests de bout en bout (E2E) et le nettoyage de la duplication de code (Sonar).
    - Correction du reset du store lors de la déconnexion pour garantir la sécurité des données [#1517](https://github.com/SocialGouv/vao/issues/1517).

### Autres changements
- Configuration de l'authentification (basicauth) pour l'outil de test de mail Maildev [#1541](https://github.com/SocialGouv/vao/issues/1541).
