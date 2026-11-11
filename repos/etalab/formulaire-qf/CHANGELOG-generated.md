## Changelog : formulaire-qf (30 derniers jours, au 10 novembre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur la sécurisation des données personnelles et la fiabilisation du processus de transmission du quotient familial. Les utilisateurs bénéficieront d'une gestion de session plus robuste avec FranceConnect et de corrections visant à éviter les erreurs de saisie ou les doubles envois accidentels.

### Évolutions fonctionnelles
- **Sécurisation des envois** : Empêche les doubles envois de dossiers lors d'un clic répété sur le bouton « Transmettre » [#434](https://github.com/etalab/formulaire-qf/pull/434).
- **Amélioration du suivi** : Optimisation de l'affichage des numéros de dossier et ajout de liens de retour pour faciliter la navigation [#438](https://github.com/etalab/formulaire-qf/pull/438).
- **Expérience FranceConnect** : Amélioration de la gestion des sessions pour éviter les confusions de données entre différents usagers lors de la connexion [#433](https://github.com/etalab/formulaire-qf/pull/433).
- **Fiabilité des données** : Mise en place d'alertes en cas de numéro de téléphone manquant pour les transmissions DataPass [#405](https://github.com/etalab/formulaire-qf/pull/405).
- **Navigation** : Correction de l'affichage lors de la sélection d'une collectivité [#433](https://github.com/etalab/formulaire-qf/pull/433).

### Évolutions techniques
- **Protection des données (RGPD)** : Nettoyage majeur pour empêcher l'envoi de données sensibles (identité, quotient familial, téléphone, emails) vers l'outil de suivi d'erreurs Sentry [#406](https://github.com/etalab/formulaire-qf/pull/406), [#404](https://github.com/etalab/formulaire-qf/pull/404), [#393](https://github.com/etalab/formulaire-qf/pull/393).
- **Mises à jour majeures** : Montée de version de Ruby (4.0.9) [#414](https://github.com/etalab/formulaire-qf/pull/414), Rails (8.1.4.1) [#427](https://github.com/etalab/formulaire-qf/pull/427) et GoodJob (4.24) [#430](https://github.com/etalab/formulaire-qf/pull/430).
- **Maintenance de la base de données** : Automatisation du nettoyage des sessions inactives pour optimiser le stockage et les performances [#432](https://github.com/etalab/formulaire-qf/pull/432).
- **Sécurité de la CI** : Renforcement de la chaîne d'intégration continue pour bloquer l'utilisation de dépendances présentant des vulnérabilités connues [#421](https://github.com/etalab/formulaire-qf/pull/421).

### Autres changements
- **Documentation** : Mise à jour des guides de développement (`CLAUDE.md`) pour inclure les nouvelles conventions et l'usage de Sentry [#417](https://github.com/etalab/formulaire-qf/pull/417), [#423](https://github.com/etalab/formulaire-qf/pull/423).
- **Outillage de développement** : Ajout de scripts pour faciliter le travail en environnement de développement isolé (worktrees) [#394](https://github.com/etalab/formulaire-qf/pull/394).
