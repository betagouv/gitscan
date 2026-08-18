## Changelog : vao (30 derniers jours, au 16 août 2026)

### Résumé
Ce mois a été marqué par un développement intensif du processus de "Premier Agrément" (DREETS), incluant désormais la gestion complète des demandes de compléments, des corrections et des refus. Parallèlement, plusieurs stabilisations ont été effectuées sur les parcours "Fusager" et les outils d'administration pour améliorer la fiabilité des saisies et des droits d'accès.

### Évolutions fonctionnelles

**Gestion du Premier Agrément (DREETS)**
- Mise en place de la page dédiée au premier agrément [#1501](https://github.com/SocialGouv/vao/issues/1501).
- Gestion du cycle de vie des demandes : demande de compléments [#1492](https://github.com/SocialGouv/vao/issues/1492), gestion des modifications suite aux demandes [#1493](https://github.com/SocialGouv/vao/issues/1493) et confirmation de la complétude des dossiers [#1498](https://github.com/SocialGouv/vao/issues/1498).
- Gestion des refus : interface côté DREETS [#1495](https://github.com/SocialGouv/vao/issues/1495) et mise à jour des modèles d'emails de notification [#1497](https://github.com/SocialGouv/vao/issues/1497).
- Validation du premier agrément [#1506](https://github.com/SocialGouv/vao/issues/1506) et prise en compte des corrections demandées [#1504](https://github.com/SocialGouv/vao/issues/1504).

**Parcours Fusager & Agrément**
- Ajout de la possibilité de supprimer un agrément directement depuis le formulaire d'organisme [#1507](https://github.com/SocialGouv/vao/issues/1507).
- Correction des contrôles sur l'âge et le handicap [#1515](https://github.com/SocialGouv/vao/issues/1515).
- Résolution d'erreurs lors de la création d'organismes [#1512](https://github.com/SocialGouv/vao/issues/1512) et de problèmes de permissions lors des vérifications EIG [#1510](https://github.com/SocialGouv/vao/issues/1510).

**Back-office & Administration**
- Masquage des sections RGAA et Bilan dans l'interface [#1491](https://github.com/SocialGouv/vao/issues/1491).
- Amélioration de la visibilité de la liste de validation des comptes OVA [#1513](https://github.com/SocialGouv/vao/issues/1513).

**Corrections diverses**
- Correction de la validation des dates de visite pour l'hébergement [#1505](https://github.com/SocialGouv/vao/issues/1505).
- Ajustement du bouton de refus lors de la validation de compte [#1500](https://github.com/SocialGouv/vao/issues/1500).
- Amélioration de la formulation concernant la mention du casier judiciaire [#1499](https://github.com/SocialGouv/vao/issues/1499).

### Évolutions techniques

**Infrastructure & CI/CD**
- Migration de la construction des images vers `buildkit-operator` [#1464](https://github.com/SocialGouv/vao/issues/1464).

**Qualité du code**
- Résolution de problèmes de duplication de code identifiés par Sonar [#1515](https://github.com/SocialGouv/vao/issues/1515).
