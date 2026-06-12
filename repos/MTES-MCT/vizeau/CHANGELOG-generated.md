## Changelog : vizeau (30 derniers jours, au 11 juin 2026)

### Résumé
Ce mois-ci, Vizeau a connu des avancées significatives dans la gestion des projets, l'expérience utilisateur et l'administration du système. Les utilisateurs peuvent désormais créer des projets avec des étapes définies, attacher des exploitations et des parcelles à ces projets, et bénéficier d'une interface améliorée pour la visualisation de la qualité de l'eau. Des commandes CLI ont été ajoutées pour faciliter l'administration et le seeding des données.

### Évolutions fonctionnelles
- Ajout d'un formulaire de création de projet avec un système d'étapes ([#436](https://github.com/MTES-MCT/vizeau/pull/436), [#426](https://github.com/MTES-MCT/vizeau/pull/426)).
- Possibilité d'attacher des exploitations, parcelles et captages aux projets ([#425](https://github.com/MTES-MCT/vizeau/pull/425), [#432](https://github.com/MTES-MCT/vizeau/pull/432), [#434](https://github.com/MTES-MCT/vizeau/pull/434)).
- Amélioration de la page de visualisation synthétique de la qualité de l'eau ([#424](https://github.com/MTES-MCT/vizeau/pull/424)).
- Ajout d'une page "en construction" pour les projets ([#427](https://github.com/MTES-MCT/vizeau/pull/427)).
- Correction de l'affichage de l'évolution des parcelles bio (passage de % à ha) ([#428](https://github.com/MTES-MCT/vizeau/pull/428)).
- Correction de l'affichage des couleurs dans la répartition des cultures ([#431](https://github.com/MTES-MCT/vizeau/pull/431)).
- Ajout d'une commande CLI pour réinitialiser le mot de passe d'un utilisateur ([#434](https://github.com/MTES-MCT/vizeau/pull/434)).
- Possibilité de créer de nouveaux territoires via la CLI ([#410](https://github.com/MTES-MCT/vizeau/pull/410)).
- Amélioration de la visualisation du suivi des substances ([#409](https://github.com/MTES-MCT/vizeau/pull/409)).
- Tri des substances affichées dans la liste déroulante ([#407](https://github.com/MTES-MCT/vizeau/pull/407)).

### Évolutions techniques
- Refactorisation des filtres pour améliorer la performance et la maintenabilité ([#435](https://github.com/MTES-MCT/vizeau/pull/435)).
- Passage de la CI à Node 24 pour bénéficier des dernières améliorations et correctifs de sécurité ([#429](https://github.com/MTES-MCT/vizeau/pull/429)).
- Mise à jour des variables d'environnement de la CI pour une meilleure configuration.
- Corrections de mocks et amélioration de la gestion d'erreur lors d'un export CSV.
- Correction d'une mauvaise requête SQL.

### Autres changements
- Mise à jour de la documentation de migration en production ([#433](https://github.com/MTES-MCT/vizeau/pull/433)).
- Amélioration de la gestion des tests et corrections diverses.
- Corrections et améliorations diverses de l'interface utilisateur.
- Suppression de code inutile et nettoyage général du code.
