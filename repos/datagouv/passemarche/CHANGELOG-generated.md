## Changelog : passemarche (30 derniers jours, au 20 octobre 2026)

### Résumé
Ce mois-ci, l'application a franchi une étape majeure dans la gestion des candidatures en groupement. Le travail collaboratif est désormais au cœur de l'expérience : les co-traitants peuvent rejoindre un groupement, remplir leur partie et sélectionner leurs lots de manière autonome, permettant au mandataire de soumettre l'ensemble de la candidature en un clic.

### Évolutions fonctionnelles
- **Collaboration en groupement** : les co-traitants peuvent désormais rejoindre un groupement via une invitation, sauvegarder leur partie en brouillon et la transmettre au mandataire ([#572](https://github.com/datagouv/passemarche/pull/572)).
- **Gestion des lots** : les co-traitants peuvent sélectionner les lots qui les concernent au sein du périmètre du groupement ([#562](https://github.com/datagouv/passemarche/pull/562)). Une option permet également de désactiver la limitation du nombre de lots par candidat ([#563](https://github.com/datagouv/passemarche/pull/563)).
- **Soumission simplifiée** : le mandataire peut désormais soumettre la candidature complète du groupement, ce qui verrouille automatiquement l'accès aux modifications pour tous les membres ([#549](https://github.com/datagouv/passemarche/pull/549), [#568](https://github.com/datagouv/passemarche/pull/568)).
- **Tableau de bord et suivi** : amélioration de l'interface de suivi pour le mandataire, incluant la visualisation des lots et le statut de progression des membres du groupement ([#526](https://github.com/datagouv/passemarche/pull/526)).
- **Communications et notifications** : refonte des emails (mise en page, images intégrées, terminologie plus précise) et ajout de notifications lors de la transmission des formulaires ou de la soumission finale ([#569](https://github.com/datagouv/passemarche/pull/569), [#570](https://github.com/datagouv/passemarche/pull/570)).
- **Expérience utilisateur** : création de pages dédiées pour la gestion des invitations (cas où l'invitation est expirée ou non trouvée) ([#534](https://github.com/datagouv/passemarche/pull/534)).

### Évolutions techniques
- **Traçabilité et audit** : mise en place d'un historique complet des modifications des membres et des groupements via l'intégration de `paper_trail` ([#570](https://github.com/datagouv/passemarche/pull/570)).
- **Refactoring de l'interface** : migration de composants clés (gestion des lots, membres du groupement) vers `ViewComponents` pour une meilleure modularité et réutilisation ([#541](https://github.com/datagouv/passemarche/pull/541), [#540](https://github.com/datagouv/passemarche/pull/540)).
- **Architecture CSS** : découpage du fichier CSS principal en fichiers thématiques par domaine pour faciliter la maintenance ([#539](https://github.com/datagouv/passemarche/pull/539)).
- **Tests** : renforcement significatif de la couverture de tests (Cucumber et RSpec) sur les parcours critiques de groupement, de co-traitance et de soumission.

### Autres changements
- **Internationalisation** : amélioration et correction de la traduction anglaise du tableau de bord des groupements ([#538](https://github.com/datagouv/passemarche/pull/538)).
- **Correction PDF** : résolution d'un problème d'encodage UTF-8 pour les dates dans les documents PDF générés ([#542](https://github.com/datagouv/passemarche/pull/542)).
