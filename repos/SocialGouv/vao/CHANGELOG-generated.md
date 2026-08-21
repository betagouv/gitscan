## Changelog : vao (30 derniers jours, au 20 août 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur la stabilisation du processus de "premier agrément", particulièrement pour les utilisateurs de la DREETS, et sur l'amélioration des outils de gestion dans le back-office. Plusieurs corrections ont été apportées pour fluidifier la saisie des données (dates, contrôles d'âge) et affiner les messages envoyés aux utilisateurs.

### Évolutions fonctionnelles

**Gestion des premiers agréments (DREETS)**
- Mise en place de la page dédiée aux premiers agréments ([#1501](https://github.com/SocialGouv/vao/issues/1501)).
- Ajout de la confirmation de complétude des dossiers pour faciliter le suivi ([#1498](https://github.com/SocialGouv/vao/issues/1498)).
- Amélioration de la gestion des refus : interface dédiée côté DREETS et correction des libellés dans les emails de notification ([#1495](https://github.com/SocialGouv/vao/issues/1495), [#1497](https://github.com/SocialGouv/vao/issues/1497)).

**Back-Office & Administration**
- Ajout de fonctionnalités de validation pour les premiers agréments ([#1506](https://github.com/SocialGouv/vao/issues/1506)).
- Amélioration de la visibilité de la validation des comptes OVA dans les listes ([#1513](https://github.com/SocialGouv/vao/issues/1513)).
- Simplification de l'interface par le masquage des sections RGAA et Bilan ([#1491](https://github.com/SocialGouv/vao/issues/1491)).

**Gestion des organismes et des dossiers**
- Possibilité de supprimer un agrément directement depuis le formulaire d'organisme ([#1507](https://github.com/SocialGouv/vao/issues/1507)).
- Correction d'erreurs lors de la création d'organismes pour les agréments ([#1512](https://github.com/SocialGouv/vao/issues/1512)).
- Autorisation de la suppression ou de la modification des séjours et bilans liés aux agréments ([#1516](https://github.com/SocialGouv/vao/issues/1516)).

**Corrections et expérience utilisateur**
- Résolution de problèmes de contrôles de cohérence (âge et déficience) lors des agréments ([#1515](https://github.com/SocialGouv/vao/issues/1515)).
- Correction des règles de validation concernant les dates de visite des hébergements ([#1505](https://github.com/SocialGouv/vao/issues/1505)).
- Correction de problèmes de permissions sur les contrôles EIG ([#1511](https://github.com/SocialGouv/vao/issues/1511)).
- Ajustements de l'interface : correction du bouton de refus de validation de compte ([#1500](https://github.com/SocialGouv/vao/issues/1500)) et des libellés relatifs au casier judiciaire ([#1499](https://github.com/SocialGouv/vao/issues/1499)).

### Évolutions techniques

**Infrastructure & CI/CD**
- Migration de la construction des images vers `buildkit-operator` pour optimiser les processus de déploiement ([#1464](https://github.com/SocialGouv/vao/issues/1464)).

**Qualité du code**
- Refactoring de plusieurs modules pour réduire la duplication de code signalée par les outils d'analyse (Sonar).
