## Changelog : vao (30 derniers jours, au 11 septembre 2026)

### Résumé
Ce mois a été marqué par une étape importante avec l'introduction du nouveau module d'hébergement et son tunnel de création. Parallèlement, le projet a bénéficié d'une montée en version majeure de son infrastructure technique (Nuxt 4 et Node js 24) pour garantir la pérennité du système. De nombreuses corrections ont également été apportées pour fiabiliser la gestion des agréments et la qualité des communications par email.

### Évolutions fonctionnelles
- **Module Hébergement** : 
    - Mise en place du tunnel de création d'OVA pour l'hébergement ([#1535](https://github.com/SocialGouv/vao/issues/1535)).
    - Migration globale du module d'hébergement ([#1521](https://github.com/SocialGouv/vao/issues/1521)).
- **Gestion des agréments** :
    - Amélioration de la validation des demandes RGAA ([#1526](https://github.com/SocialGouv/vao/issues/1526), [#1518](https://github.com/SocialGouv/vao/issues/1518)).
    - Correction du processus de renouvellement pour les OVA secondaires ([#1522](https://github.com/SocialGouv/vao/issues/1522)).
    - Fiabilisation du filtrage (exclusion des agréments supprimés [#1530](https://github.com/SocialGouv/vao/issues/1530)) et des contrôles liés à l'âge et au handicap ([#1515](https://github.com/SocialGouv/vao/issues/1515)).
    - Correction de la logique de mise à jour des agréments au sein des organismes ([#1525](https://github.com/SocialGouv/vao/issues/1525)).
- **Communications et Expérience Utilisateur** :
    - Correction des liens contenus dans les emails envoyés ([#1529](https://github.com/SocialGouv/vao/issues/1529)).
    - Ajustement du libellé (wording) des emails de refus d'agrément ([#1524](https://github.com/SocialGouv/vao/issues/1524)).
    - Amélioration de la gestion des modifications de séjours ([#1516](https://github.com/SocialGouv/vao/issues/1516)).

### Évolutions techniques
- **Mise à jour du socle technologique** :
    - Migration vers Nuxt v4 ([#1544](https://github.com/SocialGouv/vao/issues/1544)).
    - Passage à Node.js 24 ([#1549](https://github.com/SocialGouv/vao/issues/1549)).
- **Architecture et Développement** :
    - Refonte de l'architecture des compétences liées à l'IA ([#1534](https://github.com/SocialGouv/vao/issues/1534)).
    - Implémentation de *feature flags* pour le déploiement progressif du module hébergement ([#1533](https://github.com/SocialGouv/vao/issues/1533)).
    - Réinitialisation du store d'agrément lors de la déconnexion pour renforcer la sécurité des sessions ([#1517](https://github.com/SocialGouv/vao/issues/1517)).
- **Tests et Cartographie** :
    - Correction et stabilisation des tests de bout en bout (E2E) suite aux changements d'interface ([#1554](https://github.com/SocialGouv/vao/issues/1554)).
    - Mise à jour de la bibliothèque de cartographie MapLibre-GL vers la v5.

### Autres changements
- Ajout d'une authentification de base pour l'outil de test de messagerie Maildev ([#1541](https://github.com/SocialGouv/vao/issues/1541)).
